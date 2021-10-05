import bpy
from petra_blender_addon.blendertools import remove_link


# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = S.node_tree

nodeRL = nodetree.nodes["Render Layers"]  # This is "Render Layer"
nodeHub = nodetree.nodes["Hub"]  # This is "Hub"
nodeHubInput = nodeHub.node_tree.nodes["Group Input"]
nodeR4 = nodeHub.node_tree.nodes["R4_pointiness"]  # This is "Pointiness"

# Select render Engine
C.scene.render.engine = "CYCLES"

# Apply material to selected objects
material = bpy.data.materials["r4_pointiness"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material


remove_link(nodeHubInput.outputs[4], nodeR4.inputs[0])
# remove_link(nodeHubInput.outputs[4], nodeR4.inputs[1])
# remove_link(nodeHubInput.outputs[4], nodeR4.inputs[2])

# Decimate Selected mesh
# bpy.ops.object.modifier_add(type="DECIMATE")
# C.object.modifiers["Decimate"].ratio = # value definied by users

# Create link
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[7])
nodetree.links.new(nodeHubInput.outputs[4], nodeR4.inputs[0])
