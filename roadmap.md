# "Roadmap" for the development of PETrA

**Legend:**
- [ ] : task to do
- [x] : completed task
- :red_circle: : high priority
- :orange_circle: : medium priority
- :blue_circle: : low priority


## Developments about layers
### C1, color:
+ [ ] :blue_circle: : Image decorrelation (see [DStrecth](http://www.dstretch.com/))
 
R2, contour lines:
+ integrate the control of spacing in the side bar
+ in the script, apply rotation and scale to get a good result (we have a weird effect when rotation is different of 0, and scale different of 1)
+ how to affect the output name with the spacing value? The idea is to achieve an output file name like 'cam##_R2_CL-xmm'
 
R3, deviation map:
+ integrate the plugin "deviation map" to compute the distance between 2 meshes
+ add control on median value
+ add out of range value (blue colored vertices) in the mask layer
+ interact in the side panel with median and extreme values
+ find a way to create them in a more general way ( not necessary DM1 and DM2)...
    + in the DM plugin, how to name correctly output (for instance ,"DM2" instead of "DM.001")
+ how to affect the output name with the extreme and medlayeralues? The idea is to achieve an output file name like 'cam##_R3_DMx-x-x-xmm'
 
Others:
+ finish to write action's scripts
+ about nodes, is it really better to name them?
+ when rendering, if R3 is selected, check if one DM vertex color at least is present on the selected mesh
+ add "help button" in the panel, in relation with each layer and/or parameter, linking to a specific page of the documentation for R3 at least, but probably each layer
+ rewrite the whole documentation, but in English this time


## User interface, general interactions:
- [ ] complete the integration of cameras manager
- [ ] load action's scripts and add a player to execute them (layer renderer)
- [ ] add controls over some rendering options (listed hereafter)
