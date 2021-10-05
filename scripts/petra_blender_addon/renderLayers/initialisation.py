################################################################
# Setting everything properly to render any layer of information
# (in case a user change something)
################################################################

import bpy
from petra_blender_addon.blendertools import remove_link


C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

# Don't render `Reference Sphere`
bpy.data.objects["Reference Sphere"].hide_render = True

## Render transparent background
C.scene.render.film_transparent = True

## Color management
C.scene.view_settings.view_transform = "Standard"

# Hide in render
bpy.data.objects["Reference Sphere"].hide_render = True
bpy.data.objects["Framing Box"].hide_render = True

# Deactivate Ambient Occlusion
bpy.context.scene.eevee.use_gtao = False

# /////////////////////
# Configure Compositor

# Get reference
nodeRL = nodetree.nodes["Render Layers"]  # This is "Render Layer"
nodeHub = nodetree.nodes["Hub"]  # This is "Hub"
nodeHubInput = nodeHub.node_tree.nodes["Group Input"]
nodeC1 = nodeHub.node_tree.nodes["C1_color"]  # This is "C1: Color"
nodeH = nodeHub.node_tree.nodes["H_covering"]  # This is "H: Covering"
nodeL1 = nodeHub.node_tree.nodes["L1_AO"]  # This is "L1: Ambient Occlusion"
nodeR1 = nodeHub.node_tree.nodes["R1_shading"]  # This is "R1: Shading"
nodeR2 = nodeHub.node_tree.nodes["R2_contourLine"]  # This is "Contour Lines"
nodeR3 = nodeHub.node_tree.nodes["R3_distanceMap"]  # This is "Distance Map"
nodeR4 = nodeHub.node_tree.nodes["R4_pointiness"]  # This is "Pointiness"
nodeR5 = nodeHub.node_tree.nodes["R5_aspect"]  # This is Aspect
nodeR6 = nodeHub.node_tree.nodes["R6_slope"]  # This is "R6: Slope"

for i in range(10):  # loops through "i = 0 ... 9".
    remove_link(nodeRL.outputs[0], nodeHub.inputs[i])

remove_link(nodeHubInput.outputs[0], nodeC1.inputs[0])
remove_link(nodeHubInput.outputs[0], nodeC1.inputs[1])

remove_link(nodeHubInput.outputs[4], nodeR4.inputs[0])

remove_link(nodeHubInput.outputs[5], nodeR5.inputs[0])

# Render Display Type: Keep User Interface
