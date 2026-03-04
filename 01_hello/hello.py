#!/usr/bin/env python3
"""
Auteur: Jean-Yves
But: Dire bonjour (Projet 01 du livre)
"""

import argparse


def get_args():
    """Récupérer les arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(description="Dire bonjour")

    # On définit l'option -n (ou --name)
    parser.add_argument("-n", "--name", metavar="nom", default="World", help="Le nom à saluer")

    return parser.parse_args()


def main():
    """Le cœur du programme"""
    args = get_args()
    # On affiche exactement ce que le test attend : Hello, suivi du nom !
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
