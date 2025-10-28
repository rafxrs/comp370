import argparse
from comedic import is_comedic_actor

def read_acting_csv(filepath):
    acting_names = []
    with open(filepath, 'r') as f:
        f_iter = iter(f)
        header = next(f_iter)  # skip header
        for line in f_iter:
            name = line.split(",")[-1].strip()
            acting_names.append(name)
    return acting_names

def main():
    parser = argparse.ArgumentParser();
    parser.add_argument("acting_csv")

    args = parser.parse_args()

    # open the acting csv
    acting_names = read_acting_csv(args.acting_csv)


    # count the number of comedic actors
    for name in acting_names:
        if is_comedic_actor(name):
            print(name)

    pass

if __name__ == "__main__":
    main()