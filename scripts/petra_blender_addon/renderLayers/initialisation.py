################################################################
# Setting everything properly to render any layer of information
# (in case a user change something)
################################################################

import bpy
from petra_blender_addon.blendertools import remove_link


C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

# Don't render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = True

## Render transparent background
C.scene.render.film_transparent = True

## Color management
C.scene.view_settings.view_transform = "Standard"

# Hide in render
D.objects["Reference Sphere"].hide_render = True
D.objects["Framing Box"].hide_render = True

# Deactivate Ambient Occlusion
C.scene.eevee.use_gtao = False

# Remove "Decimate" modifier
bpy.ops.object.modifier_remove(modifier="Decimate")


# /////////////////////
# Configure Compositor

# Get reference
node_RL = nodetree.nodes["Render Layers"]
node_PETrA = nodetree.nodes["PETrA"]
node_PETrA_Input = node_PETrA.node_tree.nodes["Group Input"]
node_C1 = node_PETrA.node_tree.nodes["C1_color"]
node_H = node_PETrA.node_tree.nodes["H_covering"]
node_L1 = node_PETrA.node_tree.nodes["L1_AO"]
node_R1 = node_PETrA.node_tree.nodes["R1_shading"]
node_R2 = node_PETrA.node_tree.nodes["R2_contourLine"]
node_R3 = node_PETrA.node_tree.nodes["R3_distanceMap"]
node_R4 = node_PETrA.node_tree.nodes["R4_pointiness"]
node_R5 = node_PETrA.node_tree.nodes["R5_aspect"]
node_R6 = node_PETrA.node_tree.nodes["R6_slope"]

for i in range(10):  # loops through "i = 0 ... 9".
    remove_link(node_RL.outputs[0], node_PETrA.inputs[i])

remove_link(node_PETrA_Input.outputs[0], node_C1.inputs[0])
remove_link(node_PETrA_Input.outputs[0], node_C1.inputs[1])

# Render Display Type: Keep User Interface
