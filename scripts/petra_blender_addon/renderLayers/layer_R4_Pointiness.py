import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]

node1 = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
node2 = S.node_tree.nodes["Group"] # This is "Hub"
nodeR4 = S.node_tree.nodes["Group.005"]# This is "Pointiness"

# Select render Engine
C.scene.render.engine = 'CYCLES'

# Apply material to selected objects
C.object.active_material.name = "r4_pointiness"

# 100%
## Configure Compositor
nodetree.links.new(node1.outputs[0], node2.inputs[7])
nodetree.links.new(node2.outputs[4], nodeR4.inputs[0])

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# 25%
# Decimate Selected mesh
bpy.ops.object.modifier_add(type='DECIMATE')
C.object.modifiers["Decimate"].ratio = 0.25

## Configure Compositor
nodetree.links.remove(node2.outputs[4], nodeR4.inputs[0])
nodetree.links.new(node2.outputs[4], nodeR4.inputs[1])

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# 10%
# Decimate Selected mesh
bpy.ops.object.modifier_add(type='DECIMATE')
bpy.context.object.modifiers["Decimate"].ratio = 0.1

## Configure Compositor
nodetree.links.remove(node2.outputs[4], nodeR4.inputs[1])
nodetree.links.new(node2.outputs[4], nodeR4.inputs[2])

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Delete DECIMATE modifyer on selected object
bpy.ops.object.modifier_remove(modifier="Decimate")

# Set Compositor in its initial state
nodetree.links.remove(node1.outputs[0], node2.inputs[7])
nodetree.links.remove(node2.outputs[4], nodeR4.inputs[2])