import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"
nodeR5 = S.node_tree.nodes["Group.006"]# This is Aspect

# Select render Engine
C.scene.render.engine = 'BLENDER_EEVEE'

# Apply material
C.object.active_material.name = "r5_aspect"
D.objects["Reference Sphere"].active_material.name = "r5_aspect"
        
# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[8])
nodetree.links.new(nodeR5.outputs[5], node2.inputs[0])

# Render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = False

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[8])
nodetree.links.remove(nodeR5.outputs[5], node2.inputs[0])

# Set `Reference Sphere` in its initial state
D.objects["Reference Sphere"].hide_render = True


# /////////////////////////////////////////
# NOTE: We have to define if it's necessary to create different LOD (100%; 25% 10%)
# Rendering a mesh with a decimation modifyer is really time consuming