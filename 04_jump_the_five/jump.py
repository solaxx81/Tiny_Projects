#!/usr/bin/env python3
"""
Author : JYM <jymo81.dude451@slmail.me>
Date   : 2026-03-06
Purpose:    Jump the Five
            In this exercise, we’re going to write a Python program called jump.py that will
            take in some text as a positional argument. Each number in the text will be
            encoded using this algorithm. All non-number text will pass through unchanged.

            Here are a couple of examples:
                $ ./jump.py 867-5309
                243-0751
                $ ./jump.py 'Call 1-800-329-8044 today!'
                Call 9-255-781-2566 today!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Exécution principale : c'est ici que cela se passe."""

    args = get_args()
    str_arg = args.text or ""
    jumper = {"1": "9", "2": "8", "3": "7", "4": "6", "5": "0", "6": "4", "7": "3", "8": "2", "9": "1", "0": "5"}

    sortie: list[str] = [jumper.get(char, char) for char in str_arg]

    print("".join(sortie))


# --------------------------------------------------
if __name__ == "__main__":
    main()
