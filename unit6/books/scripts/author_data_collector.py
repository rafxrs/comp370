import requests
import os.path as osp
import json
import argparse

scripts_path = osp.dirname(__file__)
raw_path = osp.join(scripts_path, "..", "data","raw")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("author_name", type=str, help="Name of the author to query")
    args = parser.parse_args()

    author = args.author_name.replace(" ", "%20")

    # get author's key
    query_url = f"https://openlibrary.org/search/authors.json?q={author}"
    r = requests.get(query_url)

    author_data = r.json()
    author_key = author_data['docs'][0]['key']
    print(f"Author Key: {author_key}")

    # query for books
    books_url = f"https://openlibrary.org/authors/{author_key}/works.json"
    r = requests.get(books_url)

    books_data = r.json()
    
    # write out the raw data
    fname = f"author_{author_key}_works.json"

    with open(osp.join(raw_path, fname), "w") as f:
        json.dump(books_data, f, indent=4)

if __name__ == "__main__":
    main()