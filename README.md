# Credit:
This project has been conducted by the contributors below. This project is a semester long project performed at CentraleSupélec in Spring 2022, under the directive of Micheal Kirkpatrick, Cristian Puentes et Trungdung Le, professor at CentraleSupélec. Our client were Implicity, a French Cardiology HealthTech compagny represented by David Perlmutter and Eliot Crespin.

This README.md have been created by Virgile Rapegno. This project is a group effort, see below the contributors. 

# Disclaimer:
This project have been conducted in France for French client and supervised by French professor. Also the Report is therefore written in French, and code details as well. 

# Project: ECG Generator
## Project Members:
- CUBAYNES Marie marie.cubaynes@student-cs.fr
- GERONY Guillaume guillaume.gerony@student-cs.fr
- HAKEM Hugo hugo.hakem@student-cs.fr
- JEAN-MACTOUX Selena selena.jean-mactoux@student-cs.fr
- RAPEGNO Virgile virgile.rapegno@student-cs.fr
- WU Sarah sarah.wu@student-cs.fr

## Project Description:
Develop a software for generating electrocardiograms (ECG, 1 lead) with various pathologies (asystole, bradycardia, tachycardia, flutter, atrial fibrillation, ventricular fibrillation), and incorporating parasites and noise, among other features.

The project team is expected to:

- Understand the different types of arrhythmias and their impact on ECG in order to model them.
- Research ECG databases (e.g., physionet, CU, AHA).
- Implement a graphical interface in Python to select arrhythmia types and generate ECG files with different sequences.

This software could be highly beneficial for:

- Testing or training machine learning algorithms for ECG analysis.
- Training medical students in ECG analysis. It can be validated by physicians to determine the realism of the generated sequences.

## Usage:
Two options are available:

- The graphical interface allows the observation of a single ECG at a time, configurable as desired. Simply launch the interface.py file to open it.
- The generator is also available in the terminal through the export.py file. Specify the chosen disease type, the number of ECGs to generate, and the destination for the files. More information is available with the -help option.

## Dependencies:
This project requires the installation of the following Python modules:

matplotlib
numpy
scipy
wfdb
Ensure their installation with a simple:
```
pip install requirements.txt
```
