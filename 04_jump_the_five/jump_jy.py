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
    str_arg = args.text
    jumper = {"1": "9", "2": "8", "3": "7", "4": "6", "5": "0", "6": "4", "7": "3", "8": "2", "9": "1", "0": "5"}

    sortie: list[str] = []
    for char in str_arg:
        if char in jumper:
            sortie.append(jumper[char])
        else:
            sortie.append(char)
        """
        Tout ce bloc if peut être remplacé par la ligne ci-dessous.
                sortie.append(jumper.get(char, char))
        Extrait du livre p.87 :
        I can provide a second, optional argument to dict.get(), which is the default value
        to return when the key does not exist. In this program, I want to print the character
        itself when it does not exist in jumper. For instance, if I had “A,” I’d want to print “A”:
            >>> jumper.get('A', 'A')
            'A'
        But if I have “5,” I want to print “0”:
        >>> jumper.get('5', '5')
            '0'
        """

    print("".join(sortie))


# --------------------------------------------------
if __name__ == "__main__":
    main()
