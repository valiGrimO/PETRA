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

# Activate Ambient Occlusion
C.scene.eevee.use_gtao = True

# Ambient Occlusion Distance
C.scene.eevee.gtao_distance = 5

# Ambient Occlusion Quality
C.scene.eevee.gtao_quality = 1

# Apply material to selected objects
material = D.materials["l1_ao"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')

# Configure Compositor
nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[3])
