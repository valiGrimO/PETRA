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
material = D.materials["R3_DM"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[6])

# Adjust Output filenames
node_R3_Output0 = node_R3.node_tree.nodes["File Output"]
node_R3_Output1 = node_R3.node_tree.nodes["File Output.001"]

R3_ID_full = D.materials["R3_DM"].node_tree.nodes["inputColor"].layer_name
R3_ID = R3_ID_full[0:3]

node_R3_Output0.file_slots[0].path = f"Cam-##_R3_{R3_ID}"
node_R3_Output1.file_slots[0].path = f"Cam-##_R3_{R3_ID_full}_NDG"
node_R3_Output1.file_slots[1].path = f"Cam-##_R3_{R3_ID_full}_BBR"
node_R3_Output1.file_slots[2].path = f"Cam-##_R3_{R3_ID_full}_BVJR"
node_R3_Output1.file_slots[3].path = f"Cam-##_R3_{R3_ID_full}_MAGMA"
node_R3_Output1.file_slots[4].path = f"Cam-##_R3_{R3_ID_full}_SPECTRAL"
node_R3_Output1.file_slots[5].path = f"Cam-##_R3_{R3_ID_full}_VIRIDIS"
node_R3_Output1.file_slots[6].path = f"Cam-##_R3_{R3_ID}_H1"





#################################################
# tmp
tmpR3 = bpy.data.node_groups["R3: Deviation Map"].nodes["tmp_R3"]

tmpR3.file_slots[0].path = f"Cam-##_R3_{R3_ID}_MAGMA"
tmpR3.file_slots[1].path = f"Cam-##_R3_{R3_ID}_H1"
