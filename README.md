# Dashboard pour l'évaluation du niveau d'accompagnement des élèves

## Description du Projet

Ce projet consiste en la création d'un **dashboard** permettant d’évaluer le niveau de **complexité d'accompagnement** des élèves pour améliorer leur niveau scolaire en tenant compte de plusieurs variables, telles que l’âge, la situation des parents, les activités, les absences, la consommation d’alcool, la note finale et ainsi de suite.

## Démarche

1. **Analyse exploratoire des données**:
   - Compréhension de la composition du dataset ainsi que le type de variables et leurs distributions.

3. **Prétraitement des données** :
   - Encodage des variables catégorielles;
   - Standardisation des données numériques pour les rendre compatibles avec l'algorithme du clustering.

4. **Clustering des élèves** :
   - Application de l'algorithme **K-Prototypes** (adapté aux données mixtes) pour segmenter les élèves en groupes homogènes selon leurs caractéristiques;
  
5. **Définition du score d'accompagnement** :
   - Définition d'un niveau de suivi ou de soutien des élèves en fonction du cluster auquel ils appartiennent. Chaque cluster est associé à un score d'accompagnement, qui peut être  utilisé pour adapter les interventions pédagogiques.

6. **Visualisation des données** :
   - Un **dashboard interactif** permet de visualiser sur un graph la dispersion des élèves en fonction de leur **note finale** et **le score d’accompagnement**.

## Déploiement et maintenance
- Le code est structuré de manière modulaire, avec des classes distinctes pour chaque tâche (analyse exploratoire, prétraitement, clustering, définition du score, visualisation), ce qui facilite sa compréhension, sa maintenance et son amélioration dans le temps;
- Le fichier requirements.txt contient toutes les bibliothèques et dépendances nécessaires pour l'éxécution du projet, permettant à un nouveau développeur de prendre la main sur le code et d'éxécuter le programme sans bugs;

## Instruction pour l'exécution du code
- Cloner le projet en local à l'aide de la commande : git clone https://github.com/Ayoub219/Students_support.git
- Créer un environnement virtuel par la commande : python -m venv nom_environnement
- Activer l'environnement virtuel: venv\Scripts\activate
- Installer les librairies et les dépendances: pip install -r requirements.txt
- Exécuter le dashboard: streamlit run main.py
- Le code intègre aussi des tests unitaires qui garantissent son bon fonctionnement ainsi que sa fiabilité avant le déploiement.


---


