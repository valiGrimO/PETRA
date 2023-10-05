# R3, Cartes des écarts

## Problème
La génération de cette couche d'information est longue et fastidieuse car il faut manipuler plusieurs logiciel pour arriver au résultat final:
+ Meshlab pour générer les maillages de comparaison
+ CloudCompare pour effectuer un premier calcul et déterminer les facteurs d'une distribution gaussienne (moyenne et écart-type)
+ LibreOffice Calc pour obtenir les valeurs min et max
+ Blender pour réaliser le calcul final avec tous les éléments préparés en amont.

L'objectif est de rassembler toutes ces étapes au sein de Blender, et de rendre les calculs les plus transparents possibles. Ce devrait être possible grâce au "Geometry Node".

Plusieurs étapes sont nécessaires:
1. Créer les maillages de comparaison
2. Calculer la distance entre deux maillages

## 1. Créer le maillage de comparaison



## 2. Calculer la distance entre deux maillages
