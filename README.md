# Présentation sur GitHub Actions


# Introduction

- Qu'est-ce que GitHub Actions ?
- Pourquoi utiliser GitHub Actions ?
- Concepts de base : workflows, événements, jobs, steps, actions

---

# Qu'est-ce que GitHub Actions ?

- GitHub Actions est une plateforme de CI/CD intégrée à GitHub.
- Elle permet d'automatiser les workflows de développement directement depuis vos dépôts GitHub.
- Avec GitHub Actions, vous pouvez créer des workflows personnalisés pour construire, tester et déployer votre code.

---

# Pourquoi utiliser GitHub Actions ?

- **Intégration directe avec GitHub** : Facile à configurer et à gérer.
- **Automatisation** : Automatise les tâches répétitives comme les tests, les builds et les déploiements.
- **Collaboration** : Facilite la collaboration entre les membres de l'équipe.
- **Flexibilité** : Prend en charge une large gamme de langages de programmation et de frameworks.
- **Communauté et écosystème** : Bénéficiez d'une vaste bibliothèque d'actions préconstruites.

---

# Concepts de base

- **Workflows** : Processus automatisé déclenché par un événement spécifique.
- **Événements** : Déclencheurs qui lancent un workflow (ex: push, pull request).
- **Jobs** : Ensemble d'étapes exécutées sur la même machine virtuelle.
- **Steps** : Tâches individuelles dans un job (commandes shell, scripts, actions).
- **Actions** : Unités de code réutilisables pour vos workflows.

---

# Exemple de Workflow

## Workflow pour exécuter main.py

```yaml
name: Run main.py on push and manually

on:
  push: # Automatique sur chaque push
    branches:
      - main
  workflow_dispatch: # Manuel depuis l'onglet Actions

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run main.py
        run: python main.py
```

---

# Explication du Workflow

## Nom du Workflow

```yaml
name: Run main.py on push and manually
```

- `name` : Donne un nom à votre workflow pour le rendre facilement identifiable.

---

## Événements de Déclenchement

```yaml
on:
  push: # Automatique sur chaque push
    branches:
      - main
  workflow_dispatch: # Manuel depuis l'onglet Actions
```

- `on` : Spécifie les événements qui déclenchent le workflow.
  - `push` : Le workflow est déclenché automatiquement à chaque push sur la branche `main`.
  - `workflow_dispatch` : Permet de déclencher le workflow manuellement depuis l'onglet Actions de GitHub.

---

## Jobs

```yaml
jobs:
  run-script:
    runs-on: ubuntu-latest
```

- `jobs` : Définit les jobs à exécuter.
  - `run-script` : Nom du job.
  - `runs-on: ubuntu-latest` : Spécifie que le job sera exécuté sur la dernière version d'Ubuntu.

---

## Étapes (Steps)

### Checkout du Code

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4
```

- `uses: actions/checkout@v4` : Utilise l'action `checkout` pour récupérer le code source du dépôt.

---

### Configuration de Python

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.10'
```

- `uses: actions/setup-python@v5` : Utilise l'action `setup-python` pour configurer l'environnement Python.
- `with: python-version: '3.10'` : Spécifie la version de Python à utiliser, ici Python 3.10.

---

### Installation des Dépendances

```yaml
- name: Install dependencies
  run: pip install -r requirements.txt
```

- `run: pip install -r requirements.txt` : Installe les dépendances du projet listées dans le fichier `requirements.txt`.

---

### Exécution de main.py

```yaml
- name: Run main.py
  run: python main.py
```

- `run: python main.py` : Exécute le script `main.py`.

---

# Lab: GitHub Actions et Variables d'Environnement

## Objectif
L'objectif de ce lab est de vous familiariser avec les étapes pour utiliser GitHub Actions, y compris :

- Le clonage d'un dépôt GitHub.
- La création et le basculement vers une nouvelle branche.
- L'ajout et l'utilisation de variables d'environnement dans GitHub Actions.
- L'exécution d'un script Python.
- L'affichage du nom de la branche courante.
- Le commit et le push des modifications.
- La visualisation des résultats dans GitHub Actions.
- Le déclenchement manuel d'un job.
