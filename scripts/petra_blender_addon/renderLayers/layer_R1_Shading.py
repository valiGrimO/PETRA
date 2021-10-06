import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node_PETrA = S.node_tree.nodes["PETrA"] # This is "Hub"

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material to selected objects
material = D.materials["r1_nmc"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

refSphere = D.objects["Reference Sphere"]
refSphere.material_slots[0].material = material

# Render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = False

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[4])
