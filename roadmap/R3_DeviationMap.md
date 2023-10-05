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
Il est possible de décimer et lisser un maillage très simplement avec Geometry node en suivant cette configuration:
![img](https://github.com/valiGrimO/PETRA/blob/b0ccffb5e3f556b3224f09c5ff249b9f4f196aef/roadmap/R3a_smoothMeshes.png)

Pour l'exécution du script, il faudra simplement veiller à :
+ dupliquer le maillage
+ créer le Geometry Node
+ trouver les bonnes valeurs
+ vérifier si le Geometry Node est effectif au moment du calcul de la distance entre deux maillages, afin de ne pas appliquer le modificateur.

## 2. Calculer la distance entre deux maillages
