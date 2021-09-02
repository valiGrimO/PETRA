import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"
nodeC1 = S.node_tree.nodes["Group.001"]# This is "C1: Color"

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Apply material 
C.object.active_material.name = "c1_prv"
D.materials["c1_prv"].node_tree.nodes["Vertex Color"].layer_name = "Col"

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[0])
nodetree.links.new(node2.outputs[0], nodeC1.inputs[1])

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[0])
nodetree.links.remove(node2.outputs[0], nodeC1.inputs[1])

