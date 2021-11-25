# **Notes**

## User interface
These scripts should appeared in the "Layer of Information Setup" as a list with a check button. This way, we can define the layer to produce according to what we are documenting.

## Previewing and Rendering
In order to preview a layer, when a button looking like a camera is clicked,
1. `initialisation.py` has to be executed first,
2. then anyone of the list beginning with `layer_...`.
are run.

In order to render a layer, when hitting the `produce documentation` button,
1. `initialisation.py`
2. `layer_...`
3. `render.py`
are run.

## Point of interest
### *R3. Deviation map*
Users can generate until 8 maps, automatically named `DM1`, `DM2`, etc.
The idea is to show a list of every vertex color index, So we can select which one should be rendered.


### *R4. Pointiness*
Note: `layer_R4_Pointiness-10pc` and `layer_R4_Pointiness-25pc`should not be previewable since it would be too much time consuming (because of a decimation modifier)
