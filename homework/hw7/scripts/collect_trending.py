"""
CLI entrypoint to scrape top 5 trending Montreal Gazette stories.

Usage:
    python scripts/collect_trending.py -o trending.json
"""

import argparse
from src.scraper import get_trending_links, scrape_article
from src.io_utils import save_to_json

def main():
    parser = argparse.ArgumentParser(description="Collect top 5 trending Montreal Gazette stories.")
    parser.add_argument("-o", "--output", required=True, help="Output JSON filename (e.g. trending.json)")
    args = parser.parse_args()

    trending_links = get_trending_links()
    results = [scrape_article(url) for url in trending_links]

    save_to_json(results, args.output)
    print(f"Saved {len(results)} articles to {args.output}")

if __name__ == "__main__":
    main()
