import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

nodeRL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
nodeHub = S.node_tree.nodes["Hub"] # This is "Hub"
nodeC1 = S.node_tree.nodes["C1_color"]# This is "C1: Color"

# Material
    # Material should be configured first by user

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Configure Compositor
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[0])
nodetree.links.new(nodeHub.outputs[0], nodeC1.inputs[0])
