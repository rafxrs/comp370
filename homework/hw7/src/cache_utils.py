from pathlib import Path
import time
import requests

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

def get_cached(url, sleep_time=1.0):
    """Return page content, using cached copy if available."""
    cache_file = CACHE_DIR / (url.replace("https://", "").replace("/", "_") + ".html")

    if cache_file.exists():
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()

    print(f"Fetching {url}")
    time.sleep(sleep_time)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    html = r.text

    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(html)

    return html
