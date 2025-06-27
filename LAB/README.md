# Lab: GitHub Actions et Variables d'Environnement

## Objectif
L'objectif de ce lab est de vous familiariser avec les étapes pour utiliser GitHub Actions, y compris :
1. Le clonage d'un dépôt GitHub.
2. La création et le basculement vers une nouvelle branche.
3. L'ajout et l'utilisation de variables d'environnement dans GitHub Actions.
4. L'exécution d'un script Python.
5. L'affichage du nom de la branche courante.
6. Le commit et le push des modifications.
7. La visualisation des résultats dans GitHub Actions.
8. Le déclenchement manuel d'un job.


## Étapes

### Étape 1 : Cloner le dépôt GitHub
La première étape consiste à cloner le dépôt GitHub sur votre machine locale. Utilisez la commande `git clone` suivie de l'URL du dépôt.

```sh
git clone https://github.com/techsysfr/github-actions-lab.git
```

### Étape 2 : Naviguer dans le dépôt
Une fois le dépôt cloné, naviguez dans le répertoire du dépôt :

```sh
cd votre-depot
```

### Étape 3 : Créer une nouvelle branche et basculer dessus
Créez une nouvelle branche nommée `[branch-name]` et basculez dessus en utilisant la commande `git checkout -b` :

```sh
git checkout -b [branch-name]
```

### Étape 4 : Ajouter une étape dans GitHub Actions pour les variables d'environnement
Modifiez le fichier `test-ci.yml` de workflow GitHub Actions dans le répertoire `.github/workflows` de votre dépôt.

```yaml
# Changez le nom de workflow
name: CI with Environment Variables

on:
  push:
    branches:
      - [branch-name] # Remplacez [branch-name] par le nom de votre branche
  workflow_dispatch:

# Ajoutez le variable global
env:
  GLOBAL_VAR: "This is a global variable"

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    
    # Affichez le variable global 
    - name: Print global variable
      run: echo "Global variable: $GLOBAL_VAR"

    # Ajoutez et affichez le variable local
    - name: Set and print local variable
      env:
        LOCAL_VAR: "This is a local variable"
      run: |
        echo "Local variable: $LOCAL_VAR"
    # Affichez le nom de branch
    - name: Print branch name
      run: |
        echo "Branch name: $GITHUB_REF_NAME"

    - name: Run Python script
      run: |
        python script.py
```

### Étape 5 : Ajouter les modifications
Ajoutez les modifications à l'index (staging area) en utilisant la commande `git add` :

```sh
git add .
```

### Étape 6 : Commiter les modifications
Commitez les modifications avec un message de commit descriptif :

```sh
git commit -m "Add GitHub Actions workflow with environment variables and Python script"
```

### Étape 7 : Pousser les modifications vers le dépôt distant
Poussez les modifications vers le dépôt distant sur la branche `[branch-name]` :

```sh
git push origin [branch-name]
```

### Étape 8 : Voir le résultat dans GitHub Actions
Allez dans l'onglet `Actions` de votre dépôt GitHub pour voir le résultat de l'exécution du workflow. Vous devriez voir un nouveau workflow nommé `CI with Environment Variables` qui a été déclenché par le push sur la branche `[branch-name]`.

### Étape 9 : Lancer le job manuellement
Pour lancer le job manuellement, allez dans l'onglet `Actions` de votre dépôt GitHub, sélectionnez le workflow `CI with Environment Variables`, et cliquez sur le bouton `Run workflow`. Vous pouvez choisir la branche `[branch-name]` et lancer le workflow.

## 👉 Allez plus loin : Utiliser les variables dans `script.py`

Créez un fichier `script.py` à la racine de votre dépôt contenant :

```python
import os

# Accès à la variable globale
global_var = os.environ.get("GLOBAL_VAR")

# Accès à la variable locale
local_var = os.environ.get("LOCAL_VAR")

# Affichage
print(f"Global variable from env: {global_var}")
print(f"Local variable from env: {local_var}")
```

Modifiez ensuite le fichier `test-ci.yml` et ajoutez une étape supplémentaire pour exécuter `script.py` :

```yaml
- name: Run Python script
  env:
    LOCAL_VAR: "This is a local variable"
  run: python script.py