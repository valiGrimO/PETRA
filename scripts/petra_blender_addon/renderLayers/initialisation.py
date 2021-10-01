################################################################
# Setting everything properly to render any layer of information 
# (in case a user change something)
################################################################

import bpy

C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

# Don't render `Reference Sphere`
bpy.data.objects["Reference Sphere"].hide_render = True

## Render transparent background
C.scene.render.film_transparent = True

## Color management
C.scene.view_settings.view_transform = 'Standard'

# Hide in render
bpy.data.objects["Reference Sphere"].hide_render = True
bpy.data.objects["Framing Box"].hide_render = True


#/////////////////////
# Configure Compositor

# Get reference
nodeRL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
nodeHub = S.node_tree.nodes["Hub"] # This is "Hub"
nodeC1 = S.node_tree.nodes["C1_color"]# This is "C1: Color"
nodeH = S.node_tree.nodes["Hub"].node_tree.nodes["H_covering"] # This is "H: Covering"
nodeL1 = S.node_tree.nodes["Hub"].node_tree.nodes["L1_AO"]# This is "L1: Ambient Occlusion"
nodeR1 = S.node_tree.nodes["R1_shading"]# This is "R1: Shading"
nodeR2 = S.node_tree.nodes["R2_contourLine"]# This is "Contour Lines"
nodeR3 = S.node_tree.nodes["R3_distanceMap"]# This is "Distance Map"
nodeR4 = S.node_tree.nodes["R4_pointiness"]# This is "Pointiness"
nodeR5 = S.node_tree.nodes["R5_aspect"]# This is Aspect
nodeR6 = S.node_tree.nodes["Hub"].node_tree.nodes["R6_slope"] # This is "R6: Slope"

# Remove links from "Render Layers" to "Hub"
def remove_link(socket_out, socket_in):
    for link in socket_out.links:
        if link.to_socket == socket_in:
            nodetree.links.remove(link)

remove_link(nodeRL.outputs[0], nodeHub.inputs[0])
remove_link(nodeRL.outputs[0], nodeHub.inputs[1])
remove_link(nodeRL.outputs[0], nodeHub.inputs[2])
remove_link(nodeRL.outputs[0], nodeHub.inputs[3])
remove_link(nodeRL.outputs[0], nodeHub.inputs[4])
remove_link(nodeRL.outputs[0], nodeHub.inputs[5])
remove_link(nodeRL.outputs[0], nodeHub.inputs[6])
remove_link(nodeRL.outputs[0], nodeHub.inputs[7])
remove_link(nodeRL.outputs[0], nodeHub.inputs[8])
remove_link(nodeRL.outputs[0], nodeHub.inputs[9])

remove_link(nodeHub.outputs[0], nodeC1.inputs[0])
remove_link(nodeHub.outputs[0], nodeC1.inputs[1])

remove_link(nodeHub.outputs[4], nodeR4.inputs[1])
remove_link(nodeHub.outputs[4], nodeR4.inputs[2])

remove_link(nodeHub.outputs[5], nodeR5.inputs[1])
remove_link(nodeHub.outputs[5], nodeR5.inputs[2])

# Render Display Type: Keep User Interface
