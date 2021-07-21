import bpy


# https://docs.blender.org/api/current/bpy.types.CompositorNode.html

# switch on nodes and get reference
bpy.context.scene.use_nodes = True
nodetree = bpy.context.scene.node_tree

# clear default nodes
for node in nodetree.nodes:
    nodetree.nodes.remove(node)

# adding Render Layers, node 1
node1 = nodetree.nodes.new("CompositorNodeRLayers")
node1.location = (0, 0)

# adding compositor, node 2
node2 = nodetree.nodes.new("CompositorNodeComposite")
node2.location = (300, -200)

# adding Bright/Contraste, node 3
node3 = nodetree.nodes.new("CompositorNodeBrightContrast")
node3.location = (300, 0)

# adding Group, node 4
node4 = nodetree.nodes.new("CompositorNodeGroup")
node4.location = (300, -340)

# --------------------------------------------------
# adding subtree of node 4
# --------------------------------------------------
node4.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Group.001")
node4_nodetree = node4.node_tree  # shortcut; akin to `nodetree`

node4_in = node4_nodetree.nodes.new("NodeGroupInput")
node4_in.location = (0, 0)
node4_nodetree.inputs.new("NodeSocketColor", "C1: Color")
node4_nodetree.inputs.new("NodeSocketColor", "H1: Masks")

node4_out = node4_nodetree.nodes.new("NodeGroupOutput")
node4_out.location = (200, -200)
node4_nodetree.outputs.new("NodeSocketColor", "C1")

node4_1 = node4_nodetree.nodes.new("CompositorNodeBrightContrast")
node4_1.location = (200, 0)

node4_nodetree.links.new(node4_in.outputs["C1: Color"], node4_out.inputs["C1"])
# --------------------------------------------------

# adding Output, node 5
node5 = nodetree.nodes.new("CompositorNodeOutputFile")
node5.location = (500, 0)
node5.base_path = "/tmp/other"
node5.format.file_format = "TIFF"
node5.format.color_mode = "BW"

# connecting nodes
nodetree.links.new(node1.outputs[0], node2.inputs[0])
nodetree.links.new(node1.outputs[0], node3.inputs[0])
nodetree.links.new(node1.outputs[0], node4.inputs[0])
nodetree.links.new(node3.outputs[0], node5.inputs[0])

# https://blenderartists.org/t/python-add-custom-nodegroup/1205661/2
