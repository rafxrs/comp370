import argparse
import pandas as pd
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Compare topic distributions for McGill vs Concordia.")
    parser.add_argument("mcgill_file", help="Path to final_labeled_dataset_mcgill.tsv")
    parser.add_argument("concordia_file", help="Path to final_labeled_dataset_concordia.tsv")
    parser.add_argument("-o", "--out", default="results.png", help="Output image file (default: results.png)")
    args = parser.parse_args()

    # Load data
    mcgill = pd.read_csv(args.mcgill_file, sep="\t")
    concordia = pd.read_csv(args.concordia_file, sep="\t")

    # Check expected column
    if "final_label" not in mcgill.columns or "final_label" not in concordia.columns:
        raise ValueError("Both TSV files must contain a column named 'final_label'.")

    # Count categories
    mc_counts = mcgill["final_label"].value_counts().sort_index()
    co_counts = concordia["final_label"].value_counts().sort_index()

    # Combine into a single DataFrame
    df = pd.DataFrame({"McGill": mc_counts, "Concordia": co_counts}).fillna(0)

    # Plot
    df.plot(kind="bar", figsize=(10, 6))
    plt.title("Topic Distribution: McGill vs Concordia")
    plt.xlabel("Category")
    plt.ylabel("Number of Posts")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Save output
    plt.savefig(args.out)
    print(f"Saved plot to {args.out}")

if __name__ == "__main__":
    main()