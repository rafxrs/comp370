import pandas as pd
import argparse

def fetch_data(path: str) -> pd.DataFrame:
    # load data from data folder
    df = pd.read_csv(path)
    # from the original data with 4 columns (title, writer, pony, dialog)
    # rename to 3 columns (episode, speaker, content)
    df = df.rename(columns={"title": "episode", "pony": "speaker", "dialog": "content"})
    # drop the writer column
    df = df.drop(columns=["writer"])
    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, default="data/clean_dialog.csv", help="Path to the input cleaned dialog CSV file")
    parser.add_argument("--output_path", type=str, default="data/processed_dialog.csv", help="Path to the output processed dialog CSV file")
    args = parser.parse_args()

    df = fetch_data(args.input_path)

    # clean content
    # remove "" characters
    df["content"] = df["content"].str.replace('"', '', regex=False)
    # remove unknown characters (anything between <>)
    df["content"] = df["content"].str.replace("<.*?>", "", regex=True)
    # remove ad libs (anything between [])
    df["content"] = df["content"].str.replace("\[.*?\]", "", regex=True)

    # save new data to data folder
    df.to_csv(args.output_path, index=False)

if __name__ == "__main__":
    main()