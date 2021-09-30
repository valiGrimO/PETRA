import bpy
from petra_blender_addon import popup


# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

node1 = S.node_tree.nodes["Render Layers"]  # This is "Render Layer"
node2 = S.node_tree.nodes["Group"]  # This is "Hub"
nodeR2 = S.node_tree.nodes["Group.003"]  # This is "Contour Lines"

# Select render Engine
C.scene.render.engine = "BLENDER_EEVEE"

# Apply material to selected objects
C.object.active_material.name = "r2_contourline"

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[5])
nodetree.links.new(node2.outputs[2], nodeR2.inputs[0])

# Adjust Output filenames (end with -Xmm)
r2_value = round(
    bpy.data.materials["r2_contourline"]
    .node_tree.nodes["Value"]
    .outputs[0]
    .default_value
)
nodeR2z = nodeR2.node_tree.nodes["File Output"]
pattern = f"Cam-##_R2_CDN%s-{r2_value}mm"
nodeR2z.file_slots[0].path = pattern % 1
nodeR2z.file_slots[1].path = pattern % 2
nodeR2z.file_slots[2].path = pattern % 3

# Check for correct rotation and scale
warning_text = """Rotation for "%s" should be equal to 0°,
and scale to 1 in order to have the right output.
If not, you should apply transformation (ctrl+A)."""
for selected_object in C.selected_objects:
    rotation = selected_object.rotation_euler
    scale = selected_object.scale
    if tuple(rotation) == (0, 0, 0) and tuple(scale) == (1, 1, 1):
        continue
    popup(warning_text % selected_object.name, title="WARNING", icon="ERROR")


# CONTOUR LINES 1
## Configure Material
# D.materials["r2_contourline"].node_tree.nodes["Math"].unmute
# D.materials["r2_contourline"].node_tree.nodes["Math.001"].mute
# D.materials["r2_contourline"].node_tree.nodes["Math.002"].mute

## Produce Documentation
# hit "produce documentation" in the PETrA Pannel (Rendering)

# CONTOUR LINES 2
## Relink compositor
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[0])
nodetree.links.new(node2.outputs[2], nodeR2.inputs[1])

## Configure Material
# D.materials["r2_contourline"].node_tree.nodes["Math.001"].unmute

## Produce Documentation
# hit "produce documentation" in the PETrA Pannel (Rendering)

# CONTOUR LINES 3
## Relink compositor
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[1])
nodetree.links.new(node2.outputs[2], nodeR2.inputs[2])

## Configure Material
D.materials["r2_contourline"].node_tree.nodes["Math.002"].unmute

## Produce Documentation
# hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
# nodetree.links.remove(node1.outputs[0], node2.inputs[5])
# nodetree.links.remove(node2.outputs[2], nodeR2.inputs[2])
