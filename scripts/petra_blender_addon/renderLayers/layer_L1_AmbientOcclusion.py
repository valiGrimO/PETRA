import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Activate Ambient Occlusion
bpy.context.scene.eevee.use_gtao = True

# Ambient Occlusion Distance
bpy.context.scene.eevee.gtao_distance = 5

# Ambient Occlusion Quality
bpy.context.scene.eevee.gtao_quality = 1

# Apply material to selected objects
C.object.active_material.name = "l1_ao"

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[3])

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Deactivate Ambient Occlusion
bpy.context.scene.eevee.use_gtao = False

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[3])