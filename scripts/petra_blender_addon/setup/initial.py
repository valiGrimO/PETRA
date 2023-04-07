import bpy
import addon_utils
import copy


print("[PETRA] Setup: Initial")

C = bpy.context
D = bpy.data


#######################################
# GEOMETRY NODES ON DOCUMENTED OBJECT #
#######################################

documentedObject = C.selected_objects[0]


# Add GeometryNodes modifier
bpy.ops.object.modifier_add(type='NODES')
bpy.ops.node.new_geometry_node_group_assign()

# Rename Node Group
gn = D.node_groups["Geometry Nodes"]
gn.name = "mergeByDistance"
    # pour la console:
    # gn = D.node_groups["mergeByDistance"]

# Configure group input
begin = gn.nodes["Group Input"]
begin.label = "input"
begin.name = "input"
begin.location = (0, 0)

# input resolution
resolution = gn.nodes.new("ShaderNodeValue")
resolution.label = "resolution"
resolution.name = "resolution"
resolution.location = (0, -140)
resolution.outputs[0].default_value = 0.01

# Add Math1
math1 = gn.nodes.new("ShaderNodeMath")
math1.name = "Math1"
math1.label = "Math1"
math1.location = (200, -60)
math1.operation = "MULTIPLY"
math1.inputs[1].default_value = 2
math1.mute = True

# Add Math2
math2 = gn.nodes.new("ShaderNodeMath")
math2.name = "Math2"
math2.label = "Math2"
math2.location = (400, -60)
math2.operation = "MULTIPLY"
math2.inputs[1].default_value = 3
math2.mute = True

# Add Merge by distance
merge = gn.nodes.new("GeometryNodeMergeByDistance")
merge.name = "Merge by Distance"
merge.label = "Merge by Distance"
merge.location = (600 ,60)

# Configure group output
out = gn.nodes["Group Output"]
out.name = "output"
out.label = "output"
out.location = (800, 60)

#LINKS
gn.links.new(begin.outputs[0], merge.inputs[0])
gn.links.new(resolution.outputs[0], math1.inputs[0])
gn.links.new(math1.outputs[0], math2.inputs[0])
gn.links.new(math2.outputs[0], merge.inputs[2])
gn.links.new(merge.outputs[0], out.inputs[0])

# Rename Begin outputs[1]
# gn.inputs[1].name = "Resolution"

# Don't use Merge By Distance
bpy.context.object.modifiers["GeometryNodes"].show_render = False

# Fake user
gn.use_fake_user = True


#####################
# RENDER PROPERTIES #
#####################

## Render transparent background
C.scene.render.film_transparent = True

## Color management
C.scene.view_settings.view_transform = 'Standard'


#####################
# CREATE COLLECTION #
#####################

Asset_collection = D.collections.new("PETRA")
C.scene.collection.children.link(Asset_collection)

C.view_layer.active_layer_collection = C.view_layer.layer_collection.children["PETRA"]


##########################################################################
# SET 3D CURSOR TO THE CENTER OF THE BOUNDING BOX OF THE SELECTED OBJECT #
##########################################################################

documentedObject = C.selected_objects[0]
locationCursor = D.scenes["Scene"].cursor.location
locationCursor[0] = documentedObject.location[0]
locationCursor[1] = documentedObject.location[1]
locationCursor[2] = documentedObject.location[2]
locationStart = copy.deepcopy(documentedObject.location)
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
locationBB = copy.deepcopy(documentedObject.location)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
D.scenes["Scene"].cursor.location = locationBB


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

bpy.ops.object.material_slot_add()

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
C.object.data.clip_start = 0.001

## Cam-02
bpy.ops.object.camera_add(location=(0.5, 0, 0), rotation=(1.5708, 0.00, 1.5708))
so = C.selected_objects[0]
so.name = "Cam-02"
C.object.data.clip_start = 0.001

## Cam-03
bpy.ops.object.camera_add(location=(0, 0.5, 0), rotation=(1.5708, 0.00, 3.14159))
so = C.selected_objects[0]
so.name = "Cam-03"
C.object.data.clip_start = 0.001

## Cam-04
bpy.ops.object.camera_add(location=(-0.5, 0, 0), rotation=(1.5708, 0, -1.5708))
so = C.selected_objects[0]
so.name = "Cam-04"
C.object.data.clip_start = 0.001

## Cam-05
bpy.ops.object.camera_add(location=(0, 0, 0.5), rotation=(0, 0, 0))
so = C.selected_objects[0]
so.name = "Cam-05"
C.object.data.clip_start = 0.001

## Cam-06
bpy.ops.object.camera_add(location=(0, 0, -0.5), rotation=(0, 3.14159, 3.14159))
so = C.selected_objects[0]
so.name = "Cam-06"
C.object.data.clip_start = 0.001

## Set Camera Ortho
for obj in D.collections['PETRA'].all_objects:
    if obj.type == "CAMERA":
        print(obj.data.type)
        obj.data.type = "ORTHO"

## Link orthographic scale to framing box dimensions:

    # review this part with Python Functions and Python Loops to make it more easy to read

### ------
### CAM-01
cam_01 = bpy.data.objects["Cam-01"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_01.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var1a = fcurve.driver.variables.new()
var1a.targets[0].id = framing_box
var1a.targets[0].data_path = "dimensions[0]"

var1b = fcurve.driver.variables.new()
var1b.targets[0].id = framing_box
var1b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-02
cam_02 = bpy.data.objects["Cam-02"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_02.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var2a = fcurve.driver.variables.new()
var2a.targets[0].id = framing_box
var2a.targets[0].data_path = "dimensions[1]"

var2b = fcurve.driver.variables.new()
var2b.targets[0].id = framing_box
var2b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-03
cam_03 = bpy.data.objects["Cam-03"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_03.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var3a = fcurve.driver.variables.new()
var3a.targets[0].id = framing_box
var3a.targets[0].data_path = "dimensions[0]"

var3b = fcurve.driver.variables.new()
var3b.targets[0].id = framing_box
var3b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-04
cam_04 = bpy.data.objects["Cam-04"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_04.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var4a = fcurve.driver.variables.new()
var4a.targets[0].id = framing_box
var4a.targets[0].data_path = "dimensions[1]"

var4b = fcurve.driver.variables.new()
var4b.targets[0].id = framing_box
var4b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-05
cam_05 = bpy.data.objects["Cam-05"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_05.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var5a = fcurve.driver.variables.new()
var5a.targets[0].id = framing_box
var5a.targets[0].data_path = "dimensions[0]"

var5b = fcurve.driver.variables.new()
var5b.targets[0].id = framing_box
var5b.targets[0].data_path = "dimensions[1]"

### ------
### CAM-06
cam_06 = bpy.data.objects["Cam-06"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_06.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var6a = fcurve.driver.variables.new()
var6a.targets[0].id = framing_box
var6a.targets[0].data_path = "dimensions[0]"

var6b = fcurve.driver.variables.new()
var6b.targets[0].id = framing_box
var6b.targets[0].data_path = "dimensions[1]"

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
D.scenes[0].frame_end = 6


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


####################################
# PRINT METADATA ON RENDERED IMAGE #
####################################

metadata = bpy.context.scene.render

metadata.use_stamp_date = False
metadata.use_stamp_time = False
metadata.use_stamp_render_time = False
metadata.use_stamp_frame = False
metadata.use_stamp_frame_range = False
metadata.use_stamp_memory = False
metadata.use_stamp_hostname = False
metadata.use_stamp_camera = False
metadata.use_stamp_lens = False
metadata.use_stamp_scene = False
metadata.use_stamp_marker = False
metadata.use_stamp_filename = False
metadata.use_stamp_sequencer_strip = False

metadata.use_stamp_note = True
metadata.use_stamp = True

for mod in addon_utils.modules():
    if mod.bl_info['name'] == 'PETRA':
        name = str(mod.bl_info.get('name'))
        version = str(mod.bl_info.get('version'))
        petraVersion = name + " " + version
        
D.scenes["Scene"].render.stamp_note_text = "Rendered with " + petraVersion
