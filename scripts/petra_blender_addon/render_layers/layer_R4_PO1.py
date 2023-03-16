import bpy
from petra_blender_addon import popup
from petra_blender_addon.blendertools import remove_link


# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = S.node_tree

node_RL = nodetree.nodes["Render Layers"]
node_PETrA = nodetree.nodes["PETrA"]
node_PETrA_Input = node_PETrA.node_tree.nodes["Group Input"]
node_R4 = node_PETrA.node_tree.nodes["R4_pointiness"]
gn = D.node_groups["mergeByDistance"] # this is Geometry Nodes

# Select render Engine
C.scene.render.engine = "CYCLES"

# Apply material to selected objects
material = D.materials["R4_POI"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')

# Render GeoNode modifyer
selected_object.modifiers["GeometryNodes"].show_render = True

# Apply modifier to every selected object
bpy.ops.object.make_links_data(type='MODIFIERS')

# Set Mesh Resolution  = 1
math1 = gn.nodes["Math1"]
math1.mute = True

math2 = gn.nodes["Math2"]
math2.mute = True

# Adjust Output filenames (end with -[ratio])
node_R4_Output = node_R4.node_tree.nodes["File Output"]
resolution = selected_object.modifiers["GeometryNodes"]["Input_2"]
resolution_mm = round(resolution*1000, 6)
pattern = f"Cam-##_R4_POI-{resolution_mm}mm"
node_R4_Output.file_slots[0].path = pattern

# Create link
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[7])
