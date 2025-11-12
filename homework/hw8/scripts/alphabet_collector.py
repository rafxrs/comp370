import random  # For random delays
import argparse  # For command-line parsing
import collections  # For deque, which we use as a queue (BFS)
import json  # For reading/writing cache
import os  # For file existence checks
import re  # For regex to find age/gender and normalize
import time  # For sleep between requests
import string  # For ascii_lowercase
from typing import Dict, Any, List, Optional, Set  # For type hints
import requests  # For HTTP requests
from bs4 import BeautifulSoup, NavigableString  # For HTML parsing

# -------------------------- CONSTANTS -------------------------- #

BASE_URL = "https://www.whosdatedwho.com"  # Base domain for the site
CACHE_PATH = "wdw_cache_alphabet.json"  # Where we store cached HTML

# -------------------------- CACHE HELPERS -------------------------- #

def load_cache() -> Dict[str, str]:
    """Load the cache file if it exists; otherwise return an empty dict."""
    # Check if the cache file exists
    if os.path.exists(CACHE_PATH):
        # Open and read JSON into a dict
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    # If no file, return empty cache
    return {}

def save_cache(cache: Dict[str, str]) -> None:
    """Save the given cache dictionary to disk."""
    # Open file in write mode and dump the dict as JSON
    # make sure the file is in pretty json format
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)

def fetch_url(url: str, cache: Dict[str, str]) -> Optional[str]:
    """
    Fetch HTML for a URL, using the cache to avoid re-downloading.
    Returns the HTML string or None if request fails.
    """
    # If we already have it cached, return right away
    if url in cache:
        return cache[url]
    # Otherwise, sleep to be polite
    request_delay_seconds = random.uniform(0.1, 0.5)  # Delay between real HTTP requests to be respectful
    time.sleep(request_delay_seconds)
    # Make the HTTP request with a simple UA
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (assignment scraper)"})
    # If the response is not OK, report and return None
    if resp.status_code != 200:
        print(f"[warn] could not fetch {url} (status {resp.status_code})")
        return None
    # Get HTML text
    html_text = resp.text
    # Store in cache
    cache[url] = html_text
    # Save cache to disk
    save_cache(cache)
    # Return the HTML
    return html_text

# -------------------------- NAME / SLUG HELPERS -------------------------- #

def slugify_name(name: str) -> str:
    """Turn a display name like 'Justin Bieber' into 'justin-bieber'."""
    # Trim, lowercase
    name = name.strip().lower()
    # Replace whitespace with dashes
    name = re.sub(r"\s+", "-", name)
    # Remove non-alphanumeric/dash
    name = re.sub(r"[^a-z0-9\-]", "", name)
    # Return slug
    return name

def slug_to_display_name(slug: str) -> str:
    """Turn 'justin-bieber' back into 'Justin Bieber'."""
    # Replace dashes with spaces
    name = slug.replace("-", " ")
    # Title-case the result
    return name.title()

def build_profile_url_from_slug(slug: str) -> str:
    """Build the URL to a celebrity profile from a slug."""
    # Combine base + /dating/ + slug
    return f"{BASE_URL}/dating/{slug}"

# start_tag, end_tag are what's returned by BeautifulSoup's find() method
def extract_html_between_tags(html: str, start_tag, end_tag) -> str:
    """
    Extract the raw HTML (including tags like <p>, <div>, etc.)
    between two specified tags in the HTML.
    tags are given as strings, e.g. "h1[style='font-size: 1.2rem;']", "h4[class='ff-auto-relationships']"
    """
    start_elem = start_tag
    end_elem = end_tag

    # If either is missing, return empty string
    if not start_elem or not end_elem:
        return ""

    # Collect all elements between them
    parts = []
    for elem in start_elem.next_siblings:
        if elem == end_elem:
            break
        parts.append(str(elem))

    # Join and strip any leading/trailing whitespace
    return "".join(parts).strip()

# -------------------------- META EXTRACTION (AGE / GENDER) -------------------------- #

def extract_age_and_gender_from_profile(html: str) -> Dict[str, Optional[str]]:
    """
    Best-effort extraction of age and gender from the profile HTML.
    Returns a dict with keys 'age' and 'gender', values are strings or None.
    Age is extracted from e.g. <div class="ff-fact-box small age"><div class="header">Age</div><div class="fact ">31</div><div class="footer">years old</div></div>
    Gender is inferred from text between <h4 class="ff-auto-about">About</h4> and <h4 class="ff-auto-contribute">Contribute</h4>
    You can infer gender by the pronouns used in the text between About and Contribute.
    If he/him/his is used, gender is Male.
    If she/her/hers is used, gender is Female.
    """
    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")
    # Get all text for easy regex matching
    full_text = soup.get_text(" ", strip=True)

    # Start with None
    age_val: Optional[str] = None
    gender_val: Optional[str] = None

    # Try to find age pattern
    age_related_text = soup.find("div", class_="ff-fact-box small age")
    if age_related_text:
        fact_div = age_related_text.find("div", class_="fact") 
        if fact_div:
            age_text = fact_div.get_text(strip=True)
            if age_text.isdigit():
                age_val = int(age_text)

    # Try to infer gender from text between About and Contribute
    about_h4 = soup.find("h4", class_="ff-auto-about")
    contribute_h4 = soup.find("h4", class_="ff-auto-contribute")
    about_html = extract_html_between_tags(html, about_h4, contribute_h4)

    if about_html:
        about_lower = "".join(about_html).lower()
        # Check for gender, be aware that she is a substring of he
        # so check for she/her/hers first
        if "she" in about_lower or "her" in about_lower or "hers" in about_lower:
            gender_val = "female"
        elif "he" in about_lower or "him" in about_lower or "his" in about_lower:
            gender_val = "male"
        else:
            gender_val = None

    # Return what we found
    return {"age": age_val, "gender": gender_val}

def parse_names_and_slugs_from_letter_page(html, per_letter):
    soup = BeautifulSoup(html, "html.parser")

    names = []
    slugs = []

    box = soup.find("div", class_="ff-box-grid ff-medium-square") 

    # breakpoint()

    for li in box.find_all("li"):
        link_a = li.find("a", href=True)
        name_div = link_a.find("div", class_="ff-name")
        link = link_a['href']
        if name_div is None or not link.startswith(f"{BASE_URL}/dating/"):
            continue
        name = name_div.get_text(strip=True)
        # get slug from the link
        slug = link.replace(f"{BASE_URL}/dating/", "").strip("/")

        names.append(name)
        slugs.append(slug)
        # break if reach target counts
        if len(names) >= per_letter:
            break
    return names, slugs

def alphabet_collect(per_letter):
    cache = load_cache()
    results = []

    for letter in string.ascii_lowercase:
        letter_url = f"{BASE_URL}/popular?letter={letter.lower()}"
        letter_html = fetch_url(letter_url, cache)

        names, slugs = parse_names_and_slugs_from_letter_page(letter_html, per_letter)

        names = names[:per_letter]

        for name, slug in zip(names, slugs):
            profile_url = build_profile_url_from_slug(slug)
            profile_html = fetch_url(profile_url, cache)
            meta = extract_age_and_gender_from_profile(profile_html)
            celeb_record = {
                "name": name,  # keep original display name from the letter page
                "slug": slug,  # normalized slug
                "url": profile_url,  # link to their profile
                "age": meta.get("age"),  # maybe None
                "gender": meta.get("gender"),  # maybe None
            }
            results.append(celeb_record)

    return results

def main():
    """Command-line entry point."""
    # Set up argument parser
    parser = argparse.ArgumentParser()
    # How many per letter
    parser.add_argument(
        "--per-letter",
        type=int,
        default=1,
    )
    # Where to write JSON
    parser.add_argument(
        "--output",
        default="alphabet.json",
    )
    # Parse the arguments
    args = parser.parse_args()

    # Run the collection
    celebs = alphabet_collect(args.per_letter)

    # Write to JSON file
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(celebs, f, indent=2, ensure_ascii=False)

    # Print a quick summary
    print(f"Collected {len(celebs)} celebrities via alphabet sampling, saved to {args.output}")

# Standard Python entrypoint guard
if __name__ == "__main__":
    main()
