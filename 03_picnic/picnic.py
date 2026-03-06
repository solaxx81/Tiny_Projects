#!/usr/bin/env python3
"""
Author : JYM <jymo81.dude451@slmail.me>
Date   : 2026-03-05
Purpose: Liste du picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Items for picnic", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("item", metavar="str", nargs="+", help="Item(s) to bring")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Exécution principale : c'est ici que cela se passe."""

    args = get_args()
    items = args.item
    sorted_ = args.sorted
    number = len(items)
    bringing = ""

    if sorted_:
        items.sort()

    if number == 1:
        bringing = items[0]
    elif number == 2:
        # si par exemple items=["a","b"] utiliser chaine=" , ".join(items) va créer une chaîne avec chaque élément
        # séparés par " , " un print(chaine) donnera : a , b
        bringing = " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        bringing = ", ".join(items)

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
