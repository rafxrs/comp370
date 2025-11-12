#!/usr/bin/env python3
import argparse
import csv
from datetime import datetime
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Count complaint types per borough within a date range."
    )
    parser.add_argument("-i", "--input", required=True, help="Input CSV file")
    parser.add_argument("-s", "--start", required=True, help="Start date (MM/DD/YYYY)")
    parser.add_argument("-e", "--end", required=True, help="End date (MM/DD/YYYY)")
    parser.add_argument("-o", "--output", help="Output file (optional)")
    args = parser.parse_args()

    start = datetime.strptime(args.start, "%m/%d/%Y")
    end = datetime.strptime(args.end, "%m/%d/%Y")

    complaint_counts = {}

    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            try:
                created_date = datetime.strptime(row[1], "%m/%d/%Y %I:%M:%S %p")
            except ValueError:
                continue  # skip malformed dates

            if not (start <= created_date <= end):
                continue

            complaint_type = row[5].strip()
            borough = row[25].strip()
            if not complaint_type or not borough:
                continue

            key = (complaint_type, borough)
            complaint_counts[key] = complaint_counts.get(key, 0) + 1

    output = sys.stdout if not args.output else open(args.output, "w", newline="", encoding="utf-8")
    writer = csv.writer(output)
    writer.writerow(["complaint type", "borough", "count"])
    for (ctype, borough), count in sorted(complaint_counts.items()):
        writer.writerow([ctype, borough, count])
    if args.output:
        output.close()

if __name__ == "__main__":
    main()
