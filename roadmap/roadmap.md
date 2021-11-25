# List of tasks for the development of **PETrA**

**Legend:**
- [ ] task to do
- [x] completed task
- :large_blue_circle: low priority
- :yellow_circle: medium priority
- :red_circle: high priority
- :green_circle: validated task

## Camera Management
- [ ] :yellow_circle: Add a check box to each camera in order to select the ones to be rendered (sometimes, we don't need every layer of information for some point of view)

## Layer of information in details
### C1, Color
- [ ] :large_blue_circle: Image decorrelation

### L1, Ambient occlusion
- [ ] :yellow_circle: Integrate control of ambient occlusion

### R2, contour lines
- [ ] :red_circle: integrate sublayers in user interface

### R3, Deviation map
- [ ] :red_circle: integrate sublayers in user interface
- [ ] :red_circle: if there is several `DM` vertex color, create a loop to render each one
- [ ] :yellow_circle: integrate the plugin "deviation map" to compute the distance between 2 meshes. It is already configured to meet the PETrA requirement. We need to show only "normalization value", and to compute the distance
- [ ] :large_blue_circle: **render script** when rendering, if R3 is selected, check if one `DM` vertex color at least is present on the selected mesh
- [ ] :large_blue_circle: how to find normalization value without CloudCompare?

**_Open questions_**
- user can produce several `DM` layer. How to document them? In a sense of which parameters were used to produce the comparison mesh, and for which purpose?

### R4, Pointiness
- [ ] :yellow_circle: Create a loop to apply decimate modifier to every selected meshes

## Scripts about previewing and rendering layers of information
- [ ] :red_circle: rendering an animation is not working, we need to hit the preview button to apply the render size
- **LAST MEETING** [`layer_render.py #L5`](https://github.com/valiGrimO/PETrA/blob/b1e7e841c446dcbdc4a2f887ffec58d6561a9e17/scripts/petra_blender_addon/render_layers/layer_render.py#L5) : `bpy.ops.petra.activate_and_preview_scene_camera()` doesn't seem to work

## User interface, general interactions
- [ ] **M+V** :large_blue_circle: add "help button" in the panel, in relation with each layer and/or parameter, linking to a specific page of the documentation for R3 at least, but probably each layer
- [ ] **V** :yellow_circle: rewrite the whole documentation, but in English this time
- [ ] **M** or **V** :yellow_circle: How to remove the `modelling` tab present by default in Blender? In this tab, we enter directly in edit mode, and since we are working with huge meshes, it is time consumming to wait until everything is loaded as we don't need to interact...

## Paradata
- **LAST MEETING** [`paradata.py #L116`](https://github.com/valiGrimO/PETrA/blob/b1e7e841c446dcbdc4a2f887ffec58d6561a9e17/scripts/petra_blender_addon/paradata.py#L116) : don't succeed to compute `imageResolution`
- **LAST MEETING** [`paradata.py #L123`](https://github.com/valiGrimO/PETrA/blob/b1e7e841c446dcbdc4a2f887ffec58d6561a9e17/scripts/petra_blender_addon/paradata.py#L123) : how could I get `orthographicScale` displayed in the user interface?
- **LAST MEETING** [`paradata.py #L124`](https://github.com/valiGrimO/PETrA/blob/b1e7e841c446dcbdc4a2f887ffec58d6561a9e17/scripts/petra_blender_addon/paradata.py#L124) : how could I get the `printedSize` (in cm) displayed in the user interface?
- **LAST MEETING** [`paradata.py #L`](https://github.com/valiGrimO/PETrA/blob/b1e7e841c446dcbdc4a2f887ffec58d6561a9e17/scripts/petra_blender_addon/paradata.py#L128) : how could I get `clippingStart`, `clippingEnd`, `shift_x` and `shift_y`?
- **LAST MEETING** [`paradata.py #L133`](https://github.com/valiGrimO/PETrA/blob/b1e7e841c446dcbdc4a2f887ffec58d6561a9e17/scripts/petra_blender_addon/paradata.py#L133) : getting absolute location and rotation of cameras is more efficient than the relative position to framing box. With absolute values, we don't need the framing box to get the same point of view. To get those values, we can use the 3D cursor:
- select the object we want to document
- move 3d cursor to the selection `bpy.ops.view3d.snap_cursor_to_selected()`
- get locations of 3d cursor `bpy.data.scenes["Scene"].cursor.location[0]`
- rotations are defined by the framing box rotation and local rotation of cameras

# Roadmap for the development of **ICEO**
- Coming after PETrA will be completed!
