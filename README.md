# Projet de Prediction de Churn Client - Secteur Telecom

## Description du Projet
Ce projet vise à prédire le départ des clients (churn) pour une entreprise de télécommunications. L'objectif est d'identifier les profils à risque pour permettre la mise en place de stratégies de rétention adaptées. 

Le projet couvre l'ensemble du cycle de vie des données, incluant l'analyse exploratoire, le prétraitement via une pipeline Scikit-Learn, et la mise à disposition du modèle via une API Flask conteneurisée avec Docker.

## Organisation des Fichiers
Le projet est organisé de la manière suivante :

* **churn_analysis.ipynb** : Analyse exploratoire (EDA), nettoyage des données, entraînement du modèle supervisé et segmentation par clustering.
* **models/model.pkl** : Pipeline de production sauvegardée (incluant les transformations et le modèle).
* **api/main.py** : Script de l'API Flask pour servir les prédictions.
* **api/test_api.py** : Script de test permettant de valider le fonctionnement de l'API.
* **requirements.txt** : Liste des dépendances Python.
* **Dockerfile** : Configuration pour la création de l'image Docker.

## Installation et Utilisation

### Installation classique
1. Installer les dépendances :
```bash
pip install -r requirements.txt

Lancer l'API :

Bash
./.venv/bin/python api/main.py
Tester l'API (dans un autre terminal) :

Bash
./.venv/bin/python api/test_api.py
Utilisation avec Docker
Docker permet d'éviter les problèmes de versions de bibliothèques entre les machines.

Construire l'image :

Bash
docker build -t churn-api .
Lancer le conteneur :

Bash
docker run -p 5000:5000 churn-api