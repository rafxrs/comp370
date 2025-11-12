import argparse
import os
import json
import re
import time
import requests
from bs4 import BeautifulSoup
import collections
import random

CACHE_PATH = "wdw_cache_snowball.json"
BASE_URL = "https://www.whosdatedwho.com/dating"

def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r") as f:
            return json.load(f)
    else:
        return {}

def save_cache(cache):
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)

def slugify_name(name: str):
    name = name.strip().lower()
    # replace space with -
    name = re.sub(r"\s+", "-", name)

    return name

def slug_to_display_name(slug):
    # replace space with -
    name = slug.replace("-", " ")
    name = name.title()
    return name

def build_profile_url_from_slug(slug: str):
    return f"{BASE_URL}/{slug}"

def fetch_url(url:str, cache): # return HTML, if in cache, lazy return, if not request
    if cache:
        if url in cache: # cache is a dict of {url: html}
            return cache[url]
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (assignment scraper)"})

    request_dalay_seconds = random.uniform(0.1, 0.5) # sleep between fetches
    time.sleep(request_dalay_seconds)

    # get the html from resp
    html = resp.text
    # store html to the value of url
    cache[url] = html
    # cache once visited
    save_cache(cache)

    return html

def extract_html_between_tags(html, start_tag, end_tag):
    if not start_tag or not end_tag:
        return ""
    # collect everything in between as text
    parts = []
    for tag in start_tag.next_siblings:
        if tag == end_tag:
            break
        parts.append(str(tag))

    return "".join(parts).strip()

def extract_age_and_gender_from_profile(html:str):
    # parse html
    soup = BeautifulSoup(html, "html.parser")

    full_text = soup.get_text(" ", strip=True)

    age_val = None
    gender_val = None

    # find age pattern
    age_related_text = soup.find("div", class_="ff-fact-box small age")
    if age_related_text:
        fact_div = age_related_text.find("div", class_="fact")
        if fact_div:
            age_text = fact_div.get_text(strip=True)
            age_val = int(age_text)
    # find gender pattern, extract text between about and contribute
    about_h4 = soup.find("h4", class_="ff-auto-about")
    contribute_h4 = soup.find("h4", class_="ff-auto-contribute")
    about_html = extract_html_between_tags(html, about_h4, contribute_h4)
    # this should return html between two tags
    # check if there is any pronoun we can use
    # because he is a substring of she, we should check she first

    if about_html:
        about_lower = about_html.lower()
        if "she" in about_lower or "her" in about_lower or "hers" in about_lower:
            gender_val = "female"
        elif "he" in about_lower or "him" in about_lower or "his" in about_lower:
            gender_val = "male"
        else:
            gender_val = None
    
    return {"age": age_val, "gender": gender_val} # this is meta data

def extract_partner_slugs_from_profile(html, current_slug):
    
    soup = BeautifulSoup(html, "html.parser")

    dating_history_h1 = soup.find("h1", style="font-size: 1.2rem;")
    if dating_history_h1 is None:
        current_partner_slugs = []

    relationships_h4 = soup.find("h4", class_="ff-auto-relationships")
    about_h4 = soup.find("h4", class_="ff-auto-about")
    if dating_history_h1 is None and relationships_h4 is None and about_h4 is None:
        return []

    current_relationship_html = None
    past_relationship_html = None

    if dating_history_h1 is not None and relationships_h4 is not None:
        current_relationship_html = extract_html_between_tags(
            html, dating_history_h1, relationships_h4
        )
    if relationships_h4 is not None and about_h4 is not None:
        past_relationship_html = extract_html_between_tags(
            html, relationships_h4, about_h4
        )

    # collect slugs
    partner_slugs = []

    def pull_slugs_from_html(html_:str):
        soup = BeautifulSoup(html_, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if not href.startswith("/dating/"): continue # only want links for people
            other_slug = href.replace("/dating/", "")
            # if self-loop, skip
            if other_slug == current_slug:
                continue
            partner_slugs.append(other_slug)

    if current_relationship_html:   
        pull_slugs_from_html(current_relationship_html)
    if past_relationship_html:
        pull_slugs_from_html(past_relationship_html)
    
    unique_slugs = list(set(partner_slugs))
    return unique_slugs



def snowball_collect(start_name: str, target_count: int):
    """
    Snowball sampling: BFS (COMP 250)
    This can be done by queue
    - check out cache (be respectful, avoid being blocked)
    - put the start cele into the queue
    - pop 
    - fetch url
    - parse the html, find age and gender, find other people
    - enquene the people you found
    - repeat pop queue
    - until reach number of targets
    """
    # load cache
    cache = load_cache()

    # init the queue for BFS
    queue = collections.deque()

    # put name/slug of start into the queue
    start_slug = slugify_name(start_name)
    queue.append(start_slug)

    # use the queue for BFS
    # need to check if the current person has been visited
    seen = set()
    results = []
    # BFS
    while queue:
        current_slug = queue.popleft()
        if current_slug in seen:
            continue # skip if seen
        # fetch url
        profile_url = build_profile_url_from_slug(current_slug) # return a dict with meta data
        # breakpoint()
        html = fetch_url(profile_url, cache)

        if html is None:
            print("HTML not found in the url: ", profile_url)
            continue # skip if not found

        # find age and gender
        meta = extract_age_and_gender_from_profile(html)

        celeb_record ={
            "name": slug_to_display_name(current_slug),
            "slug": current_slug,
            "url": profile_url,
            "age": meta.get("age"),
            "gender": meta.get("gender")
        }

        results.append(celeb_record)

        # mark the current slug as seen
        seen.add(current_slug)

        if len(results) >= target_count:
            break
        
        # find partners' slugs
        # pass current slug avoid self-loop
        partner_slugs = extract_partner_slugs_from_profile(html, current_slug)

        for pslug in partner_slugs:
            if pslug not in seen and pslug not in queue:
                queue.append(pslug)
    
    return results



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--start")
    parser.add_argument("--target", type=int, default=3)

    parser.add_argument("--output", default="snowball.json")

    args = parser.parse_args()

    # return a list of dict
    celebs = snowball_collect(args.start, args.target)

    with open(args.output, "w") as f:
        json.dump(celebs, f, indent=2)

    print("Snowball Collection Completed.")


if __name__ == "__main__":
    main()