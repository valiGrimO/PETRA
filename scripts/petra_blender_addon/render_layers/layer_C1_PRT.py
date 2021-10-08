import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = S.node_tree.nodes["Render Layers"]
node_PETrA = S.node_tree.nodes["PETrA"]
node_PETrA_Input = node_PETrA.node_tree.nodes["Group Input"]
node_PETrA_nodetree = node_PETrA.node_tree
node_C1 = node_PETrA.node_tree.nodes["C1_color"]

# Materials
    # Material should be configured first by user

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[0])
node_PETrA_nodetree.links.new(node_PETrA_Input.outputs[0], node_C1.inputs[0]) # not working
