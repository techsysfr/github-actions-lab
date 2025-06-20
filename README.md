# Atelier GitHub Actions

---

# Introduction

## Qu'est-ce que GitHub Actions ?

- GitHub Actions est une plateforme de CI/CD intégrée à GitHub.
- Elle permet d'automatiser les workflows de développement directement depuis vos dépôts GitHub.
- Avec GitHub Actions, vous pouvez créer des workflows personnalisés pour construire, tester et déployer votre code.

---

## Pourquoi utiliser GitHub Actions ?

- **Intégration directe avec GitHub** : Facile à configurer et à gérer.
- **Automatisation** : Automatise les tâches répétitives comme les tests, les builds et les déploiements.
- **Collaboration** : Facilite la collaboration entre les membres de l'équipe.
- **Flexibilité** : Prend en charge une large gamme de langages de programmation et de frameworks.
- **Communauté et écosystème** : Bénéficiez d'une vaste bibliothèque d'actions préconstruites.

---

## Concepts de base

- **Workflows** : Processus automatisé déclenché par un événement spécifique.
- **Événements** : Déclencheurs qui lancent un workflow (ex: push, pull request).
- **Jobs** : Ensemble d'étapes exécutées sur la même machine virtuelle.
- **Steps** : Tâches individuelles dans un job (commandes shell, scripts, actions).
- **Actions** : Unités de code réutilisables pour vos workflows.

---

# Création d'un Workflow

## Exemple de Workflow

```yaml
name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run a one-line script
      run: echo Hello, world!
```

---

# Explication du Workflow

- `name`: Nom du workflow
- `on`: Événement qui déclenche le workflow
- `jobs`: Liste des jobs à exécuter
- `runs-on`: Type de machine virtuelle à utiliser
- `steps`: Liste des étapes à exécuter

---

# Exemple Pratique avec Python

## Exemple de Workflow pour un Projet Python

```yaml
name: Python CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m pytest
```

---

# Explication du Workflow Python

- `name: Python CI`: Donne un nom à votre workflow pour le rendre facilement identifiable.
- `on: [push]`: Spécifie que le workflow sera déclenché à chaque push sur le dépôt.
- `jobs`: Définit les jobs à exécuter. Ici, nous avons un seul job nommé `build`.
- `runs-on: ubuntu-latest`: Indique que le job sera exécuté sur la dernière version d'Ubuntu.
- `steps`: Liste des étapes à exécuter dans le job.
- `uses: actions/checkout@v2`: Utilise l'action `checkout` pour récupérer le code source du dépôt.
- `uses: actions/setup-python@v2`: Utilise l'action `setup-python` pour configurer l'environnement Python.
- `with: python-version: '3.9'`: Spécifie la version de Python à utiliser, ici Python 3.9.
- `run: python -m pip install --upgrade pip`: Met à jour pip, le gestionnaire de paquets Python.
- `run: pip install -r requirements.txt`: Installe les dépendances du projet listées dans le fichier `requirements.txt`.
- `run: python -m pytest`: Exécute les tests avec pytest, un framework de test pour Python.

---

# Exercice Pratique

1. Créez un nouveau dépôt GitHub.
2. Ajoutez un fichier `.github/workflows/python-ci.yml` avec le contenu suivant :

```yaml
name: Python CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m pytest
```

3. Créez un fichier `requirements.txt` et ajoutez vos dépendances.
4. Créez un fichier de test avec pytest.
5. Commitez et poussez les changements pour déclencher le workflow.

---
