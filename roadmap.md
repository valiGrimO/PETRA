# Roadmap for the development of PETrA

**Legend:**
- [ ] :large_blue_circle: task to do, with low priority
- [ ] :yellow_circle: task to do, with medium priority
- [ ] :red_circle: task to do, with high priority
- [x] : completed task

## Developments about layers
### C1, color:
- [ ] :large_blue_circle: : Image decorrelation (see [DStrecth](http://www.dstretch.com/))
 
### R2, contour lines:
- [ ] :red_circle: **render script** : we have a weird effect if rotation is different of 0, and scale different of 1. We should warn the user to apply rotation and scale (`ctrl` + `A`) or propose to apply this operation.
- [ ] :red_circle: **render script** : how to affect the output name with the spacing value? The idea is to achieve an output file name like 'cam##_R2_CL-xmm'
- [ ] :yellow_circle: **user interaction** : integrate the control of spacing in the side bar
 
### R3, deviation map:
- [ ] :yellow_circle: **ex. plugin** : integrate the plugin "deviation map" to compute the distance between 2 meshes. It is already configured to meet the PETrA requirement. We don't need to show him, just compute the distance
- [ ] :red_circle: **ex. plugin** : in the DM plugin, how to name correctly output (for instance ,"DM2" instead of "DM.001")
- [ ] :red_circle: **material** : add control on median value in the material node
- [ ] :red_circle: **material** : add out of range value (blue colored vertices) in the mask layer
- [ ] :red_circle: **render script** : how to affect the output name with the extreme and median values? The idea is to achieve an output file name like 'cam##_R3_DM`a`-`b`-`c`-`d`mm' where `a` is the ID of the deviation map computation ; `b` is the minimum value ; `c` is the median value ; `d` is the maximum value.
- [ ] :large_blue_circle: **render script** when rendering, if R3 is selected, check if one `DM` vertex color at least is present on the selected mesh
- [ ] :large_blue_circle: **render script** if there is several `DM` vertex color, create a loop to render each one
- [ ] :large_blue_circle: **user interaction** : interact in the side panel with median and extreme values

**_Open questions:_**
- user can produce several `DM` layer. How to document them? In a sense of which parameter where used to produce the comparison mesh, and for which purpose?
 
### Others:
- [ ] :red_circle: **render script** finish to write action's scripts
  - [ ] how to remove a link?
  - [ ] how to apply (and not rename) a matrial to a selected object, and a specific object?
  - [ ] how to hit "produce documentation"?
  - [ ] how to mute and unmute a node?
- [ ] **generic question** about compositing nodes, is it really better to name them?
- [ ] rewrite the whole documentation, but in English this time


## User interface, general interactions:
- [ ] :yellow_circle: complete the integration of cameras manager
- [ ] :yellow_circle: load action's scripts and add a player to execute them (layer renderer), when every script will work fine
- [ ] :large_blue_circle: add "help button" in the panel, in relation with each layer and/or parameter, linking to a specific page of the documentation for R3 at least, but probably each layer
