# Guide d'installation et de consultation du cours MCP (en français)

Bienvenue ! Ce guide vous explique comment installer et consulter la formation sur le Model Context Protocol (MCP) en français.

## 1. Prérequis

- Python 3.8 ou supérieur
- `pip` (installé avec Python)
- (Optionnel) Un environnement virtuel Python (recommandé)

## 2. Installation des dépendances

Ouvrez un terminal dans le dossier du projet, puis exécutez :

```bash
pip install -r requirements.txt
```

## 3. Consulter la formation en français

- Le fichier `README_fr.md` contient la présentation du cours et les informations principales en français.
- Les unités de cours détaillées ne sont actuellement disponibles qu'en anglais (`units/en/`) et en vietnamien (`units/vi/`).

## 4. Générer les contenus de cours en français (optionnel)

Un script de traduction automatique est fourni pour générer les unités en français à partir des versions anglaises ou vietnamiennes.

### Utilisation du script de traduction

1. Placez-vous dans le dossier `scripts/` :
   ```bash
   cd scripts
   ```
2. Lancez le script de traduction français :
   ```bash
   python fr.py
   ```
   Ce script va traduire les contenus et générer les fichiers nécessaires (voir le script pour personnaliser la sortie).

> **Remarque** : Le script utilise des règles précises pour la traduction et nécessite que les fichiers sources soient présents dans `units/en/` ou `units/vi/`.

## 5. Questions ou contributions

Pour toute question ou suggestion, consultez le fichier `README_fr.md` ou ouvrez une issue sur le dépôt GitHub.

Bonne formation ! 