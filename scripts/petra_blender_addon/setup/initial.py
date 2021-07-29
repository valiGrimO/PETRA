import bpy


print("[PETRA] Setup: Initial")

C = bpy.context
D = bpy.data

#####################
# RENDER PROPERTIES #
#####################

## Render transparent background
C.scene.render.film_transparent = True

#####################
# CREATE COLLECTION #
#####################

Asset_collection = D.collections.new("PETRA")
C.scene.collection.children.link(Asset_collection)

C.view_layer.active_layer_collection = C.view_layer.layer_collection.children["PETRA"]

###############
# FRAMING BOX #
###############

## Create a Cube
bpy.ops.mesh.primitive_cube_add(
    enter_editmode=False, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
)
so = C.selected_objects[0]
so.name = "Framing Box"

## Skin modifyer
bpy.ops.object.modifier_add(type="SKIN")

## Skin resize
bpy.ops.object.editmode_toggle()
bpy.ops.transform.skin_resize(value=(0.1, 0.1, 0.1))
bpy.ops.object.editmode_toggle()

## Apply modifyer
bpy.ops.object.modifier_apply(modifier="Skin", report=True)

## Scale the box
C.object.scale = 0.487805, 0.487805, 0.487805
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

####################
# Reference Sphere #
####################

bpy.ops.mesh.primitive_ico_sphere_add(
    radius=0.05, location=(0.4, 0.4, 0.4), scale=(1, 1, 1)
)
so = C.selected_objects[0]
so.name = "Reference Sphere"

bpy.ops.object.modifier_add(type="SUBSURF")
C.object.modifiers["Subdivision"].levels = 2
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_apply(modifier="Subdivision", report=True)

###########
# Cameras #
###########

## Cam-01
bpy.ops.object.camera_add(location=(0, -0.5, 0), rotation=(1.5708, 0, 0))
so = C.selected_objects[0]
so.name = "Cam-01"

## Cam-02
bpy.ops.object.camera_add(location=(0.5, 0, 0), rotation=(1.5708, 0.00, 1.5708))
so = C.selected_objects[0]
so.name = "Cam-02"
C.object.hide_set(True)

## Cam-03
bpy.ops.object.camera_add(location=(0, 0.5, 0), rotation=(1.5708, 0.00, 3.14159))
so = C.selected_objects[0]
so.name = "Cam-03"
C.object.hide_set(True)

## Cam-04
bpy.ops.object.camera_add(location=(-0.5, 0, 0), rotation=(1.5708, 0, -1.5708))
so = C.selected_objects[0]
so.name = "Cam-04"
C.object.hide_set(True)

## Cam-05
bpy.ops.object.camera_add(location=(0, 0, 0.5), rotation=(0, 0, 0))
so = C.selected_objects[0]
so.name = "Cam-05"
C.object.hide_set(True)

## Cam-06
bpy.ops.object.camera_add(location=(0, 0, -0.5), rotation=(0, 3.14159, 3.14159))
so = C.selected_objects[0]
so.name = "Cam-06"
C.object.hide_set(True)

## Set Camera Ortho
for obj in C.scene.objects: # how to apply only on cameras in the `PETRA collection`?
    if obj.type == "CAMERA":
        print(obj.data.type)
        obj.data.type = "ORTHO"



## Define orthographic scale:
### create new drivers
camera = bpy.data.objects["Cam-01"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = camera.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var1 = fcurve.driver.variables.new()
var1.targets[0].id = framing_box
var1.targets[0].data_path = "dimensions[0]"

var2 = fcurve.driver.variables.new()
var2.targets[0].id = framing_box
var2.targets[0].data_path = "dimensions[2]"

### inspect created drivers
camera = bpy.data.objects["Cam-01"].data
drivers = camera.animation_data.drivers

drivers[0].data_path
'ortho_scale'
drivers[0].driver.type
'MAX'

drivers[0].driver.variables[0].targets[0].id
bpy.data.objects['Framing Box']
drivers[0].driver.variables[0].targets[0].data_type
'dimensions[0]'

drivers[0].driver.variables[1].targets[0].id
bpy.data.objects['Framing Box']
drivers[0].driver.variables[1].targets[0].data_path
'dimensions[2]'


### Cam-01
    # Choose the highest value between
        # bpy.data.objects["Framing Box"].scale[0]
        # bpy.data.objects["Framing Box"].scale[2]
    # Copy this value as a new driver
        # bpy.ops.ui.copy_as_driver_button()

    # Set this value as the orthographic scale of the camera
        # bpy.ops.anim.paste_driver_button()

### Cam-02
    # Choose the highest value between
        # bpy.data.objects["Framing Box"].scale[1]
        # bpy.data.objects["Framing Box"].scale[2]
    # Copy this value as a new driver
        # bpy.ops.ui.copy_as_driver_button()

    # Set this value as the orthographic scale of the camera
        # bpy.ops.anim.paste_driver_button()


### Cam-03
    # Choose the highest value between
        # bpy.data.objects["Framing Box"].scale[0]
        # bpy.data.objects["Framing Box"].scale[2]
    # Copy this value as a new driver
        # bpy.ops.ui.copy_as_driver_button()

    # Set this value as the orthographic scale of the camera
        # bpy.ops.anim.paste_driver_button()


### Cam-04
    # Choose the highest value between
        # bpy.data.objects["Framing Box"].scale[1]
        # bpy.data.objects["Framing Box"].scale[2]
    # Copy this value as a new driver
        # bpy.ops.ui.copy_as_driver_button()

    # Set this value as the orthographic scale of the camera
        # bpy.ops.anim.paste_driver_button()


### Cam-05
    # Choose the highest value between
        # bpy.data.objects["Framing Box"].scale[0]
        # bpy.data.objects["Framing Box"].scale[1]
    # Copy this value as a new driver
        # bpy.ops.ui.copy_as_driver_button()

    # Set this value as the orthographic scale of the camera
        # bpy.ops.anim.paste_driver_button()


### Cam-06
    # Choose the highest value between
        # bpy.data.objects["Framing Box"].scale[0]
        # bpy.data.objects["Framing Box"].scale[1]
    # Copy this value as a new driver
        # bpy.ops.ui.copy_as_driver_button()

    # Set this value as the orthographic scale of the camera
        # bpy.ops.anim.paste_driver_button()

## Parenting Cameras to 'Framing Box'
a = D.objects["Framing Box"]
b = D.objects["Cam-01"]
c = D.objects["Cam-02"]
d = D.objects["Cam-03"]
e = D.objects["Cam-04"]
f = D.objects["Cam-05"]
g = D.objects["Cam-06"]
h = D.objects["Reference Sphere"]

b.parent = a
c.parent = a
d.parent = a
e.parent = a
f.parent = a
g.parent = a
h.parent = a

## Cameras Binding
scene = C.scene
markers = {
    "F_01": {"frame": 1, "camera": "Cam-01", "frame_time": 1},
    "F_02": {"frame": 2, "camera": "Cam-02", "frame_time": 2},
    "F_03": {"frame": 3, "camera": "Cam-03", "frame_time": 3},
    "F_04": {"frame": 4, "camera": "Cam-04", "frame_time": 4},
    "F_05": {"frame": 5, "camera": "Cam-05", "frame_time": 5},
    "F_06": {"frame": 6, "camera": "Cam-06", "frame_time": 6},
}
for name, m_data in markers.items():
    # add a marker
    marker = scene.timeline_markers.new(name, frame=m_data["frame"])
    marker.camera = scene.objects.get(m_data["camera"])

## Set the length of the timeline
D.scenes[0].frame_start = 1
D.scenes[0].frame_end = 7

####################
# MOVE TO 3DCURSOR #
####################


def snap_active_to_cursor(obj: bpy.types.Object, copy_rotation=False):
    cursor = C.scene.cursor
    active_object = D.objects["Framing Box"]
    active_object.location = cursor.location

    if copy_rotation:
        active_object.rotation_euler = cursor.rotation_euler


obj = C.scene.objects["Framing Box"]
snap_active_to_cursor(obj)

####################################
# MAKE SOME OBJECTS NOT RENDERABLE #
####################################

## Deselect all objects
bpy.ops.object.select_all(action="DESELECT")

## Select some objects
for o in D.objects:
    # Check for given object names
    if o.name in ("Framing Box", "Reference Sphere"):
        o.select_set(True)

## Make those objects not renderable
selection = C.selected_objects

for obj in selection:
    obj.hide_render = not obj.hide_render

## Deselect all objects
bpy.ops.object.select_all(action="DESELECT")

## Select Framing Box (to ease resizing)
D.objects["Framing Box"].select_set(True)
