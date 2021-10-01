import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

nodeRL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
nodeHub = S.node_tree.nodes["Hub"] # This is "Hub"
nodeR5 = S.node_tree.nodes["R5_aspect"]# This is Aspect

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material
material = bpy.data.materials["r5_aspect"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

refSphere = bpy.data.objects["Reference Sphere"]
refSphere.material_slots[0].material = material
        
# Configure Compositor
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[8])
nodetree.links.new(nodeHub.outputs[5], nodeR5.inputs[0])

# Render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = False

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)