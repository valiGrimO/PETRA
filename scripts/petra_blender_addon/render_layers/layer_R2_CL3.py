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
node_R2_tmp = bpy.data.node_groups["R2: Contour Lines"].nodes["tmp_CL"]


# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"


# Apply material to selected objects
material = D.materials["R2_CL"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material


# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')

# Apply the right spacing
D.materials["R2_CL"].node_tree.nodes["math1"].mute = False
D.materials["R2_CL"].node_tree.nodes["math2"].mute = False
D.materials["R2_CL"].node_tree.nodes["math3"].mute = False


# Output name
node_R2z.file_slots[0].path = "Cam-##_R2_CL3"
node_R2_tmp.file_slots[0].path = "Cam-##_R2_CL3"

    
# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[5])
