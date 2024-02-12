# Projet : générateur d'ECG
## Membre du projet :
- CUBAYNES Marie marie.cubaynes@student-cs.fr
- GERONY Guillaume guillaume.gerony@student-cs.fr
- HAKEM Hugo hugo.hakem@student-cs.fr
- JEAN-MACTOUX Selena selena.jean-mactoux@student-cs.fr
- RAPEGNO Virgile virgile.rapegno@student-cs.fr
- WU Sarah sarah.wu@student-cs.fr

## Description du projet : 
Développer un logiciel générateurd’électrocardiogrammes(ECG, 1 voie) avec différentes pathologies (asystolie,  bradycardie,  tachycardie,  flutter,  fibrillation  atriale,  fibrillation  ventriculaire) et intégrant entre autres, des parasites et du bruit.

L’équipe projet devra :
- Comprendre les différents types d'arythmies et leur impact sur l'ECG afin de les modéliser,
- Rechercher les bases de données d'ECG (bases physionet, CU, AHA),
- Mettre en œuvre une interface graphique en Python permettant de choisir des types d'arythmie et générer de fichiers ECG avec séquences différentes.

Ce logiciel pourrait être très utile pour :
- Tester ou entraîner des algorithmes de machine learning d'analyse d'ECG.
- Former des étudiants en médicine à l’analyse d’ECG. Il pourra être validé par des médecins qui établiront si les séquences générées sont improbables ou réels. 

## Utilisation :
Deux possibilités sont disponibles :
- L'interface graphique permet d'observer un unique ECG à la fois que l'on peut configurer comme on le souhaite. Il suffit de lancer le fichier **interface.py** pour l'ouvrir.
- Le générateur est aussi disponible dans le terminal au travers du fichier **export.py**. Il convient de préciser le type de maladie choisie, le nombre d'ECG à générer et la destination des fichiers. Plus d'information sont disponibles avec l'option -help.

## Dépendences :
Ce projet requiert l'installation des modules pythons suivants :
- matplotlib
- numpy
- scipy
- wfdb
Il est simple de s'assurer de l'installation avec un simple
```
pip install requirements.txt
```