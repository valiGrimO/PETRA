import bpy
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

# Select render Engine
C.scene.render.engine = "CYCLES"

# Apply material to selected objects
material = D.materials["r4_pointiness"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Decimate Selected mesh
modifier = selected_object.modifiers.new(name="Decimate", type="DECIMATE")
modifier.ratio = 1.0  # value definied by users
ratio_as_percent = round(modifier.ratio * 100)

# Adjust Output filenames (end with -[ratio])
node_R4_Output = node_R4.node_tree.nodes["File Output"]
pattern = f"Cam-##_R4_POI-{ratio_as_percent}"
node_R4_Output.file_slots[0].path = pattern

# Create link
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[7])
