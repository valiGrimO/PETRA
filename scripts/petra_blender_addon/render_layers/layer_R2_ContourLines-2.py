import bpy
from petra_blender_addon import popup
from petra_blender_addon.blendertools import remove_link


# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = C.scene.node_tree

node_RL = S.node_tree.nodes["Render Layers"]
node_PETrA = S.node_tree.nodes["PETrA"]
node_R2 = node_PETrA.node_tree.nodes["R2_contourLine"]
node_R2_nodetree = node_R2.node_tree
node_R2b = node_R2.node_tree.nodes["ColorRamp"]
node_R2z = node_R2.node_tree.nodes["File Output"]

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material to selected objects
material = D.materials["r2_contourline"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Apply material to every selected object
bpy.ops.object.make_links_data(type='MATERIAL')

# Adjust Output filenames (end with -Xmm)
r2_value = round(
    D.materials["r2_contourline"]
    .node_tree.nodes["Value"]
    .outputs[0]
    .default_value
)
node_R2z.file_slots[0].path = f"Cam-##_R2_CDN1-{r2_value}mm"
node_R2z.file_slots[1].path = f"Cam-##_R2_CDN2-{r2_value * 5}mm"
node_R2z.file_slots[2].path = f"Cam-##_R2_CDN3-{r2_value * 10}mm"

# Check for correct rotation and scale
warning_text = """Rotation for "%s" should be equal to 0°,
and scale to 1 in order to have the right output.
If not, you should apply any transformation (ctrl+A)."""
for selected_object in C.selected_objects:
    rotation = selected_object.rotation_euler
    scale = selected_object.scale
    if tuple(rotation) == (0, 0, 0) and tuple(scale) == (1, 1, 1):
        continue
    popup(warning_text % selected_object.name, title="WARNING", icon="ERROR")

# Configure Material
D.materials["r2_contourline"].node_tree.nodes["Math"].mute = False
D.materials["r2_contourline"].node_tree.nodes["Math.001"].mute = False
D.materials["r2_contourline"].node_tree.nodes["Math.002"].mute = True

# Configure Compositor
for i in range(3):  # loops through "i = 0 ... 2".
    remove_link(node_R2b.outputs[0], node_R2z.inputs[i])

nodetree.links.new(node_RL.outputs[0], node_PETrA.inputs[5])
node_R2_nodetree.links.new(node_R2b.outputs[0], node_R2z.inputs[1])