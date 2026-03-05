
## Mise en place d'un nouvel exercice

#### En prenant par exemple le chapitre 2 : crowsnest

- Soit **copier le dossier** du livre vers son dossier de travail `02_crowsnest`,   
soit depuis le dossier du chapitre `02_crowsnest`, dans le terminal **entrer la commande** qui créera un template de fichier prêt à être utilisé par les tests. :
    ```Python
    new crowsnest.py
    ```

- **Rendre exécutable** le nouveau fichier :
`chmod +x crowsnest.py`

- **Renommer tout de suite** le fichier de test : `test.py` devient `test_crowsnest.py`. (Cela évite les conflits d'importation).

- **Appliquer la correction** au début du fichier de test pour que VS Code trouve le programme en **remplaçant** :

    ```Python
        prg = 'crowsnest.py'
    ```
    #### Par :

    ```Python
        import os
        prg = os.path.join(os.path.dirname(__file__), 'crowsnest.py')
    ```

- **Penser à corriger** le fichier "Makefile" avec le vrai nom du fichier de test.
