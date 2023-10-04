# C1, Décorrélation d'image

## Informations sur la décorrélation d'image
- [Image Decorrelation with DStrecth, for archaeologists](http://www.dstretch.com/)
- [Image Decorrelation with Python](https://github.com/Dan-in-CA/decorrstretch)
- [Image Decorrelation explanations](https://dhanushkadangampola.blogspot.com/2015/02/decorrelation-stretching.html)

## Paramètres par défaut dans DStretch
|  | L | A | B |
|---|---|---|---|
| `LAB`	| 0,5 | 1,0	| 1,0 |
| `LDS`	| 0,5	| 0,9	| 0,5 |
| `LBK`	| 0,5	| 1,1	| 0,6 |
| `LBL`	| 0,5	| 1,2	| 1,0 |
| `LWE`	| 0,5	| 1,0	| 1,4 |
| `LYE`	| 2,0	| 1,0	| 2,0 |
| `LRD`	| 0,5	| 0,8	| 1,2 |
| `LRE`	| 0,5	| 0,5	| 1,0 |

|  | Y | U | V |
|---|---|---|---|
| `YUV` | 0,7	| 1,0	| 1,0 |
| `YDS` | 1,0	| 0,5	| 1,0 |
| `YBK` | 1,5	| 0,2	| 1,6 |
| `YDT` | 1,75 | 0,6 | 1,0 |
| `YBG` | 2,0 | 1,0 | 1,7 |
| `YBL` | 1,5 | 0,4 | 2,0 |
| `YWE` | 1,5 | 1,6 | 0,2 |
| `YYE` | 2,0 | 2,0 | 1,0 |
| `YRD` | 2,0 | 1,0 | 0,4 |
| `YRE` | 8,0 | 1,0 | 0,4 |
| `YBR` | 1,0 | 0,8 | 0,4 |

**Note:** Il n'y a pas d'information pour produire l'image `CRGB`.

## Pistes de réflexion pour intégrer la décorrélation d'image dans PETRA (Blender)
*En se basant sur [Image Decorrelation with Python](https://github.com/Dan-in-CA/decorrstretch)*

### Les bibliothèques
Deux bibliothèques sont nécessaires: PIL (pillow) et NumPy

**NumPy**
Cette bibliothèque est installée par défaut. Il suffit simplement de l'appeler
```
import numpy
```

**PIL**
Cette bibliothèque n'est pas installée dans l'environnement Python de Blender. Mais il ne faut l'installer qu'une seule fois, au risque de mettre la pagaille dans l'installation de Blender...
Pour l'installer:
```
import sys
!{sys.exec_prefix}/bin/python -m pip install pillow numpy
```
Il faudra donc vérifier l'installation de Pillow avant d'exécuter cette ligne.

