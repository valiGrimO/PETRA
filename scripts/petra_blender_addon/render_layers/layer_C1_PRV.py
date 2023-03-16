import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = nodetree.nodes["Render Layers"]
node_PETrA = nodetree.nodes["PETrA"]
node_PETrA_Input = node_PETrA.node_tree.nodes["Group Input"]
node_PETrA_nodetree = node_PETrA.node_tree
node_C1 = node_PETrA.node_tree.nodes["C1_color"]

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material
material = D.materials["C1_PRV"]

selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material
D.materials["C1_PRV"].node_tree.nodes["inputColor"].layer_name = "Col"

# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[0])
node_PETrA_nodetree.links.new(node_PETrA_Input.outputs[0], node_C1.inputs[1])
