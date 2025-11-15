#!/usr/bin/env python3
import json
import argparse
import random
import sys

def main():
    parser = argparse.ArgumentParser(description="Extract random Reddit posts to TSV")
    parser.add_argument("-o", "--out", help="Output TSV file", required=True)
    parser.add_argument("json_file", help="Input Reddit JSON file")
    parser.add_argument("num_posts", type=int, help="Number of posts to output")
    args = parser.parse_args()

    # Load JSON
    try:
        with open(args.json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

    # Reddit posts live in data["data"]["children"]
    try:
        posts = data["data"]["children"]
    except KeyError:
        print("Error: Input JSON does not look like Reddit /new.json format.")
        sys.exit(1)

    # Extract (name, title) pairs
    extracted = []
    for p in posts:
        pdata = p.get("data", {})
        name = pdata.get("name", "")
        title = pdata.get("title", "")

        if name and title:
            extracted.append((name, title))

    if len(extracted) == 0:
        print("Error: No posts found in JSON.")
        sys.exit(1)

    # Random selection (or all if requested > available)
    num_to_output = min(args.num_posts, len(extracted))
    selected = random.sample(extracted, num_to_output)

    # Write to TSV
    with open(args.out, "w", encoding="utf-8") as out:
        out.write("Name\ttitle\tcoding\n")
        for name, title in selected:
            out.write(f"{name}\t{title}\t\n")

    print(f"Wrote {num_to_output} posts to {args.out}")


if __name__ == "__main__":
    main()
