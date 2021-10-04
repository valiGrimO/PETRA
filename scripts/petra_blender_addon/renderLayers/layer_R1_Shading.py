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
material = bpy.data.materials["r1_nmc"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

refSphere = bpy.data.objects["Reference Sphere"]
refSphere.material_slots[0].material = material

# Render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = False

# Configure Compositor
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[4])
