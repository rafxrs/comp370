"""
Count the number of unique author IDs in a dataset.
"""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("datafile", type=str, help="Path to the data file")
    parser.add_argument("blacklist", type=str, help="Path to the author ID blacklist file", default="data/author_id_blacklist.json")

    args = parser.parse_args()
    author_ids = set() # sets are used to store unique items and are optimized for membership tests
    
    if args.blacklist:
        import json
        with open(args.blacklist, "r") as bl_fh:
            author_id_blacklist = set(json.load(bl_fh)) # load blacklist into a set for fast lookup

    fh = open(args.datafile, "r")
    line_iterator = iter(fh) # create an iterator from the file handle
    line_iterator.__next__()  # skip header line

    for line in line_iterator:
        parts = line.strip().split(',')
        if len(parts) > 1:
            author_id = parts[0]
            if author_id not in author_id_blacklist:
                author_ids.add(author_id)

    print(f"Number of unique author IDs: {len(author_ids)}")

if __name__ == "__main__":
    main()