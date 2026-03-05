#!/usr/bin/env python3
"""
Author : JYM <jymo81.dude451@slmail.me>
Date   : 2026-03-05
Purpose: Crow's Nest 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article.", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # 1er 'word' : attribut récupéré par la fonction get_args()
    # 2eme 'word' : affiché dans l'aide pour dire "quoi saisir .. str, int, ou autre"
    # 3eme 'word' : texte d'aide décrivant ce que doit être le 2eme 'word'
    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    mot = args.word
    article = "a"
    if mot[0].lower() in "aeiou":
        article = "an"

    print(f"Ahoy, Captain, {article} {mot} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
