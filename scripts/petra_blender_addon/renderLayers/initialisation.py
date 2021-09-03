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

# Set color Management to default
bpy.context.scene.view_settings.view_transform = 'Filmic'

# Hide in render
bpy.data.objects["Reference Sphere"].hide_render = True
bpy.data.objects["Framing Box"].hide_render = True


#/////////////////////
# Configure Compositor

# Get reference
node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"
nodeC1 = S.node_tree.nodes["Group.001"]# This is "C1: Color"
nodeH = S.node_tree.nodes["Group"].node_tree.nodes["Group"] # This is "H: Covering"
nodeL1 = S.node_tree.nodes["Group"].node_tree.nodes["Group.001"]# This is "L1: Ambient Occlusion"
nodeR1 = S.node_tree.nodes["Group.002"]# This is "R1: Shading"
nodeR2 = S.node_tree.nodes["Group.003"]# This is "Contour Lines"
nodeR3 = S.node_tree.nodes["Group.004"]# This is "Distance Map"
nodeR4 = S.node_tree.nodes["Group.005"]# This is "Pointiness"
nodeR5 = S.node_tree.nodes["Group.006"]# This is Aspect
nodeR6 = S.node_tree.nodes["Group"].node_tree.nodes["Group.002"] # This is "R6: Slope"

# Remove links from "Render Layers" to "Hub"
# nodetree.links.remove(node1.outputs[0], node2.inputs[0])
# nodetree.links.remove(node1.outputs[0], node2.inputs[1])
# nodetree.links.remove(node1.outputs[0], node2.inputs[2])
# nodetree.links.remove(node1.outputs[0], node2.inputs[3])
# nodetree.links.remove(node1.outputs[0], node2.inputs[4])
# nodetree.links.remove(node1.outputs[0], node2.inputs[5])
# nodetree.links.remove(node1.outputs[0], node2.inputs[6])
# nodetree.links.remove(node1.outputs[0], node2.inputs[7])
# nodetree.links.remove(node1.outputs[0], node2.inputs[8])
# nodetree.links.remove(node1.outputs[0], node2.inputs[9])

# Remove links from "Hub" to "C1: Color"
# nodetree.links.remove(node2.outputs[0], nodeC1.inputs[0])
# nodetree.links.remove(node2.outputs[0], nodeC1.inputs[1])

# Remove links from "Hub" to "R2: Contour Lines"
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[0])
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[1])
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[2])

# Remove links from "Hub" to "R4: Pointiness"
# nodetree.links.remove(node2.outputs[4], nodeR4.inputs[0])
# nodetree.links.remove(node2.outputs[4], nodeR4.inputs[1])
# nodetree.links.remove(node2.outputs[4], nodeR4.inputs[2])

# Remove links from "Hub" to "R5: Aspect"
# nodetree.links.remove(node2.outputs[5], nodeR5.inputs[0])
# nodetree.links.remove(node2.outputs[5], nodeR5.inputs[1])
# nodetree.links.remove(node2.outputs[5], nodeR5.inputs[2])

# Render Display Type: Keep User Interface
