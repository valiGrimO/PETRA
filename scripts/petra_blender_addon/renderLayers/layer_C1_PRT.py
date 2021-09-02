import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"
nodeC1 = S.node_tree.nodes["Group.001"]# This is "C1: Color"

# Material
    # Material should be configured first by user

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[0])
nodetree.links.new(node2.outputs[0], nodeC1.inputs[0])

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[0])
nodetree.links.remove(node2.outputs[0], nodeC1.inputs[0])
