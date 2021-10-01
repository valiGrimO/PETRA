import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

nodeRL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
nodeHub = S.node_tree.nodes["Hub"] # This is "Hub"

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material to selected objects
material = bpy.data.materials["r3_deviation_map"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Configure Compositor
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[6])

# Change vertex color in the material
D.materials["r3_deviation_map"].node_tree.nodes["Vertex Color"].layer_name = "DM1"

# hit "produce documentation" in the PETrA Pannel (Rendering)

# Note: Since several Vertex Color Indexes beginning with `DM` might exist (max = 7), then a loop have to render everyone, and the output name should be incremented (`DM1`, `DM2`, etc.)