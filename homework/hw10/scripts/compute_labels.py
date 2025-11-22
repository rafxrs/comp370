import argparse
import pandas as pd
from collections import Counter
import os

def main():
    parser = argparse.ArgumentParser(description="Compute annotator agreement and produce final labeled dataset.")
    parser.add_argument("input_file", help="TSV with 3 annotator columns")
    parser.add_argument("output_file", help="Output TSV for final labeled dataset")
    args = parser.parse_args()

    # Load the TSV
    df = pd.read_csv(args.input_file, sep="\t")

    # Auto-detect coding columns
    coding_cols = [col for col in df.columns if col.startswith("coding")]
    if len(coding_cols) != 3:
        raise ValueError(f"Expected 3 coding columns, found {len(coding_cols)}: {coding_cols}")

    c1, c2, c3 = coding_cols

    # Functions
    def full_agreement(row):
        return row[c1] == row[c2] == row[c3]

    def majority_label(row):
        labels = [row[c1], row[c2], row[c3]]
        return Counter(labels).most_common(1)[0][0]

    def majority_agreement(row):
        labels = [row[c1], row[c2], row[c3]]
        return Counter(labels).most_common(1)[0][1] >= 2

    # Apply functions
    df["full_agreement"] = df.apply(full_agreement, axis=1)
    df["majority_agreement"] = df.apply(majority_agreement, axis=1)
    df["final_label"] = df.apply(majority_label, axis=1)

    # Write final labeled dataset EXACTLY as requested
    df_out = df[["Name", "title", "final_label"]]
    df_out.to_csv(args.output_file, sep="\t", index=False)

    # Write summary
    summary_file = args.output_file.replace(".tsv", "_agreement_summary.txt")
    with open(summary_file, "w") as f:
        f.write(f"Total posts: {len(df)}\n")
        f.write(f"Full agreement: {df['full_agreement'].sum()}\n")
        f.write(f"Majority agreement: {df['majority_agreement'].sum()}\n")
        f.write(f"No-agreement cases: {len(df) - df['majority_agreement'].sum()}\n")

if __name__ == "__main__":
    main()
