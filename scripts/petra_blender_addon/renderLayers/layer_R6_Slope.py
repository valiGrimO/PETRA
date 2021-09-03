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

# Apply material
C.object.active_material.name = "r6_slope"
# D.objects["Reference Sphere"].active_material.name = "r6_slope" # bug
        
# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[9])

# Render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = False

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set `Reference Sphere` in its initial state
D.objects["Reference Sphere"].hide_render = True

# Set Compositor in its initial state
# nodetree.links.remove(node1.outputs[0], node2.inputs[9]) # bug
