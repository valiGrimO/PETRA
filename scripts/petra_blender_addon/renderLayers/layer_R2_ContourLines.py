import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"
nodeR2 = S.node_tree.nodes["Group.003"]# This is "Contour Lines"

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
C.object.active_material.name = "r2_contourline"

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[5])
nodetree.links.new(node2.outputs[2], nodeR2.inputs[0])

# CONTOUR LINES 1
## Configure Material
# D.materials["r2_contourline"].node_tree.nodes["Math"].unmute
# D.materials["r2_contourline"].node_tree.nodes["Math.001"].mute
# D.materials["r2_contourline"].node_tree.nodes["Math.002"].mute

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# CONTOUR LINES 2
## Relink compositor
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[0])
nodetree.links.new(node2.outputs[2], nodeR2.inputs[1])

## Configure Material
# D.materials["r2_contourline"].node_tree.nodes["Math.001"].unmute

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# CONTOUR LINES 3
## Relink compositor
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[1])
nodetree.links.new(node2.outputs[2], nodeR2.inputs[2])

## Configure Material
D.materials["r2_contourline"].node_tree.nodes["Math.002"].unmute

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
# nodetree.links.remove(node1.outputs[0], node2.inputs[5])
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[2])