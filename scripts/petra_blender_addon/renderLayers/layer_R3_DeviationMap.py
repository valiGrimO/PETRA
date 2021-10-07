import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = S.node_tree.nodes["Render Layers"]
node_PETrA = S.node_tree.nodes["PETrA"]
node_R3 = node_PETrA.node_tree.nodes["R3_deviationMap"]

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material to selected objects
material = D.materials["r3_deviation_map"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[6])

# Adjust Output filenames (end with -[normValue])
node_R3_Output = node_R3.node_tree.nodes["File Output"]
pattern = f"Cam-##_R3_{R3_normValue}"
node_R3_Output.file_slots[0].path = pattern

# Change vertex color in the material
D.materials["r3_deviation_map"].node_tree.nodes["Vertex Color"].layer_name = "DM1"

# Note: Since several Vertex Color Indexes beginning with `DM` might exist (max = 7), then a loop have to render everyone, and the output name should be incremented (`DM1`, `DM2`, etc.)
