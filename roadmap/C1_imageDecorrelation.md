# C1, Décorrélation d'image

## Informations sur la décorrélation d'image
- [Image Decorrelation with DStrecth, for archaeologists](http://www.dstretch.com/) - Outil obsolète depuis qu'ImageJ n'est plus maintenu.
- [Image Decorrelation with ERA, for archaeologists](https://gitlab.huma-num.fr/fmonna/era-extraction-from-rock-art) - Outil évoluant dans un environnement logiciel à jour. Très simple d'utilisation et plus rapide que DStretch. Ne fonctionne que sous Windows. Pour le télécharger, aller dans la [branche Windows du Git](https://gitlab.huma-num.fr/fmonna/era-extraction-from-rock-art/-/tree/Windows_EXE?ref_type=heads)
- [Image Decorrelation with Python](https://github.com/Dan-in-CA/decorrstretch)
- [Image Decorrelation explanations](https://dhanushkadangampola.blogspot.com/2015/02/decorrelation-stretching.html)

L'idéal serait d'intégrer la décorrelation d'image directement au sein de l'interface du plugin PETRA, dans Blender.

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

### Les variables
Dans l'état actuel du code, il existe trois variables:
+ infile = input("Enter file to process: ")
+ outfile = input("Enter output file: ")
+ tol_val = input("Enter tol value (optional): ")

`tol_val` est utilisé pour permettre à l'utilisateur de spécifier une tolérance pour l'étirement de contraste linéaire lors du traitement de l'image. Si l'utilisateur ne spécifie pas de tolérance, le code gère cela en utilisant "tol" comme None. Avec ce seul paramètre, il n'est pas possible de mobiliser plusieurs espaces de couleur à la manière de DStretch.

### Vers DStretch
Le code actuel implémente une technique de correction de contraste appelée "decorrelation stretch" (étirement de décorrélation) qui peut être utilisée pour améliorer la visualisation des images en modifiant l'espace de couleur de l'image. Cette technique est similaire à certaines des fonctionnalités de DStretch.

DStretch, quantà lui, est un logiciel spécifique qui offre une interface utilisateur dédiée et une variété d'options pour effectuer des étirements de couleur et des corrections d'image spécifiques pour les besoins de la visualisation des pétroglyphes (principalement).

Pour effectuer des étirements de couleur dans plusieurs espaces de couleur, il faudra implémenter des techniques spécifiques à l'espace de couleur souhaité, car l'étirement de décorrélation du code actuel est basé sur l'espace de couleur RGB. DStretch, quant à lui, utilise souvent des transformations d'espaces de couleur spécifiques pour obtenir des résultats optimisés pour la visualisation des pétroglyphes. 

### Travaillers dans plusieurs espaces de couleurs
**Les espaces de couleur**
D'abord, il faut choisir l'[espace de couleur](https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Espace_couleur). DStretch semble fonctionner avec:
+ LAB
+ YUV
+ RGB

Ensuite, il faut **modifiez la fonction `decorrstretch`:** Modifiez la fonction `decorrstretch` pour prendre en compte l'espace de couleur choisi. Par exemple, pour prendre en charge l'espace de couleur HSV, il faudra convertir l'image d'entrée en HSV avant de commencer les calculs et convertir le résultat final en retour dans l'espace de couleur d'origine.

Voici un exemple de modification pour prendre en charge l'espace de couleur HSV :

```
import cv2  # Pour la conversion en espace de couleur HSV

def decorrstretch(A, tol=None):
    # Convertir l'image en espace de couleur HSV
    A_hsv = cv2.cvtColor(A, cv2.COLOR_RGB2HSV)

    # Le reste du code reste inchangé, en utilisant A_hsv au lieu de A

    # Convertir le résultat en espace de couleur RGB
    B_rgb = cv2.cvtColor(B_hsv, cv2.COLOR_HSV2RGB)
    
    return B_rgb

```

**IMPORTANT:** à l'instar de la bibliothèque Pillow, OpenCV n'est pas présent dans l'envrironnement Python installé par défaut dans Blender. Il faudra donc l'installer.

**Utilisation de la fonction decorrstretch** 
Dans le script Blender, il est possible d'utiliser la fonction `decorrstretch` adaptée en fonction de l'espace de couleur choisi. Par exemple, pour l'espace de couleur HSV, il faudra s'assurer que les images sont chargées et sauvegardées dans cet espace de couleur.
```
# Charger l'image en espace de couleur HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Traiter l'image dans l'espace de couleur HSV
processed_hsv = decorrstretch(img_hsv, tol)

# Convertir le résultat en espace de couleur RGB
processed_rgb = cv2.cvtColor(processed_hsv, cv2.COLOR_HSV2RGB)

# Enregistrez l'image traitée en RGB
Image.fromarray(processed_rgb).save(outfile)

```

En adaptant le code de cette manière, il sera possible d'effectuer des étirements de couleur dans différents espaces de couleur dans Blender. Il faudra seulement choisir l'espace de couleur approprié en fonction des besoins et de bien comprendre comment effectuer les conversions nécessaires entre les espaces de couleur pour obtenir les résultats souhaités.

**Décliner à la manière de DStretch**
Pour prendre en charge une pondération différente des canaux de l'espace de couleur dans le style de DStretch, où vous pouvez pondérer différemment les composantes Y, U et V de l'espace de couleur YUV. Pour ce faire, vous pouvez ajouter des paramètres de pondération à votre fonction `decorrstretch`. Voici comment faire :
```
import numpy as np
from functools import reduce

def decorrstretch(A, tol=None, weights=(1.0, 1.0, 1.0)):
    """
    Apply decorrelation stretch to image with channel weights.

    Arguments:
    A       -- original image as numpy.array.
    tol     -- specify a linear contrast stretch, e.g., 0.01.
    weights -- weights for the Y, U, and V channels (default: [1.0, 1.0, 1.0]).
    """

    # Save the original shape
    orig_shape = A.shape

    # Reshape the image
    A = A.reshape((-1, 3)).astype(np.float)

    # Apply channel weights
    A[:, 0] *= weights[0]  # Y channel
    A[:, 1] *= weights[1]  # U channel
    A[:, 2] *= weights[2]  # V channel

    # The rest of your code remains the same...

    # Return it as a uint8 (byte) image
    return B.astype(np.uint8)
```

Dans cette version modifiée de decorrstretch, un paramètre weights a été ajouté afin de permettre de spécifier les pondérations des canaux Y, U et V. Par défaut, les pondérations sont égales pour tous les canaux (1.0, 1.0, 1.0), mais vous pouvez les personnaliser en passant un tuple de pondérations.

Lorsque la fonction `decorrstretch` est appelée, il est maintenant possible de spécifier les pondérations souhaitées, par exemple :
```
# Appliquer decorrstretch avec des pondérations personnalisées (par exemple, 1.0, 0.5, 0.5)
processed = decorrstretch(A, tol, weights=(1.0, 0.5, 0.5))
```

De cette manière, il est possible de pondérer différemment les canaux de l'espace de couleur YUV, ce qui est similaire à ce que fait DStretch avec son interface utilisateur pour créer les couches `YUV`, `YDS`, `YBK`, `YDT`, `YBG`, `YBL`, `YWE`, `YYE`, `YRD`, `YRE` et `YBR` (Cf. le tableau en haut de page).

## Synthèse
Voici un code synthétisé qui inclut les modifications nécessaires pour permettre une pondération différente des canaux 
+ de l'espace de couleur LAB pour générer une image LWE.
+ de l'espace de couleur YUV pour générer une image YBK.
Il suffit d'adapter le code pour intégrer toutes les déclinaisons possibles (Cf. le tableau au début du document)

```
import numpy as np
from functools import reduce
from PIL import Image
import cv2  # Pour les conversions d'espaces de couleur

def decorrstretch(A, tol=None, color_space='RGB', weights=(1.0, 1.0, 1.0)):
    """
    Apply decorrelation stretch to an image with channel weights.

    Arguments:
    A           -- original image as numpy.array.
    tol         -- specify a linear contrast stretch, e.g., 0.01.
    color_space -- color space to use (default: 'RGB', other options: 'YUV', 'LAB').
    weights     -- weights for the channels (default: [1.0, 1.0, 1.0]).

    Returns:
    B           -- decorrelated and stretched image.
    """

    # Save the original shape
    orig_shape = A.shape

    # Convert the image to the specified color space
    if color_space == 'RGB':
        # Already in RGB
        A_color = A
    elif color_space == 'YUV':
        A_color = cv2.cvtColor(A, cv2.COLOR_RGB2YUV)
    elif color_space == 'LAB':
        A_color = cv2.cvtColor(A, cv2.COLOR_RGB2LAB)
    else:
        raise ValueError("Unsupported color space")

    # Reshape the image
    A = A_color.reshape((-1, 3)).astype(np.float)

    # Apply channel weights
    A[:, 0] *= weights[0]  # Channel 0 (Y or L)
    A[:, 1] *= weights[1]  # Channel 1 (U or A)
    A[:, 2] *= weights[2]  # Channel 2 (V or B)

    # The rest of your code for decorrelation stretch...

    # Convert the result back to RGB color space
    if color_space == 'RGB':
        B_color = A.reshape(orig_shape).astype(np.uint8)
    elif color_space == 'YUV':
        B_yuv = A.reshape(orig_shape).astype(np.uint8)
        B_color = cv2.cvtColor(B_yuv, cv2.COLOR_YUV2RGB)
    elif color_space == 'LAB':
        B_lab = A.reshape(orig_shape).astype(np.uint8)
        B_color = cv2.cvtColor(B_lab, cv2.COLOR_LAB2RGB)

    return B_color

def process_and_save_image(infile, outfile, color_space, tol, channel_weights):
    # Load input file using PIL
    img = Image.open(infile)

    # Convert image to numpy array
    A = np.array(img)

    # Process image with decorrelation stretch in the specified color space and channel weights
    processed = decorrstretch(A, tol, color_space, channel_weights)

    # Save processed image to output file
    Image.fromarray(processed).save(outfile)

# Get user input for file paths, color space, and channel weights
infile = input("Enter file to process: ")

# Process and save LWE image (L=0.5, A=1.0, B=1.4) in LAB color space
process_and_save_image(infile, "LWE_output.png", 'LAB', 1.0, (0.5, 1.0, 1.4))

# Process and save YBK image (Y=1.5, U=0.2, V=1.6) in YUV color space
process_and_save_image(infile, "YBK_output.png", 'YUV', 1.0, (1.5, 0.2, 1.6))

print("Done")

```
**Note:** *la réflexion et le code a été généré à partir du dépôt [Image Decorrelation with Python](https://github.com/Dan-in-CA/decorrstretch) et de ChatGPT.*
