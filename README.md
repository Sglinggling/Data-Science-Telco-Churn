# Projet de Prediction de Churn Client - Secteur Telecom

## Description du Projet
Ce projet a pour objectif d'analyser et de prédire le départ des clients (churn) pour une entreprise de télécommunications. La perte de clients étant un enjeu financier majeur, cette solution permet d'identifier les profils à risque afin de mettre en place des actions de rétention ciblées. 

Le travail couvre l'ensemble de la chaîne de valeur de la donnée : de l'analyse exploratoire à la mise en production via une API conteneurisée.

## Organisation des Fichiers
Le projet est structuré de manière à séparer la phase de recherche de la phase de production :

* **eda.ipynb** : Ce notebook contient l'analyse exploratoire des données, le nettoyage, le traitement des valeurs manquantes, la visualisation ainsi que l'entraînement du modèle supervisé et de la segmentation non supervisée.
* **models/model.pkl** : Ce fichier correspond à la pipeline complète (prétraitements et modèle Random Forest) sauvegardée après entraînement.
* **api/main.py** : Script principal utilisant le framework Flask pour exposer le modèle. Il permet de recevoir des données client et de renvoyer une prédiction en temps réel.
* **api/test_api.py** : Script utilitaire permettant de tester le bon fonctionnement de l'API en simulant l'envoi d'un profil client.
* **requirements.txt** : Liste exhaustive des bibliothèques Python nécessaires au fonctionnement du projet.
* **Dockerfile** : Fichier de configuration permettant de créer une image Docker pour isoler et déployer l'application.

## Installation et Utilisation

### Installation de l'environnement
Il est recommandé d'utiliser un environnement virtuel Python pour installer les dépendances. Une fois l'environnement activé, exécutez la commande suivante :

```bash
pip install -r requirements.txt
Lancement de l'API
Pour démarrer le serveur de prédiction, rendez-vous dans le répertoire du projet et lancez le script Flask :

Bash
python3 api/main.py
Le serveur sera accessible par défaut sur le port 5000.

Test de la solution
Une fois le serveur actif, vous pouvez vérifier les prédictions en exécutant le script de test :

Bash
python3 api/test_api.py
Utilisation avec Docker
Pour garantir la portabilité de l'application, une configuration Docker est fournie.

Construction de l'image :

Bash
docker build -t churn-api .
Lancement du conteneur :

Bash
docker run -p 5000:5000 churn-api
Methodologie et Choix Techniques
Analyse de données : Une attention particulière a été portée à la corrélation entre les charges mensuelles et la durée d'engagement.

Prétraitement : L'utilisation d'une Pipeline Scikit-Learn garantit que les transformations appliquées lors de l'entraînement sont rigoureusement identiques à celles appliquées lors de la prédiction en production.

Modélisation : Un algorithme de Random Forest a été choisi pour sa robustesse. En compléSment, un clustering K-Means a été effectué pour segmenter la base client en trois groupes distincts.

Interprétation : Les résultats permettent de distinguer les clients fidèles des profils volatiles, souvent caractérisés par des contrats mois par mois et des services additionnels non souscrits.