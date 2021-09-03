import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
C.object.active_material.name = "h2_obn"

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[2])

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[2])
