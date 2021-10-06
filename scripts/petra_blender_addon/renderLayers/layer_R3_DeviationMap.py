import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = S.node_tree.nodes["Render Layers"]
node_PETrA = S.node_tree.nodes["PETrA"]

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material to selected objects
material = D.materials["r3_deviation_map"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[6])

# Change vertex color in the material
D.materials["r3_deviation_map"].node_tree.nodes["Vertex Color"].layer_name = "DM1"

# Note: Since several Vertex Color Indexes beginning with `DM` might exist (max = 7), then a loop have to render everyone, and the output name should be incremented (`DM1`, `DM2`, etc.)
