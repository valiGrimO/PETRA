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

# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[6])

# Adjust Output filenames
node_R3_Output0 = node_R3.node_tree.nodes["File Output"]
node_R3_Output1 = node_R3.node_tree.nodes["File Output.001"]
id_DM = D.materials["r3_deviation_map"].node_tree.nodes["Vertex Color"].layer_name
node_R3_Output0.file_slots[0].path = f"Cam-##_R3_{id_DM}"
node_R3_Output1.file_slots[0].path = f"Cam-##_R3_{id_DM}_BBR"
node_R3_Output1.file_slots[1].path = f"Cam-##_R3_{id_DM}_BVJR"
node_R3_Output1.file_slots[2].path = f"Cam-##_R3_{id_DM}_MAGMA"
node_R3_Output1.file_slots[3].path = f"Cam-##_R3_{id_DM}_SPECTRAL"
node_R3_Output1.file_slots[4].path = f"Cam-##_R3_{id_DM}_VIRIDIS"
node_R3_Output1.file_slots[5].path = f"Cam-##_H1_{id_DM}"

# Change vertex color in the material
# D.materials["r3_deviation_map"].node_tree.nodes["Vertex Color"].layer_name = "DM1"

# Note: Since several Vertex Color Indexes beginning with `DM` might exist (max = 7), then a loop have to render everyone, and the output name should be incremented (`DM1`, `DM2`, etc.)
