import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

nodeRL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
nodeHub = S.node_tree.nodes["Hub"] # This is "Hub"
nodeC1 = S.node_tree.nodes["C1_color"]# This is "C1: Color"

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material
material = bpy.data.materials["c1_prv"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material
D.materials["c1_prv"].node_tree.nodes["Vertex Color"].layer_name = "Col"

# Configure Compositor
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[0])
nodetree.links.new(nodeHub.outputs[0], nodeC1.inputs[1])

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)