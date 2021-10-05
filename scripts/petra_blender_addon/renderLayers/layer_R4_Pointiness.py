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
modifier = selected_object.modifiers.new(name="Decimate", type="DECIMATE")
modifier.ratio = 0.5  # value definied by users
ratio_as_percent = round(modifier.ratio * 100)

# Adjust Output filenames (end with -[ratio])
nodeR4Output = nodeR4.node_tree.nodes["File Output"]
pattern = f"Cam-##_R4_POI-{ratio_as_percent}"
nodeR4Output.file_slots[0].path = pattern

# Create link
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[7])
nodetree.links.new(nodeHubInput.outputs[4], nodeR4.inputs[0])
