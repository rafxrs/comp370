import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from src.cache_utils import get_cached

BASE_URL = "https://montrealgazette.com"
NEWS_URL = f"{BASE_URL}/category/news/"

def _absolute(href):
    if not href:
        return None
    return urljoin(BASE_URL, href)

def get_trending_links(max_links=5):
    """
    Extract all trending article URLs using the 'widget_title': 'Trending' JSON
    embedded in the <article data-evt-val='...'> attributes.
    """
    html = get_cached(NEWS_URL)
    soup = BeautifulSoup(html, "html.parser")

    links = []

    # Each trending article has data-evt-val JSON with "widget_title": "Trending"
    for article in soup.find_all("article"):
        val = article.get("data-evt-val")
        if not val or "widget_title" not in val:
            continue
        try:
            data = json.loads(val)
        except Exception:
            # Some articles use single quotes or escaped quotes → fix first
            fixed = (
                val.replace("\\'", "'")
                .replace('\\"', '"')
                .replace("“", '"')
                .replace("”", '"')
            )
            try:
                data = json.loads(fixed)
            except Exception:
                continue

        widget = data.get("widget_title", "")
        target_url = data.get("target_url")

        if widget == "Trending" and target_url:
            url = _absolute(target_url)
            if url not in links:
                links.append(url)

        if len(links) >= max_links:
            break

    return links[:max_links]

def scrape_article(url):
    """
    Scrape article metadata (title, author, date, blurb)
    using structured data <script type="application/ld+json">,
    with fallbacks to meta tags.
    """
    html = get_cached(url)
    soup = BeautifulSoup(html, "html.parser")

    title = None
    pub_date = None
    author = "Unknown"
    blurb = ""

    # 1. Structured JSON-LD block
    for script in soup.find_all("script", {"type": "application/ld+json"}):
        if not script.string:
            continue
        try:
            data = json.loads(script.string)
        except Exception:
            continue

        # Single dict or list of dicts
        items = data if isinstance(data, list) else [data]
        for item in items:
            if item.get("@type") in ["NewsArticle", "Article", "BlogPosting"]:
                title = item.get("headline") or title
                pub_date = item.get("datePublished") or item.get("dateCreated") or pub_date

                # author may be dict, list, or string
                a = item.get("author")
                if isinstance(a, list) and a and isinstance(a[0], dict):
                    author = a[0].get("name", author)
                elif isinstance(a, dict):
                    author = a.get("name", author)
                elif isinstance(a, str):
                    author = a
                blurb = item.get("description") or blurb
                break
        if title or pub_date:
            break

    # 2. Fallback to meta tags
    if not title:
        meta = soup.find("meta", property="og:title") or soup.find("meta", property="twitter:title")
        if meta and meta.has_attr("content"):
            title = meta["content"].strip()

    if not pub_date:
        meta = soup.find("meta", {"property": "article:published_time"})
        if meta and meta.has_attr("content"):
            pub_date = meta["content"].strip()

    if author == "Unknown":
        meta = soup.find("meta", {"name": "author"})
        if meta and meta.has_attr("content"):
            author = meta["content"].strip()

    if not blurb:
        meta = soup.find("meta", {"name": "description"}) or soup.find("meta", {"property": "og:description"})
        if meta and meta.has_attr("content"):
            blurb = meta["content"].strip()
        else:
            p = soup.find("p")
            blurb = p.get_text(strip=True) if p else ""

    return {
        "title": title,
        "publication_date": pub_date,
        "author": author,
        "blurb": blurb,
    }
