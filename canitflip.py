#!/usr/local/bin/py

import argparse

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('low_vote', type=float, help="Current loser's vote as percentage of reporting.")
    parser.add_argument('reporting', type=float, help='Percentage reporting. E.g. Enter "44" for 44% reporting')

    args = parser.parse_args()

    return args


def canitflip(reporting, low_vote):
    low_vote_of_total = (reporting / 100) * low_vote

    return low_vote_of_total + 100 - reporting > 50


if __name__ == "__main__":
    args = get_args()
    print(canitflip(args.reporting, args.low_vote))

