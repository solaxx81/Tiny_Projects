#!/usr/bin/env python3
"""
Author : JYM <jymo81.dude451@slmail.me>
Date   : 2026-03-08
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="*",
        help="Input file(s)",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Exécution principale : c'est ici que cela se passe."""

    args = get_args()




# --------------------------------------------------
if __name__ == "__main__":
    main()
