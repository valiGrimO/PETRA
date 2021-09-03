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

# Apply material to selected objects
C.object.active_material.name = "r3_deviation_map" # bug

# Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[6])

#################################################
# *This part is written in MarkDown:*

# We have to configure some options through the interface of the plugin. We need to match:
# 1. the vertex group available (`col`, `DM1`, `DM2`)
# 2. with extreme values

# Those options are to be configured in the `r3_deviation_map` material.

# *End of the MarkDown passage.*
#################################################

# DM1
## Change vertex color in the material
D.materials["r3_deviation_map"].node_tree.nodes["Vertex Color"].layer_name = "DM1"

## Un/mute outputs
# D.node_groups["R3: Distance Map"].nodes["File Output"].unmute # bug
# D.node_groups["R3: Distance Map"].nodes["File Output.001"].mute
# D.node_groups["R3: Distance Map"].nodes["File Output.002"].unmute
# D.node_groups["R3: Distance Map"].nodes["File Output.003"].mute

## hit "produce documentation" in the PETrA Pannel (Rendering)

# DM2
## Change vertex color in the material
D.materials["r3_deviation_map"].node_tree.nodes["Vertex Color"].layer_name = "DM2"

## Un/mute outputs
# D.node_groups["R3: Distance Map"].nodes["File Output"].mute
# D.node_groups["R3: Distance Map"].nodes["File Output.001"].unmute
# D.node_groups["R3: Distance Map"].nodes["File Output.002"].mute
# D.node_groups["R3: Distance Map"].nodes["File Output.003"].unmute

# hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
# nodetree.links.remove(node1.outputs[0], node2.inputs[6]) # bug