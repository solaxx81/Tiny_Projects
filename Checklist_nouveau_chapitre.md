
## Quand tu commences un exercice (par exemple le chapitre 2) :

1. **Copie le dossier** du livre vers ton dossier de travail.

2. **Renomme tout de suite** le fichier de test : `test.py` devient `test_crowsnest.py`. (Cela évite les conflits d'importation que nous avons vus dans les logs).

3. **Applique la correction** au début du fichier de test pour que VS Code trouve le programme :

#### Remplace :

```    Python
    prg = 'crowsnest.py'
```
#### Par :

```    Python
    import os
    prg = os.path.join(os.path.dirname(__file__), 'crowsnest.py')
```

