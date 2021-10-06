import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = S.node_tree.nodes["Render Layers"]
node_PETrA = S.node_tree.nodes["PETrA"]

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material
material = D.materials["r6_slope"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

refSphere = D.objects["Reference Sphere"]
refSphere.material_slots[0].material = material

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[9])

# Render `Reference Sphere`
D.objects["Reference Sphere"].hide_render = False
