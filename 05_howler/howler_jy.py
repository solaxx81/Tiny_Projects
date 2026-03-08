#!/usr/bin/env python3
"""
Author : JYM <jymo81.dude451@slmail.me>
Date   : 2026-03-07
Purpose: Write a program that uppercase's the given text
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", type=str, help="Input text or file")

    parser.add_argument("-o", "--outfile", type=str, help="Output filename", metavar="str", default="")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Exécution principale : c'est ici que cela se passe."""

    args = get_args()

    if args.outfile:
        out_fh = open(args.outfile, "wt")
        out_fh.write(args.text.upper())
    else:
        print(args.text.upper())


# --------------------------------------------------
if __name__ == "__main__":
    main()
