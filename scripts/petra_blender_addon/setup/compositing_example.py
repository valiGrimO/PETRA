import bpy

# https://docs.blender.org/api/current/bpy.types.CompositorNode.html

# ------------------------------------------------------------------
# INITIAL SETUP
# ------------------------------------------------------------------

# switch on nodes and get reference
bpy.context.scene.use_nodes = True
nodetree = bpy.context.scene.node_tree

# clear default nodes
for node in nodetree.nodes:
    nodetree.nodes.remove(node)

# adding Render Layers, node 1
node1 = nodetree.nodes.new("CompositorNodeRLayers")
node1.location = (0, 0)



# ------------------------------------------------------------------
# HUB
# ------------------------------------------------------------------

# adding nodegroup, node 2
node2 = nodetree.nodes.new("CompositorNodeGroup")
node2.location = (300, 100)

# ------------------------------------------------------------------
# subtree

node2.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Hub")
node2_nodetree = node2.node_tree  # shortcut; akin to `nodetree`

# create input
node2_in = node2_nodetree.nodes.new("NodeGroupInput")
node2_in.location = (0, 0)
node2_nodetree.inputs.new("NodeSocketColor", "C1: Color")
node2_nodetree.inputs.new("NodeSocketColor", "H1: Masks")
node2_nodetree.inputs.new("NodeSocketColor", "H2: Outline By Normals")
node2_nodetree.inputs.new("NodeSocketColor", "L1: Ambient Occlusion")
node2_nodetree.inputs.new("NodeSocketColor", "R1: Shading")
node2_nodetree.inputs.new("NodeSocketColor", "R2: Contour Lines")
node2_nodetree.inputs.new("NodeSocketColor", "R3: Distance Map")
node2_nodetree.inputs.new("NodeSocketColor", "R4: Pointiness")
node2_nodetree.inputs.new("NodeSocketColor", "R5: Aspect")
node2_nodetree.inputs.new("NodeSocketColor", "R6: Slope")

# hide input values -- Not working
# bpy.data.node_groups["Hub"].inputs[0].hide_value
# bpy.data.node_groups["Hub"].inputs[1].hide_value
# bpy.data.node_groups["Hub"].inputs[2].hide_value
# bpy.data.node_groups["Hub"].inputs[3].hide_value
# bpy.data.node_groups["Hub"].inputs[4].hide_value
# bpy.data.node_groups["Hub"].inputs[5].hide_value
# bpy.data.node_groups["Hub"].inputs[6].hide_value
# bpy.data.node_groups["Hub"].inputs[7].hide_value
# bpy.data.node_groups["Hub"].inputs[8].hide_value
# bpy.data.node_groups["Hub"].inputs[9].hide_value

# create outputs
node2_out = node2_nodetree.nodes.new("NodeGroupOutput")
node2_out.location = (400, 0)
node2_nodetree.outputs.new("NodeSocketColor", "C1")
node2_nodetree.outputs.new("NodeSocketColor", "R1")
node2_nodetree.outputs.new("NodeSocketColor", "R2")
node2_nodetree.outputs.new("NodeSocketColor", "R3")
node2_nodetree.outputs.new("NodeSocketColor", "R4")
node2_nodetree.outputs.new("NodeSocketColor", "R5")

# hide output values -- Not working
# bpy.data.node_groups["Hub"].outputs[0].hide_value
# bpy.data.node_groups["Hub"].outputs[1].hide_value
# bpy.data.node_groups["Hub"].outputs[2].hide_value
# bpy.data.node_groups["Hub"].outputs[3].hide_value
# bpy.data.node_groups["Hub"].outputs[4].hide_value
# bpy.data.node_groups["Hub"].outputs[5].hide_value


# node2_1 = node2_nodetree.nodes.new("CompositorNodeBrightContrast")
# node2_1.location = (200, 0)


# ------------------------------------------------------------------
# connections

node2_nodetree.links.new(node2_in.outputs["C1: Color"], node2_out.inputs["C1"])
node2_nodetree.links.new(node2_in.outputs["R1: Shading"], node2_out.inputs["R1"])
node2_nodetree.links.new(node2_in.outputs["R2: Contour Lines"], node2_out.inputs["R2"])
node2_nodetree.links.new(node2_in.outputs["R3: Distance Map"], node2_out.inputs["R3"])
node2_nodetree.links.new(node2_in.outputs["R4: Pointiness"], node2_out.inputs["R4"])
node2_nodetree.links.new(node2_in.outputs["R5: Aspect"], node2_out.inputs["R5"])


