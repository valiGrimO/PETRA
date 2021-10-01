import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

nodeRL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
nodeHub = S.node_tree.nodes["Group"] # This is "Hub"

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Activate Ambient Occlusion
bpy.context.scene.eevee.use_gtao = True

# Ambient Occlusion Distance
bpy.context.scene.eevee.gtao_distance = 5

# Ambient Occlusion Quality
bpy.context.scene.eevee.gtao_quality = 1

# Apply material to selected objects
material = bpy.data.materials["l1_ao"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Configure Compositor
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[3])

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Deactivate Ambient Occlusion
bpy.context.scene.eevee.use_gtao = False