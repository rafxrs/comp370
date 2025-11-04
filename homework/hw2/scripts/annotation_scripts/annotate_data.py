import pandas as pd
import argparse

def main():
    df = pd.read_csv("data/processed_dialog.csv")
    # add column addressee - the character who’s dialogue immediately follows the speaker is the addressee
    # watch out for same person speaking more than once in a row
    iter = df.iterrows()
    next(iter)  # skip first row
    for index, row in iter:
        if row['speaker'] == df.at[index - 1, 'speaker']:
            df.at[index - 1, 'addressee'] = row['speaker']
        else:
            df.at[index - 1, 'addressee'] = row['speaker']
    df.to_csv("data/annotated_dialog.csv", index=False)

if __name__ == "__main__":
    main()