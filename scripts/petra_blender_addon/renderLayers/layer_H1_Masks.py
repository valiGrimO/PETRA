import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]

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

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
C.object.active_material.name = "h1_masks"

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[1])

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[1])