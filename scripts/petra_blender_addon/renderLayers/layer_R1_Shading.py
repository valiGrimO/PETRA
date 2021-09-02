import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
C.object.active_material.name = "r1_nmc"
D.objects["Reference Sphere"].active_material.name = "r1_nmc"

# Render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = False

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[4])

# Set color management
bpy.context.scene.view_settings.view_transform = 'Standard'

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set `Reference Sphere` in its initial state
bpy.data.objects["Reference Sphere"].hide_render = True

# Set color Management to default
bpy.context.scene.view_settings.view_transform = 'Filmic'

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[4])