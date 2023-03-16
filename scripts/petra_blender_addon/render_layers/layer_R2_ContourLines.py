import bpy
from petra_blender_addon import popup
from petra_blender_addon.blendertools import remove_link


# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = S.node_tree.nodes["Render Layers"]
node_PETrA = S.node_tree.nodes["PETrA"]
node_R2 = node_PETrA.node_tree.nodes["R2_contourLine"]
node_R2_nodetree = node_R2.node_tree
node_R2b = node_R2.node_tree.nodes["ColorRamp"]
node_R2z = node_R2.node_tree.nodes["File Output"]


# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"


# Apply material to selected objects
material = D.materials["R2_CL"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material


# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')


# Get the value
mat = D.materials["R2_CL"].node_tree
r2_value = round(mat.nodes["value"].outputs[0].default_value)

space1 = str(r2_value)
space2 = str(r2_value * 5)
space3 = str(r2_value * 10)

# Identify which CL is produced and name it
CL = "1"
if mat.nodes["CL1"].is_active_output == True:
    CL = mat.nodes["CL1"].name
    node_R2z.file_slots[0].path = "Cam-##_R2_" + CL + "-" + space1 + "mm"

if mat.nodes["CL2"].is_active_output == True:
    CL = mat.nodes["CL2"].name
    node_R2z.file_slots[0].path = "Cam-##_R2_" + CL + "-" + space2 + "mm"
    
if mat.nodes["CL3"].is_active_output == True:
    CL = mat.nodes["CL3"].name
    node_R2z.file_slots[0].path = "Cam-##_R2_" + CL + "-" + space3 + "mm"
    
# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[5])

