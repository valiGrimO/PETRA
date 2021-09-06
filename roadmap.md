# "Roadmap" for the development of PETrA

**Legend:**
- [ ] : task to do
- [x] : completed task </br>
:red_circle: : high priority </br>
:yellow_circle: : medium priority </br>
:large_blue_circle: : low priority


## Developments about layers
### C1, color:
- [ ] :large_blue_circle: : Image decorrelation (see [DStrecth](http://www.dstretch.com/))
 
### R2, contour lines:
**Render script**
- [ ] :red_circle: in the script, apply rotation and scale to get a good result (we have a weird effect when rotation is different of 0, and scale different of 1)

**Compositing**
- [ ] :red_circle: how to affect the output name with the spacing value? The idea is to achieve an output file name like 'cam##_R2_CL-xmm'

**User interaction**
- [ ] integrate the control of spacing in the side bar
 
### R3, deviation map:
**About the existing plugin**
- [ ] :yellow_circle: integrate the plugin "deviation map" to compute the distance between 2 meshes
- [ ] :red_circle: in the DM plugin, how to name correctly output (for instance ,"DM2" instead of "DM.001")

**Material**
- [ ] :red_circle: add control on median value in the material node
- [ ] :red_circle: add out of range value (blue colored vertices) in the mask layer

**Compositing**
- [ ] :red_circle: how to affect the output name with the extreme and median values? The idea is to achieve an output file name like 'cam##_R3_DM`a`-`b`-`c`-`d`mm' where `a` is the ID of the deviation map computation ; `b` is the minimum value ; `c` is the median value ; `d` is the maximum value.

**User interaction**
- [ ] :large_blue_circle: interact in the side panel with median and extreme values
 
### Others:
- [ ] finish to write action's scripts
- [ ] about nodes, is it really better to name them?
- [ ] when rendering, if R3 is selected, check if one DM vertex color at least is present on the selected mesh
- [ ] add "help button" in the panel, in relation with each layer and/or parameter, linking to a specific page of the documentation for R3 at least, but probably each layer
- [ ] rewrite the whole documentation, but in English this time


## User interface, general interactions:
- [ ] complete the integration of cameras manager
- [ ] load action's scripts and add a player to execute them (layer renderer)
- [ ] add controls over some rendering options (listed hereafter)
