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



# ------------------------------------------------------------------
# Render Layers - NODE 1
# ------------------------------------------------------------------

# adding Render Layers, node 1
node1 = nodetree.nodes.new("CompositorNodeRLayers")
node1.location = (-300, -260)



# ------------------------------------------------------------------
# HUB - NODE 2
# ------------------------------------------------------------------

# adding nodegroup, node 2
node2 = nodetree.nodes.new("CompositorNodeGroup")
node2.location = (0, 0)

# subtree description
node2.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Hub")
node2_nodetree = node2.node_tree  # shortcut; akin to `nodetree`

# create input
node2_in = node2_nodetree.nodes.new("NodeGroupInput")
node2_in.location = (0, 0)
node2_nodetree.inputs.new("NodeSocketColor", "C1: Color")
node2_nodetree.inputs.new("NodeSocketColor", "H1: Masks")
node2_nodetree.inputs.new("NodeSocketColor", "H2: Outline By Normal")
node2_nodetree.inputs.new("NodeSocketColor", "L1: Ambient Occlusion")
node2_nodetree.inputs.new("NodeSocketColor", "R1: Shading")
node2_nodetree.inputs.new("NodeSocketColor", "R2: Contour Lines")
node2_nodetree.inputs.new("NodeSocketColor", "R3: Distance Map")
node2_nodetree.inputs.new("NodeSocketColor", "R4: Pointiness")
node2_nodetree.inputs.new("NodeSocketColor", "R5: Aspect")
node2_nodetree.inputs.new("NodeSocketColor", "R6: Slope")

# hide input values
for node2_input in node2_nodetree.inputs:
    node2_input.hide_value = True

# create outputs
node2_out = node2_nodetree.nodes.new("NodeGroupOutput")
node2_out.location = (240, 0)
node2_nodetree.outputs.new("NodeSocketColor", "C1")
node2_nodetree.outputs.new("NodeSocketColor", "R1")
node2_nodetree.outputs.new("NodeSocketColor", "R2")
node2_nodetree.outputs.new("NodeSocketColor", "R3")
node2_nodetree.outputs.new("NodeSocketColor", "R4")
node2_nodetree.outputs.new("NodeSocketColor", "R5")

# hide output values
for node2_output in node2_nodetree.inputs:
    node2_output.hide_value = True



    # --------------------------------------------------------------
    # H: Covering - NODE H
    # --------------------------------------------------------------

# adding nodegroup, node H
nodeH = node2_nodetree.nodes.new("CompositorNodeGroup")
nodeH.location = (240, 260)

# subtree description
nodeH.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="H: Covering")
nodeH_nodetree = nodeH.node_tree  # shortcut; akin to `nodetree`

# create input
nodeH_in = nodeH_nodetree.nodes.new("NodeGroupInput")
nodeH_in.location = (0, 0)
nodeH_nodetree.inputs.new("NodeSocketColor", "Cam-##_H1_Masks")
nodeH_nodetree.inputs.new("NodeSocketColor", "Cam-##_H2_Outline By Normal")
nodeH_nodetree.inputs.new("NodeSocketColor", "Cam-##_H3_Details")

## H1 - Masks
nodeH1a = nodeH_nodetree.nodes.new("CompositorNodeSepRGBA")
nodeH1a.location = (180, 260)

nodeH1b = nodeH_nodetree.nodes.new("CompositorNodeBlur")
nodeH1b.location = (360, 500)
# size_x = 20
# size_y = 20

nodeH1c = nodeH_nodetree.nodes.new("CompositorNodeValToRGB")
nodeH1c.location = (540, 500)
# colorRamp.interpolation = Constant
# cursor1 (loc = 0.0 ; colorHex = FFFFFF)
# cursor2 (loc = 0.1 ; colorHex = 000000)

nodeH1d = nodeH_nodetree.nodes.new("CompositorNodeValToRGB")
nodeH1d.location = (540, 260)
# colorRamp.interpolation = Constant
# cursor1 (loc = 0.0 ; colorHex = 898989)

nodeH1e = nodeH_nodetree.nodes.new("CompositorNodeMixRGB")
nodeH1e.location = (820, 500)
# blend_type = Multiply

nodeH1f = nodeH_nodetree.nodes.new("CompositorNodeMixRGB")
nodeH1f.location = (1000, 500)
# blend_type = Difference

nodeH1g = nodeH_nodetree.nodes.new("CompositorNodeValToRGB")
nodeH1g.location = (1180, 500)
# colorRamp.interpolation = Constant
# cursor1 (loc = 0.0 ; colorHex = FFFFFF)
# cursor1 (loc = 0.0 ; colorHex = 898989)
# cursor1 (loc = 0.0 ; colorHex = 000000)

nodeH1h = nodeH_nodetree.nodes.new("CompositorNodeFilter")
nodeH1h.location = (1460, 500)

nodeH1i = nodeH_nodetree.nodes.new("CompositorNodeSetAlpha")
nodeH1i.location = (1640, 500)

## H2 - Outline by Normals
nodeH2a = nodeH_nodetree.nodes.new("CompositorNodeFilter")
nodeH2a.location = (180, 0)
# filter_type = sobel

nodeH2b = nodeH_nodetree.nodes.new("CompositorNodeValToRGB")
nodeH2b.location = (540, 0)
# cursor1 (loc = 0.2 ; colorHex = 000000)
# cursor2 (loc = 0.3 ; colorHex = FFFFFF)

nodeH2c = nodeH_nodetree.nodes.new("CompositorNodeInvert")
nodeH2c.location = (820, 0)

nodeH2d = nodeH_nodetree.nodes.new("CompositorNodeGamma")
nodeH2d.location = (1000, 0)
# gamma value = 10.0


## H3 - Details
nodeH3a = nodeH_nodetree.nodes.new("CompositorNodeFilter")
nodeH3a.location = (180, -240)
# filter_type = prewitt

nodeH3b = nodeH_nodetree.nodes.new("CompositorNodeRGBToBW")
nodeH3b.location = (540, -240)

nodeH3c = nodeH_nodetree.nodes.new("CompositorNodeInvert")
nodeH3c.location = (820, -240)

nodeH3d = nodeH_nodetree.nodes.new("CompositorNodeGamma")
nodeH3d.location = (1000, -240)
# gamma value = 1.5

nodeH3e = nodeH_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeH3e.location = (1180, -240)

## H1 - File Output
nodeH1z = nodeH_nodetree.nodes.new("CompositorNodeOutputFile")
nodeH1z.location = (1820, 500)
nodeH1z.base_path = "//tmp"
nodeH1z.format.file_format = "PNG"
nodeH1z.format.color_mode = "RGBA"
nodeH1z.format.compression = 100
nodeH1z.file_slots[0].path = "Cam-##_H1_Masks"

## H2 - File Output
nodeH2z = nodeH_nodetree.nodes.new("CompositorNodeOutputFile")
nodeH2z.location = (1420, -180)
nodeH2z.base_path = "//tmp"
nodeH2z.format.file_format = "JPEG"
nodeH2z.format.color_mode = "BW"
nodeH2z.format.quality = 100
nodeH2z.file_slots[0].path = "Cam-##_H2_OBN"
nodeH2z.file_slots.new("Cam-##_H3_Details")

#connections
## H1
nodeH_nodetree.links.new(nodeH_in.outputs[0], nodeH1a.inputs[0])
nodeH_nodetree.links.new(nodeH1a.outputs[0], nodeH1b.inputs[0])
nodeH_nodetree.links.new(nodeH1b.outputs[0], nodeH1c.inputs[0])
nodeH_nodetree.links.new(nodeH1a.outputs[2], nodeH1d.inputs[0])
nodeH_nodetree.links.new(nodeH1c.outputs[1], nodeH1e.inputs[1])
nodeH_nodetree.links.new(nodeH1d.outputs[1], nodeH1e.inputs[2])
nodeH_nodetree.links.new(nodeH1e.outputs[0], nodeH1f.inputs[1])
nodeH_nodetree.links.new(nodeH1f.outputs[0], nodeH1g.inputs[0])
nodeH_nodetree.links.new(nodeH1g.outputs[0], nodeH1h.inputs[1])
nodeH_nodetree.links.new(nodeH1h.outputs[0], nodeH1i.inputs[0])
nodeH_nodetree.links.new(nodeH1a.outputs[3], nodeH1i.inputs[1])
nodeH_nodetree.links.new(nodeH1i.outputs[0], nodeH1z.inputs[0])
## H2
nodeH_nodetree.links.new(nodeH_in.outputs[1], nodeH2a.inputs[0])
nodeH_nodetree.links.new(nodeH2a.outputs[0], nodeH2b.inputs[0])
nodeH_nodetree.links.new(nodeH2b.outputs[0], nodeH2c.inputs[0])
nodeH_nodetree.links.new(nodeH2c.outputs[0], nodeH2d.inputs[0])
nodeH_nodetree.links.new(nodeH2d.outputs[0], nodeH2z.inputs[0])
## H3
nodeH_nodetree.links.new(nodeH_in.outputs[2], nodeH3a.inputs[0])
nodeH_nodetree.links.new(nodeH3a.outputs[0], nodeH3b.inputs[0])
nodeH_nodetree.links.new(nodeH3b.outputs[0], nodeH3c.inputs[0])
nodeH_nodetree.links.new(nodeH3c.outputs[0], nodeH3d.inputs[0])
nodeH_nodetree.links.new(nodeH3d.outputs[0], nodeH3e.inputs[1])
nodeH_nodetree.links.new(nodeH3e.outputs[0], nodeH2z.inputs[1])

    # --------------------------------------------------------------
    # L1: Ambient Occlusion - NODE L1
    # --------------------------------------------------------------

# adding nodegroup, node L1
nodeL1 = node2_nodetree.nodes.new("CompositorNodeGroup")
nodeL1.location = (240, 120)

# subtree description
nodeL1.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="L1: Ambient Occlusion")
nodeL1_nodetree = nodeL1.node_tree  # shortcut; akin to `nodetree`

# create inputs
nodeL1_in = nodeL1_nodetree.nodes.new("NodeGroupInput")
nodeL1_in.location = (0, 0)
nodeL1_nodetree.inputs.new("NodeSocketColor", "Cam-##_L1_AO")

nodeL1a = nodeL1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeL1a.location = (200, 0)

## File Output
nodeL1b = nodeL1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeL1b.location = (400, 0)
nodeL1b.base_path = "//tmp"
nodeL1b.format.file_format = "JPEG"
nodeL1b.format.color_mode = "BW"
nodeL1b.format.quality = 100
nodeL1b.file_slots[0].path = "Cam-##_L1_AO"

# connections
nodeL1_nodetree.links.new(nodeL1_in.outputs["Cam-##_L1_AO"], nodeL1a.inputs["Image"])
nodeL1_nodetree.links.new(nodeL1a.outputs[0], nodeL1b.inputs[0])


    # --------------------------------------------------------------
    # R6: Slope - NODE R6
    # --------------------------------------------------------------

# adding nodegroup, node R6
nodeR6 = node2_nodetree.nodes.new("CompositorNodeGroup")
nodeR6.location = (240, -200)

# subtree description
nodeR6.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R6: Slope")
nodeR6_nodetree = nodeR6.node_tree  # shortcut; akin to `nodetree`

# create inputs
nodeR6_in = nodeR6_nodetree.nodes.new("NodeGroupInput")
nodeR6_in.location = (0, 0)
nodeR6_nodetree.inputs.new("NodeSocketColor", "Cam-##_R6_Slope")

nodeR6a = nodeR6_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR6a.location = (200, 0)

## File Output
nodeR6b = nodeR6_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR6b.location = (400, 0)
nodeR6b.base_path = "//tmp"
nodeR6b.format.file_format = "JPEG"
nodeR6b.format.color_mode = "BW"
nodeR6b.format.quality = 100
nodeR6b.file_slots[0].path = "Cam-##_R6_Slope"

# connections
nodeR6_nodetree.links.new(nodeR6_in.outputs[0], nodeR6a.inputs[0])
nodeR6_nodetree.links.new(nodeR6a.outputs[0], nodeR6b.inputs[0])


# ------------------------------------------------------------------
# connections

node2_nodetree.links.new(node2_in.outputs["C1: Color"], node2_out.inputs["C1"])
node2_nodetree.links.new(node2_in.outputs["R1: Shading"], node2_out.inputs["R1"])
node2_nodetree.links.new(node2_in.outputs["R2: Contour Lines"], node2_out.inputs["R2"])
node2_nodetree.links.new(node2_in.outputs["R3: Distance Map"], node2_out.inputs["R3"])
node2_nodetree.links.new(node2_in.outputs["R4: Pointiness"], node2_out.inputs["R4"])
node2_nodetree.links.new(node2_in.outputs["R5: Aspect"], node2_out.inputs["R5"])
node2_nodetree.links.new(node2_in.outputs["H1: Masks"], nodeH.inputs["Cam-##_H1_Masks"])
node2_nodetree.links.new(node2_in.outputs["H2: Outline By Normal"], nodeH.inputs["Cam-##_H2_Outline By Normal"])
node2_nodetree.links.new(node2_in.outputs["R1: Shading"], nodeH.inputs["Cam-##_H3_Details"])
node2_nodetree.links.new(node2_in.outputs["L1: Ambient Occlusion"], nodeL1.inputs["Cam-##_L1_AO"])
node2_nodetree.links.new(node2_in.outputs["R6: Slope"], nodeR6.inputs["Cam-##_R6_Slope"])


# ------------------------------------------------------------------
# C1: COLOR
# ------------------------------------------------------------------
# adding nodegroup, node C1
nodeC1 = nodetree.nodes.new("CompositorNodeGroup")
nodeC1.location = (400, 280)

# subtree description
nodeC1.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="C1: Color")
nodeC1_nodetree = nodeC1.node_tree  # shortcut; akin to `nodetree`

# create input
nodeC1_in = nodeC1_nodetree.nodes.new("NodeGroupInput")
nodeC1_in.location = (0, 0)
nodeC1_nodetree.inputs.new("NodeSocketColor", "Cam-##_C1_PRTexture")
nodeC1_nodetree.inputs.new("NodeSocketColor", "Cam-##_C1_PRVertex")

# hide input values
for nodeC1_input in nodeC1_nodetree.inputs:
    nodeC1_input.hide_value = True

# inside the group
nodeC1a = nodeC1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeC1a.location = (180, 160)

nodeC1b = nodeC1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeC1b.location = (180, 0)

## File Output
nodeC1z = nodeC1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeC1z.location = (360, 60)
nodeC1z.base_path = "//tmp"
nodeC1z.format.file_format = "PNG"
nodeC1z.format.color_mode = "RGBA"
nodeC1z.format.compression = 0
nodeC1z.file_slots[0].path = "Cam-##_C1_PRT"
nodeC1z.file_slots.new("Cam-##_C1_PRV")

# connections
nodetree.links.new(node2.outputs[0], nodeC1.inputs[1])
nodeC1_nodetree.links.new(nodeC1_in.outputs[0], nodeC1a.inputs[0])
nodeC1_nodetree.links.new(nodeC1_in.outputs[1], nodeC1b.inputs[0])
nodeC1_nodetree.links.new(nodeC1a.outputs[0], nodeC1z.inputs[0])
nodeC1_nodetree.links.new(nodeC1b.outputs[0], nodeC1z.inputs[1])

# ------------------------------------------------------------------
# R1: SHADING
# ------------------------------------------------------------------
# adding nodegroup, node R1
nodeR1 = nodetree.nodes.new("CompositorNodeGroup")
nodeR1.location = (400, 160)

# subtree description
nodeR1.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R1: Shading")
nodeR1_nodetree = nodeR1.node_tree  # shortcut; akin to `nodetree`

# create inputs
nodeR1_in = nodeR1_nodetree.nodes.new("NodeGroupInput")
nodeR1_in.location = (0, 0)
nodeR1_nodetree.inputs.new("NodeSocketColor", "Cam-##_R1")

# hide input values
for nodeR1_input in nodeR1_nodetree.inputs:
    nodeR1_input.hide_value = True


## ---------------------
## NMC source
## ---------------------

nodeR1a = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR1a.location = (1000, 1340)

## File Output
nodeR1zA = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR1zA.location = (1400, 1340)
nodeR1zA.base_path = "//tmp"
nodeR1zA.format.file_format = "PNG"
nodeR1zA.format.color_mode = "RGBA"
nodeR1zA.format.compression = 0
nodeR1zA.file_slots[0].path = "Cam-##_R1_NMC"

# connections
nodetree.links.new(node2.outputs[1], nodeR1.inputs[0])
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeR1a.inputs[0])
nodeR1_nodetree.links.new(nodeR1a.outputs[0], nodeR1zA.inputs[0])

## ---------------------
## B1
## ---------------------
# adding nodegroup
nodeB1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeB1g.location = (1000, 1180)

# subtree description
nodeB1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="B1")
nodeB1g_nodetree = nodeB1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeB1g_in = nodeB1g_nodetree.nodes.new("NodeGroupInput")
nodeB1g_in.location = (0, 0)
nodeB1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeB1a = nodeB1g_nodetree.nodes.new("CompositorNodeSepRGBA")
nodeB1a.location = (180, 0)

nodeB1b = nodeB1g_nodetree.nodes.new("CompositorNodeGamma")
nodeB1b.location = (360, 0)
    # gamma = 2.4

# create group's output
nodeB1g_out = nodeB1g_nodetree.nodes.new("NodeGroupOutput")
nodeB1g_out.location = (540, 0)
nodeB1g_nodetree.outputs.new("NodeSocketColor", "output")

## File Output
nodeBout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeBout.location = (1400, 1180)
nodeBout.base_path = "//tmp"
nodeBout.format.file_format = "JPEG"
nodeBout.format.color_mode = "BW"
nodeBout.format.quality = 100
nodeBout.file_slots[0].path = "Cam-##_R1_NMC_B1"
nodeBout.file_slots.new("Cam-##_R1_NMC_B2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeB1g.inputs[0])
nodeR1_nodetree.links.new(nodeB1g.outputs[0], nodeBout.inputs[0])
    #inside nodegroup
nodeB1g_nodetree.links.new(nodeB1g_in.outputs[0], nodeB1a.inputs[0])
nodeB1g_nodetree.links.new(nodeB1a.outputs[2], nodeB1b.inputs[0])
nodeB1g_nodetree.links.new(nodeB1b.outputs[0], nodeB1g_out.inputs[0])


## ---------------------
## B2
## ---------------------
# adding nodegroup
nodeB2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeB2g.location = (1000, 1060)

# subtree description
nodeB2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="B2")
nodeB2g_nodetree = nodeB2g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeB2g_in = nodeB2g_nodetree.nodes.new("NodeGroupInput")
nodeB2g_in.location = (0, 0)
nodeB2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeB2a = nodeB2g_nodetree.nodes.new("CompositorNodeSepRGBA")
nodeB2a.location = (180, 0)

nodeB2b = nodeB2g_nodetree.nodes.new("CompositorNodeGamma")
nodeB2b.location = (360, 0)
    # gamma = 2.4

nodeB2c = nodeB2g_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeB2c.location = (540, 0)
    # controlPoint1_X = 0
    # controlPoint1_Y = 1
    # controlPoint2_X = 0.25
    # controlPoint2_Y = 0.25
    # controlPoint3_X = 1
    # controlPoint3_Y = 0

# create group's output
nodeB2g_out = nodeB2g_nodetree.nodes.new("NodeGroupOutput")
nodeB2g_out.location = (780, 0)
nodeB2g_nodetree.outputs.new("NodeSocketColor", "output")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeB2g.inputs[0])
nodeR1_nodetree.links.new(nodeB2g.outputs[0], nodeBout.inputs[1])
    #inside nodegroup
nodeB2g_nodetree.links.new(nodeB2g_in.outputs[0], nodeB2a.inputs[0])
nodeB2g_nodetree.links.new(nodeB2a.outputs[2], nodeB2b.inputs[0])
nodeB2g_nodetree.links.new(nodeB2b.outputs[0], nodeB2c.inputs[1])
nodeB2g_nodetree.links.new(nodeB2c.outputs[0], nodeB2g_out.inputs[0])

## ---------------------
## Cb1
## ---------------------
# adding nodegroup
nodeCb1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeCb1g.location = (1000, 940)

# subtree description
nodeCb1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Cb1")
nodeCb1g_nodetree = nodeCb1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeCb1g_in = nodeCb1g_nodetree.nodes.new("NodeGroupInput")
nodeCb1g_in.location = (0, 0)
nodeCb1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeCb1a = nodeCb1g_nodetree.nodes.new("CompositorNodeSepYCCA")
nodeCb1a.location = (180, 0)
    # mode = ITU 709

nodeCb1b = nodeCb1g_nodetree.nodes.new("CompositorNodeGamma")
nodeCb1b.location = (360, 0)
    # gamma = 3.6

# create group's output
nodeCb1g_out = nodeCb1g_nodetree.nodes.new("NodeGroupOutput")
nodeCb1g_out.location = (540, 0)
nodeCb1g_nodetree.outputs.new("NodeSocketColor", "output")

## File Output
nodeCbout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeCbout.location = (1400, 940)
nodeCbout.base_path = "//tmp"
nodeCbout.format.file_format = "JPEG"
nodeCbout.format.color_mode = "BW"
nodeCbout.format.quality = 100
nodeCbout.file_slots[0].path = "Cam-##_R1_NMC_Cb1"
nodeCbout.file_slots.new("Cam-##_R1_NMC_Cb2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeCb1g.inputs[0])
nodeR1_nodetree.links.new(nodeCb1g.outputs[0], nodeCbout.inputs[0])
    #inside nodegroup
nodeCb1g_nodetree.links.new(nodeCb1g_in.outputs[0], nodeCb1a.inputs[0])
nodeCb1g_nodetree.links.new(nodeCb1a.outputs[1], nodeCb1b.inputs[0])
nodeCb1g_nodetree.links.new(nodeCb1b.outputs[0], nodeCb1g_out.inputs[0])

## ---------------------
## Cb2
## ---------------------
# adding nodegroup
nodeCb2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeCb2g.location = (1000, 820)

# subtree description
nodeCb2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Cb2")
nodeCb2g_nodetree = nodeCb2g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeCb2g_in = nodeCb2g_nodetree.nodes.new("NodeGroupInput")
nodeCb2g_in.location = (0, 0)
nodeCb2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeCb2a = nodeCb2g_nodetree.nodes.new("CompositorNodeSepYCCA")
nodeCb2a.location = (180, 0)
    # mode = ITU 601

nodeCb2b = nodeCb2g_nodetree.nodes.new("CompositorNodeGamma")
nodeCb2b.location = (360, 0)
    # gamma = 2.4

nodeCb2c = nodeCb2g_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeCb2c.location = (540, 0)
    # controlPoint1_X = 0
    # controlPoint1_Y = 1
    # controlPoint2_X = 0.25
    # controlPoint2_Y = 0.25
    # controlPoint3_X = 1
    # controlPoint3_Y = 0

# create group's output
nodeCb2g_out = nodeCb2g_nodetree.nodes.new("NodeGroupOutput")
nodeCb2g_out.location = (780, 0)
nodeCb2g_nodetree.outputs.new("NodeSocketColor", "output")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeCb2g.inputs[0])
nodeR1_nodetree.links.new(nodeCb2g.outputs[0], nodeCbout.inputs[1])
    #inside nodegroup
nodeCb2g_nodetree.links.new(nodeCb2g_in.outputs[0], nodeCb2a.inputs[0])
nodeCb2g_nodetree.links.new(nodeCb2a.outputs[1], nodeCb2b.inputs[0])
nodeCb2g_nodetree.links.new(nodeCb2b.outputs[0], nodeCb2c.inputs[1])
nodeCb2g_nodetree.links.new(nodeCb2c.outputs[0], nodeCb2g_out.inputs[0])

## ---------------------
## Cr1
## ---------------------
# adding nodegroup
nodeCr1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeCr1g.location = (1000, 700)

# subtree description
nodeCr1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Cr1")
nodeCr1g_nodetree = nodeCr1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeCr1g_in = nodeCr1g_nodetree.nodes.new("NodeGroupInput")
nodeCr1g_in.location = (0, 0)
nodeCr1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeCr1a = nodeCr1g_nodetree.nodes.new("CompositorNodeSepYCCA")
nodeCr1a.location = (180, 0)
    # mode = ITU 601

nodeCr1b = nodeCr1g_nodetree.nodes.new("CompositorNodeGamma")
nodeCr1b.location = (360, 0)
    # gamma = 2.4

# create group's output
nodeCr1g_out = nodeCr1g_nodetree.nodes.new("NodeGroupOutput")
nodeCr1g_out.location = (540, 0)
nodeCr1g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeCr1Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeCr1Flat.location = (1180, 700)
nodeCr1Flat.mute = True
    # Bright = 23.0
    # Contrast = 68.0

## File Output
nodeCrout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeCrout.location = (1400, 700)
nodeCrout.base_path = "//tmp"
nodeCrout.format.file_format = "JPEG"
nodeCrout.format.color_mode = "BW"
nodeCrout.format.quality = 100
nodeCrout.file_slots[0].path = "Cam-##_R1_NMC_Cr1"
nodeCrout.file_slots.new("Cam-##_R1_NMC_Cr2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeCr1g.inputs[0])
nodeR1_nodetree.links.new(nodeCr1g.outputs[0], nodeCr1Flat.inputs[0])
nodeR1_nodetree.links.new(nodeCr1Flat.outputs[0], nodeCrout.inputs[0])
    #inside nodegroup
nodeCr1g_nodetree.links.new(nodeCr1g_in.outputs[0], nodeCr1a.inputs[0])
nodeCr1g_nodetree.links.new(nodeCr1a.outputs[2], nodeCr1b.inputs[0])
nodeCr1g_nodetree.links.new(nodeCr1b.outputs[0], nodeCr1g_out.inputs[0])

## ---------------------
## Cr2
## ---------------------
# adding nodegroup
nodeCr2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeCr2g.location = (1000, 540)

# subtree description
nodeCr2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Cr2")
nodeCr2g_nodetree = nodeCr2g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeCr2g_in = nodeCr2g_nodetree.nodes.new("NodeGroupInput")
nodeCr2g_in.location = (0, 0)
nodeCr2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeCr2a = nodeCr2g_nodetree.nodes.new("CompositorNodeSepYCCA")
nodeCr2a.location = (180, 0)
    # mode = ITU 601

nodeCr2b = nodeCr2g_nodetree.nodes.new("CompositorNodeGamma")
nodeCr2b.location = (360, 0)
    # gamma = 2.4

nodeCr2c = nodeCr2g_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeCr2c.location = (540, 0)
    # controlPoint1_X = 0
    # controlPoint1_Y = 1
    # controlPoint2_X = 0.25
    # controlPoint2_Y = 0.25
    # controlPoint3_X = 1
    # controlPoint3_Y = 0

# create group's output
nodeCr2g_out = nodeCr2g_nodetree.nodes.new("NodeGroupOutput")
nodeCr2g_out.location = (780, 0)
nodeCr2g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeCr2Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeCr2Flat.location = (1180, 540)
nodeCr2Flat.mute = True
    # Bright = 0.0
    # Contrast = 68.0

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeCr2g.inputs[0])
nodeR1_nodetree.links.new(nodeCr2g.outputs[0], nodeCr2Flat.inputs[0])
nodeR1_nodetree.links.new(nodeCr2Flat.outputs[0], nodeCrout.inputs[1])
    #inside nodegroup
nodeCr2g_nodetree.links.new(nodeCr2g_in.outputs[0], nodeCr2a.inputs[0])
nodeCr2g_nodetree.links.new(nodeCr2a.outputs[2], nodeCr2b.inputs[0])
nodeCr2g_nodetree.links.new(nodeCr2b.outputs[0], nodeCr2c.inputs[1])
nodeCr2g_nodetree.links.new(nodeCr2c.outputs[0], nodeCr2g_out.inputs[0])

## ---------------------
## G1
## ---------------------
# adding nodegroup
nodeG1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeG1g.location = (1000, 380)

# subtree description
nodeG1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="G1")
nodeG1g_nodetree = nodeG1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeG1g_in = nodeG1g_nodetree.nodes.new("NodeGroupInput")
nodeG1g_in.location = (0, 0)
nodeG1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeG1a = nodeG1g_nodetree.nodes.new("CompositorNodeSepRGBA")
nodeG1a.location = (180, 0)

# create group's output
nodeG1g_out = nodeG1g_nodetree.nodes.new("NodeGroupOutput")
nodeG1g_out.location = (360, 0)
nodeG1g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeG1Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeG1Flat.location = (1180, 380)
nodeG1Flat.mute = True
    # Bright = 0.0
    # Contrast = 30.0

## File Output
nodeGout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeGout.location = (1400, 380)
nodeGout.base_path = "//tmp"
nodeGout.format.file_format = "JPEG"
nodeGout.format.color_mode = "BW"
nodeGout.format.quality = 100
nodeGout.file_slots[0].path = "Cam-##_R1_NMC_G1"
nodeGout.file_slots.new("Cam-##_R1_NMC_G2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeG1g.inputs[0])
nodeR1_nodetree.links.new(nodeG1g.outputs[0], nodeG1Flat.inputs[0])
nodeR1_nodetree.links.new(nodeG1Flat.outputs[0], nodeGout.inputs[0])
    #inside nodegroup
nodeG1g_nodetree.links.new(nodeG1g_in.outputs[0], nodeG1a.inputs[0])
nodeG1g_nodetree.links.new(nodeG1a.outputs[1], nodeG1g_out.inputs[0])

## ---------------------
## G2
## ---------------------
# adding nodegroup
nodeG2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeG2g.location = (1000, 220)

# subtree description
nodeG2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="G2")
nodeG2g_nodetree = nodeG2g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeG2g_in = nodeG2g_nodetree.nodes.new("NodeGroupInput")
nodeG2g_in.location = (0, 0)
nodeG2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeG2a = nodeG2g_nodetree.nodes.new("CompositorNodeSepRGBA")
nodeG2a.location = (180, 0)

nodeG2b = nodeG2g_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeG2b.location = (360, 0)
    # controlPoint1_X = 0
    # controlPoint1_Y = 1
    # controlPoint2_X = 0.25
    # controlPoint2_Y = 0.25
    # controlPoint3_X = 1
    # controlPoint3_Y = 0

# create group's output
nodeG2g_out = nodeG2g_nodetree.nodes.new("NodeGroupOutput")
nodeG2g_out.location = (600, 0)
nodeG2g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeG2Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeG2Flat.location = (1180, 220)
nodeG2Flat.mute = True
    # Bright = 0.0
    # Contrast = 40.0

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeG2g.inputs[0])
nodeR1_nodetree.links.new(nodeG2g.outputs[0], nodeG2Flat.inputs[0])
nodeR1_nodetree.links.new(nodeG2Flat.outputs[0], nodeGout.inputs[1])
    #inside nodegroup
nodeG2g_nodetree.links.new(nodeG2g_in.outputs[0], nodeG2a.inputs[0])
nodeG2g_nodetree.links.new(nodeG2a.outputs[1], nodeG2b.inputs[1])
nodeG2g_nodetree.links.new(nodeG2b.outputs[0], nodeG2g_out.inputs[0])

## ---------------------
## Red1
## ---------------------
# adding nodegroup
nodeRed1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeRed1g.location = (1000, 60)

# subtree desRediption
nodeRed1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R1")
nodeRed1g_nodetree = nodeRed1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeRed1g_in = nodeRed1g_nodetree.nodes.new("NodeGroupInput")
nodeRed1g_in.location = (0, 0)
nodeRed1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeRed1a = nodeRed1g_nodetree.nodes.new("CompositorNodeSepRGBA")
nodeRed1a.location = (180, 0)

# create group's output
nodeRed1g_out = nodeRed1g_nodetree.nodes.new("NodeGroupOutput")
nodeRed1g_out.location = (360, 0)
nodeRed1g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeRed1Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeRed1Flat.location = (1180, 60)
nodeRed1Flat.mute = True
    # Bright = 0.0
    # Contrast = 30.0

## File Output
nodeRedout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeRedout.location = (1400, 60)
nodeRedout.base_path = "//tmp"
nodeRedout.format.file_format = "JPEG"
nodeRedout.format.color_mode = "BW"
nodeRedout.format.quality = 100
nodeRedout.file_slots[0].path = "Cam-##_R1_NMC_Red1"
nodeRedout.file_slots.new("Cam-##_R1_NMC_Red2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeRed1g.inputs[0])
nodeR1_nodetree.links.new(nodeRed1g.outputs[0], nodeRed1Flat.inputs[0])
nodeR1_nodetree.links.new(nodeRed1Flat.outputs[0], nodeRedout.inputs[0])
    #inside nodegroup
nodeRed1g_nodetree.links.new(nodeRed1g_in.outputs[0], nodeRed1a.inputs[0])
nodeRed1g_nodetree.links.new(nodeRed1a.outputs[0], nodeRed1g_out.inputs[0])

## ---------------------
## Red2
## ---------------------
# adding nodegroup
nodeRed2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeRed2g.location = (1000, -100)

# subtree desRediption
nodeRed2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R2")
nodeRed2g_nodetree = nodeRed2g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeRed2g_in = nodeRed2g_nodetree.nodes.new("NodeGroupInput")
nodeRed2g_in.location = (0, 0)
nodeRed2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeRed2a = nodeRed2g_nodetree.nodes.new("CompositorNodeSepRGBA")
nodeRed2a.location = (180, 0)

nodeRed2b = nodeRed2g_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeRed2b.location = (360, 0)
    # controlPoint1_X = 0
    # controlPoint1_Y = 1
    # controlPoint2_X = 0.25
    # controlPoint2_Y = 0.25
    # controlPoint3_X = 1
    # controlPoint3_Y = 0

# create group's output
nodeRed2g_out = nodeRed2g_nodetree.nodes.new("NodeGroupOutput")
nodeRed2g_out.location = (600, 0)
nodeRed2g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeRed2Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeRed2Flat.location = (1180, -100)
nodeRed2Flat.mute = True
    # Bright = 0.0
    # Contrast = 40.0

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeRed2g.inputs[0])
nodeR1_nodetree.links.new(nodeRed2g.outputs[0], nodeRed2Flat.inputs[0])
nodeR1_nodetree.links.new(nodeRed2Flat.outputs[0], nodeRedout.inputs[1])
    #inside nodegroup
nodeRed2g_nodetree.links.new(nodeRed2g_in.outputs[0], nodeRed2a.inputs[0])
nodeRed2g_nodetree.links.new(nodeRed2a.outputs[0], nodeRed2b.inputs[1])
nodeRed2g_nodetree.links.new(nodeRed2b.outputs[0], nodeRed2g_out.inputs[0])

## ---------------------
## S1
## ---------------------
# adding nodegroup
nodeS1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeS1g.location = (1000, -260)

# subtree description
nodeS1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="S1")
nodeS1g_nodetree = nodeS1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeS1g_in = nodeS1g_nodetree.nodes.new("NodeGroupInput")
nodeS1g_in.location = (0, 0)
nodeS1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeS1a = nodeS1g_nodetree.nodes.new("CompositorNodeSepHSVA")
nodeS1a.location = (180, 0)

nodeS1b = nodeS1g_nodetree.nodes.new("CompositorNodeGamma")
nodeS1b.location = (360, 0)
    # factor = 4.7

# create group's output
nodeS1g_out = nodeS1g_nodetree.nodes.new("NodeGroupOutput")
nodeS1g_out.location = (540, 0)
nodeS1g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeS1Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeS1Flat.location = (1180, -260)
nodeS1Flat.mute = True
    # Bright = 0.0
    # Contrast = 50.0

## File Output
nodeSout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeSout.location = (1400, -260)
nodeSout.base_path = "//tmp"
nodeSout.format.file_format = "JPEG"
nodeSout.format.color_mode = "BW"
nodeSout.format.quality = 100
nodeSout.file_slots[0].path = "Cam-##_R1_NMC_S1"
nodeSout.file_slots.new("Cam-##_R1_NMC_S2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeS1g.inputs[0])
nodeR1_nodetree.links.new(nodeS1g.outputs[0], nodeS1Flat.inputs[0])
nodeR1_nodetree.links.new(nodeS1Flat.outputs[0], nodeSout.inputs[0])
    #inside nodegroup
nodeS1g_nodetree.links.new(nodeS1g_in.outputs[0], nodeS1a.inputs[0])
nodeS1g_nodetree.links.new(nodeS1a.outputs[1], nodeS1b.inputs[0])
nodeS1g_nodetree.links.new(nodeS1b.outputs[0], nodeS1g_out.inputs[0])

## ---------------------
## S2
## ---------------------
# adding nodegroup
nodeS2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeS2g.location = (1000, -420)

# subtree description
nodeS2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="S2")
nodeS2g_nodetree = nodeS2g.node_tree  # shortcut; akin to `nodetree`

# Create group's inputs
nodeS2g_in = nodeS2g_nodetree.nodes.new("NodeGroupInput")
nodeS2g_in.location = (0, 0)
nodeS2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeS2a = nodeS2g_nodetree.nodes.new("CompositorNodeSepHSVA")
nodeS2a.location = (180, 0)

nodeS2b = nodeS2g_nodetree.nodes.new("CompositorNodeGamma")
nodeS2b.location = (360, 0)
    # factor = 4.7

nodeS2c = nodeS2g_nodetree.nodes.new("CompositorNodeInvert")
nodeS2c.location = (540, 0)

# Create group's output
nodeS2g_out = nodeS2g_nodetree.nodes.new("NodeGroupOutput")
nodeS2g_out.location = (720, 0)
nodeS2g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeS2Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeS2Flat.location = (1180, -420)
nodeS2Flat.mute = True
    # Bright = -12.0
    # Contrast = 77.0

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeS2g.inputs[0])
nodeR1_nodetree.links.new(nodeS2g.outputs[0], nodeS2Flat.inputs[0])
nodeR1_nodetree.links.new(nodeS2Flat.outputs[0], nodeSout.inputs[1])
    #inside nodegroup
nodeS2g_nodetree.links.new(nodeS2g_in.outputs[0], nodeS2a.inputs[0])
nodeS2g_nodetree.links.new(nodeS2a.outputs[1], nodeS2b.inputs[0])
nodeS2g_nodetree.links.new(nodeS2b.outputs[0], nodeS2c.inputs[1])
nodeS2g_nodetree.links.new(nodeS2c.outputs[0], nodeS2g_out.inputs[0])

## ---------------------
## U1
## ---------------------
# adding nodegroup
nodeU1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeU1g.location = (1000, -580)

# subtree description
nodeU1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="U1")
nodeU1g_nodetree = nodeU1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeU1g_in = nodeU1g_nodetree.nodes.new("NodeGroupInput")
nodeU1g_in.location = (0, 0)
nodeU1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeU1a = nodeU1g_nodetree.nodes.new("CompositorNodeSepYUVA")
nodeU1a.location = (180, 0)

nodeU1b = nodeU1g_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeU1b.location = (360, 0)
    # bright = 39.1
    # contrast = 46.1

nodeU1c = nodeU1g_nodetree.nodes.new("CompositorNodeGamma")
nodeU1c.location = (540, 0)
    # factor = 3.2

# create group's output
nodeU1g_out = nodeU1g_nodetree.nodes.new("NodeGroupOutput")
nodeU1g_out.location = (720, 0)
nodeU1g_nodetree.outputs.new("NodeSocketColor", "output")

## File Output
nodeUout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeUout.location = (1400, -580)
nodeUout.base_path = "//tmp"
nodeUout.format.file_format = "JPEG"
nodeUout.format.color_mode = "BW"
nodeUout.format.quality = 100
nodeUout.file_slots[0].path = "Cam-##_R1_NMC_U1"
nodeUout.file_slots.new("Cam-##_R1_NMC_U2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeU1g.inputs[0])
nodeR1_nodetree.links.new(nodeU1g.outputs[0], nodeUout.inputs[0])
    #inside nodegroup
nodeU1g_nodetree.links.new(nodeU1g_in.outputs[0], nodeU1a.inputs[0])
nodeU1g_nodetree.links.new(nodeU1a.outputs[1], nodeU1b.inputs[0])
nodeU1g_nodetree.links.new(nodeU1b.outputs[0], nodeU1c.inputs[0])
nodeU1g_nodetree.links.new(nodeU1c.outputs[0], nodeU1g_out.inputs[0])

## ---------------------
## U2
## ---------------------
# adding nodegroup
nodeU2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeU2g.location = (1000, -700)

# subtree description
nodeU2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="U2")
nodeU2g_nodetree = nodeU2g.node_tree  # shortcut; akin to `nodetree`

# Create group's inputs
nodeU2g_in = nodeU2g_nodetree.nodes.new("NodeGroupInput")
nodeU2g_in.location = (0, 0)
nodeU2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeU2a = nodeU2g_nodetree.nodes.new("CompositorNodeSepYUVA")
nodeU2a.location = (180, 0)

nodeU2b = nodeU2g_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeU2b.location = (360, 0)
    # bright = 39.1
    # contrast = 46.1

nodeU2c = nodeU2g_nodetree.nodes.new("CompositorNodeInvert")
nodeU2c.location = (540, 0)

# Create group's output
nodeU2g_out = nodeU2g_nodetree.nodes.new("NodeGroupOutput")
nodeU2g_out.location = (720, 0)
nodeU2g_nodetree.outputs.new("NodeSocketColor", "output")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeU2g.inputs[0])
nodeR1_nodetree.links.new(nodeU2g.outputs[0], nodeUout.inputs[1])
    #inside nodegroup
nodeU2g_nodetree.links.new(nodeU2g_in.outputs[0], nodeU2a.inputs[0])
nodeU2g_nodetree.links.new(nodeU2a.outputs[1], nodeU2b.inputs[0])
nodeU2g_nodetree.links.new(nodeU2b.outputs[0], nodeU2c.inputs[1])
nodeU2g_nodetree.links.new(nodeU2c.outputs[0], nodeU2g_out.inputs[0])

## ---------------------
## V1
## ---------------------
# adding nodegroup
# adding nodegroup
nodeV1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeV1g.location = (1000, -820)

# subtree description
nodeV1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="V1")
nodeV1g_nodetree = nodeV1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeV1g_in = nodeV1g_nodetree.nodes.new("NodeGroupInput")
nodeV1g_in.location = (0, 0)
nodeV1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeV1a = nodeV1g_nodetree.nodes.new("CompositorNodeSepHSVA")
nodeV1a.location = (180, 0)

nodeV1b = nodeV1g_nodetree.nodes.new("CompositorNodeGamma")
nodeV1b.location = (360, 0)
    # Factor = 3.2

# create group's output
nodeV1g_out = nodeV1g_nodetree.nodes.new("NodeGroupOutput")
nodeV1g_out.location = (540, 0)
nodeV1g_nodetree.outputs.new("NodeSocketColor", "output")

## File Output
nodeVout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeVout.location = (1400, -820)
nodeVout.base_path = "//tmp"
nodeVout.format.file_format = "JPEG"
nodeVout.format.color_mode = "BW"
nodeVout.format.quality = 100
nodeVout.file_slots[0].path = "Cam-##_R1_NMC_V1"
nodeVout.file_slots.new("Cam-##_R1_NMC_V2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeV1g.inputs[0])
nodeR1_nodetree.links.new(nodeV1g.outputs[0], nodeVout.inputs[0])
    #inside nodegroup
nodeV1g_nodetree.links.new(nodeV1g_in.outputs[0], nodeV1a.inputs[0])
nodeV1g_nodetree.links.new(nodeV1a.outputs[2], nodeV1b.inputs[0])
nodeV1g_nodetree.links.new(nodeV1b.outputs[0], nodeV1g_out.inputs[0])

## ---------------------
## V2
## ---------------------
# adding nodegroup
nodeV2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeV2g.location = (1000, -940)

# subtree description
nodeV2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="V2")
nodeV2g_nodetree = nodeV2g.node_tree  # shortcut; akin to `nodetree`

# Create group's inputs
nodeV2g_in = nodeV2g_nodetree.nodes.new("NodeGroupInput")
nodeV2g_in.location = (0, 0)
nodeV2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeV2a = nodeV2g_nodetree.nodes.new("CompositorNodeSepHSVA")
nodeV2a.location = (180, 0)

nodeV2b = nodeV2g_nodetree.nodes.new("CompositorNodeGamma")
nodeV2b.location = (360, 0)
    # Factor = 3.0

nodeV2c = nodeV2g_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeV2c.location = (540, 0)
    # controlPoint1_X = 0
    # controlPoint1_Y = 1
    # controlPoint2_X = 0.25
    # controlPoint2_Y = 0.25
    # controlPoint3_X = 1
    # controlPoint3_Y = 0

# Create group's output
nodeV2g_out = nodeV2g_nodetree.nodes.new("NodeGroupOutput")
nodeV2g_out.location = (780, 0)
nodeV2g_nodetree.outputs.new("NodeSocketColor", "output")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeV2g.inputs[0])
nodeR1_nodetree.links.new(nodeV2g.outputs[0], nodeVout.inputs[1])
    #inside nodegroup
nodeV2g_nodetree.links.new(nodeV2g_in.outputs[0], nodeV2a.inputs[0])
nodeV2g_nodetree.links.new(nodeV2a.outputs[2], nodeV2b.inputs[0])
nodeV2g_nodetree.links.new(nodeV2b.outputs[0], nodeV2c.inputs[1])
nodeV2g_nodetree.links.new(nodeV2c.outputs[0], nodeV2g_out.inputs[0])

## ---------------------
## Y1
## ---------------------
# adding nodegroup
nodeY1g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeY1g.location = (1000, -1060)

# subtree description
nodeY1g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Y1")
nodeY1g_nodetree = nodeY1g.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeY1g_in = nodeY1g_nodetree.nodes.new("NodeGroupInput")
nodeY1g_in.location = (0, 0)
nodeY1g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeY1a = nodeY1g_nodetree.nodes.new("CompositorNodeSepYCCA")
nodeY1a.location = (180, 0)
    # mode = ITU 601

nodeY1b = nodeY1g_nodetree.nodes.new("CompositorNodeGamma")
nodeY1b.location = (360, 0)
    # Factor = 1.9

# create group's output
nodeY1g_out = nodeY1g_nodetree.nodes.new("NodeGroupOutput")
nodeY1g_out.location = (540, 0)
nodeY1g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeY1Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeY1Flat.location = (1180, -1060)
nodeY1Flat.mute = True
    # Bright = 34.0
    # Contrast = 88.0

## File Output
nodeYout = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeYout.location = (1400, -1060)
nodeYout.base_path = "//tmp"
nodeYout.format.file_format = "JPEG"
nodeYout.format.color_mode = "BW"
nodeYout.format.quality = 100
nodeYout.file_slots[0].path = "Cam-##_R1_NMC_Y1"
nodeYout.file_slots.new("Cam-##_R1_NMC_Y2")

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeY1g.inputs[0])
nodeR1_nodetree.links.new(nodeY1g.outputs[0], nodeY1Flat.inputs[0])
nodeR1_nodetree.links.new(nodeY1Flat.outputs[0], nodeYout.inputs[0])
    #inside nodegroup
nodeY1g_nodetree.links.new(nodeY1g_in.outputs[0], nodeY1a.inputs[0])
nodeY1g_nodetree.links.new(nodeY1a.outputs[0], nodeY1b.inputs[0])
nodeY1g_nodetree.links.new(nodeY1b.outputs[0], nodeY1g_out.inputs[0])

## ---------------------
## Y2
## ---------------------
# adding nodegroup
nodeY2g = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeY2g.location = (1000, -1220)

# subtree description
nodeY2g.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="Y2")
nodeY2g_nodetree = nodeY2g.node_tree  # shortcut; akin to `nodetree`

# Create group's inputs
nodeY2g_in = nodeY2g_nodetree.nodes.new("NodeGroupInput")
nodeY2g_in.location = (0, 0)
nodeY2g_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeY2a = nodeY2g_nodetree.nodes.new("CompositorNodeSepYCCA")
nodeY2a.location = (180, 0)
    # mode = ITU 601

nodeY2b = nodeY2g_nodetree.nodes.new("CompositorNodeGamma")
nodeY2b.location = (360, 0)
    # Factor = 1.9

nodeY2c = nodeY2g_nodetree.nodes.new("CompositorNodeCurveRGB")
nodeY2c.location = (540, 0)
    # controlPoint1_X = 0
    # controlPoint1_Y = 1
    # controlPoint2_X = 0.25
    # controlPoint2_Y = 0.25
    # controlPoint3_X = 1
    # controlPoint3_Y = 0

nodeY2d = nodeY2g_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeY2d.location = (780, 0)
    # bright = 0.0
    # contrast = 30.0

# Create group's output
nodeY2g_out = nodeY2g_nodetree.nodes.new("NodeGroupOutput")
nodeY2g_out.location = (960, 0)
nodeY2g_nodetree.outputs.new("NodeSocketColor", "output")

# flat surface option
nodeY2Flat = nodeR1_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeY2Flat.location = (1180, -1220)
nodeY2Flat.mute = True
    # Bright = 1.0
    # Contrast = 80.0

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeY2g.inputs[0])
nodeR1_nodetree.links.new(nodeY2g.outputs[0], nodeY2Flat.inputs[0])
nodeR1_nodetree.links.new(nodeY2Flat.outputs[0], nodeYout.inputs[1])
    #inside nodegroup
nodeY2g_nodetree.links.new(nodeY2g_in.outputs[0], nodeY2a.inputs[0])
nodeY2g_nodetree.links.new(nodeY2a.outputs[0], nodeY2b.inputs[0])
nodeY2g_nodetree.links.new(nodeY2b.outputs[0], nodeY2c.inputs[1])
nodeY2g_nodetree.links.new(nodeY2c.outputs[0], nodeY2d.inputs[0])
nodeY2g_nodetree.links.new(nodeY2d.outputs[0], nodeY2g_out.inputs[0])



# ------------------------------------------------------------------
# R2: CONTOUR LINES
# ------------------------------------------------------------------
# adding nodegroup, node R1
nodeR2 = nodetree.nodes.new("CompositorNodeGroup")
nodeR2.location = (400, 40)

# subtree description
nodeR2.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R2: Contour Lines")
nodeR2_nodetree = nodeR2.node_tree  # shortcut; akin to `nodetree`

# create input
nodeR2_in = nodeR2_nodetree.nodes.new("NodeGroupInput")
nodeR2_in.location = (0, 0)
nodeR2_nodetree.inputs.new("NodeSocketColor", "Cam-##_R2_CDN1")
nodeR2_nodetree.inputs.new("NodeSocketColor", "Cam-##_R2_CDN2")
nodeR2_nodetree.inputs.new("NodeSocketColor", "Cam-##_R2_CDN3")

# hide input values
for nodeR2_input in nodeR2_nodetree.inputs:
    nodeR2_input.hide_value = True

# inside the group
nodeR2Aa = nodeR2_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR2Aa.location = (180, 260)

nodeR2Ba = nodeR2_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR2Ba.location = (180, 40)

nodeR2Ca = nodeR2_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR2Ca.location = (180, -180)

nodeR2Ab = nodeR2_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR2Ab.location = (360, 420)
# interpolation: Constant
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.5 ; colorHex = FFFFFF)

nodeR2Bb = nodeR2_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR2Bb.location = (360, 200)
# interpolation: Constant
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.5 ; colorHex = FFFFFF)

nodeR2Cb = nodeR2_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR2Cb.location = (360, -20)
# interpolation: Constant
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.5 ; colorHex = FFFFFF)

## File Output
nodeR2z = nodeR2_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR2z.location = (640, 280)
nodeR2z.base_path = "//tmp"
nodeR2z.format.file_format = "JPEG"
nodeR2z.format.color_mode = "BW"
nodeR2z.format.quality = 100
nodeR2z.file_slots[0].path = "Cam-##_R4_POI-100pc"
nodeR2z.file_slots.new("Cam-##_R4_POI-25pc")
nodeR2z.file_slots.new("Cam-##_R4_POI-10pc")

# connections
nodetree.links.new(node2.outputs[2], nodeR2.inputs[0]) # to change during the rendering

nodeR2_nodetree.links.new(nodeR2_in.outputs[0], nodeR2Aa.inputs[0])
nodeR2_nodetree.links.new(nodeR2_in.outputs[1], nodeR2Ba.inputs[0])
nodeR2_nodetree.links.new(nodeR2_in.outputs[2], nodeR2Ca.inputs[0])

nodeR2_nodetree.links.new(nodeR2Aa.outputs[0], nodeR2Ab.inputs[0])
nodeR2_nodetree.links.new(nodeR2Ba.outputs[0], nodeR2Bb.inputs[0])
nodeR2_nodetree.links.new(nodeR2Ca.outputs[0], nodeR2Cb.inputs[0])

nodeR2_nodetree.links.new(nodeR2Ab.outputs[0], nodeR2z.inputs[0])
nodeR2_nodetree.links.new(nodeR2Bb.outputs[0], nodeR2z.inputs[1])
nodeR2_nodetree.links.new(nodeR2Cb.outputs[0], nodeR2z.inputs[2])


# ------------------------------------------------------------------
# R3: DISTANCE MAP
# ------------------------------------------------------------------
# adding nodegroup, node R1
nodeR3 = nodetree.nodes.new("CompositorNodeGroup")
nodeR3.location = (400, -100)

# subtree description
nodeR3.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R3: Distance Map")
nodeR3_nodetree = nodeR3.node_tree  # shortcut; akin to `nodetree`

# create inputs
nodeR3_in = nodeR3_nodetree.nodes.new("NodeGroupInput")
nodeR3_in.location = (0, 0)
nodeR3_nodetree.inputs.new("NodeSocketColor", "Cam-##_R3_DM1")
nodeR3_nodetree.inputs.new("NodeSocketColor", "Cam-##_R3_DM2")

# hide input values
for nodeR3_input in nodeR3_nodetree.inputs:
    nodeR3_input.hide_value = True


nodeR3dm1A = nodeR3_nodetree.nodes.new("CompositorNodeRGBToBW")
nodeR3dm1A.location = (200, 0)   # DM2 y: -620)

nodeR3dm1B = nodeR3_nodetree.nodes.new("CompositorNodeGamma")
nodeR3dm1B.location = (340, 0)

nodeR3dm1C = nodeR3_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR3dm1C.location = (520, 0)

### DM-grey
nodeR3dm1_grey = nodeR3_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR3dm1_grey.location = (800, 640)

nodeR3dm1_grey_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_grey_out.location = (1080, 640)
nodeR3dm1_grey_out.base_path = "//tmp"
nodeR3dm1_grey_out.format.file_format = "PNG"
nodeR3dm1_grey_out.format.color_mode = "RGBA"
nodeR3dm1_grey_out.format.compression = 0
nodeR3dm1_grey_out.file_slots[0].path = "Cam-##_R3_DM1"
nodeR3dm1_grey_out.file_slots.new("Cam-##_R3_DM2")

### DM-BBR
nodeR3dm1_BBR = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_BBR.location = (800, 480)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 0000FA)
# cursor2 (loc = 0.425 ; colorHex = 4FF0F0)
# cursor3 (loc = 0.5 ; colorHex = FFFFFF)
# cursor4 (loc = 0.575 ; colorHex = F0F000)
# cursor5 (loc = 1.0 ; colorHex = FF0500)

nodeR3dm1_BBR_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_BBR_out.location = (1080, 480)
nodeR3dm1_BBR_out.base_path = "//tmp"
nodeR3dm1_BBR_out.format.file_format = "JPEG"
nodeR3dm1_BBR_out.format.color_mode = "RGB"
nodeR3dm1_BBR_out.format.quality = 100
nodeR3dm1_BBR_out.file_slots[0].path = "Cam-##_R3_DM1-BBR"
nodeR3dm1_BBR_out.file_slots.new("Cam-##_R3_DM2-BBR")

### DM-BVJR
nodeR3dm1_BVJR = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_BVJR.location = (800, 240)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 0000FF)
# cursor2 (loc = 0.4 ; colorHex = 00CC00)
# cursor3 (loc = 0.6 ; colorHex = FFFF00)
# cursor4 (loc = 1.0 ; colorHex = FF0000)

nodeR3dm1_BVJR_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_BVJR_out.location = (1080, 240)
nodeR3dm1_BVJR_out.base_path = "//tmp"
nodeR3dm1_BVJR_out.format.file_format = "JPEG"
nodeR3dm1_BVJR_out.format.color_mode = "RGB"
nodeR3dm1_BVJR_out.format.quality = 100
nodeR3dm1_BVJR_out.file_slots[0].path = "Cam-##_R3_DM1-BVJR"
nodeR3dm1_BVJR_out.file_slots.new("Cam-##_R3_DM2-BVJR")

### DM-Magma
nodeR3dm1_MAGMA = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_MAGMA.location = (800, 0)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.25 ; colorHex = 50127B)
# cursor3 (loc = 0.5 ; colorHex = B63679)
# cursor4 (loc = 0.75 ; colorHex = FC8761)
# cursor5 (loc = 1.0 ; colorHex = FCFDBF)

nodeR3dm1_MAGMA_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_MAGMA_out.location = (1080, 0)
nodeR3dm1_MAGMA_out.base_path = "//tmp"
nodeR3dm1_MAGMA_out.format.file_format = "JPEG"
nodeR3dm1_MAGMA_out.format.color_mode = "RGB"
nodeR3dm1_MAGMA_out.format.quality = 100
nodeR3dm1_MAGMA_out.file_slots[0].path = "Cam-##_R3_DM1-MAGMA"
nodeR3dm1_MAGMA_out.file_slots.new("Cam-##_R3_DM2-MAGMA")

### DM-Spectral
nodeR3dm1_SPECTRAL = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_SPECTRAL.location = (800, -240)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.25 ; colorHex = 50127B)
# cursor3 (loc = 0.5 ; colorHex = B63679)
# cursor4 (loc = 0.75 ; colorHex = FC8761)
# cursor5 (loc = 1.0 ; colorHex = FCFDBF)

nodeR3dm1_SPECTRAL_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_SPECTRAL_out.location = (1080, -240)
nodeR3dm1_SPECTRAL_out.base_path = "//tmp"
nodeR3dm1_SPECTRAL_out.format.file_format = "JPEG"
nodeR3dm1_SPECTRAL_out.format.color_mode = "RGB"
nodeR3dm1_SPECTRAL_out.format.quality = 100
nodeR3dm1_SPECTRAL_out.file_slots[0].path = "Cam-##_R3_DM1-SPECTRAL"
nodeR3dm1_SPECTRAL_out.file_slots.new("Cam-##_R3_DM2-SPECTRAL")


### DM-Viridis
nodeR3dm1_VIRIDIS = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_VIRIDIS.location = (800, -480)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.25 ; colorHex = 50127B)
# cursor3 (loc = 0.5 ; colorHex = B63679)
# cursor4 (loc = 0.75 ; colorHex = FC8761)
# cursor5 (loc = 1.0 ; colorHex = FCFDBF)

nodeR3dm1_VIRIDIS_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_VIRIDIS_out.location = (1080, -480)
nodeR3dm1_VIRIDIS_out.base_path = "//tmp"
nodeR3dm1_VIRIDIS_out.format.file_format = "JPEG"
nodeR3dm1_VIRIDIS_out.format.color_mode = "RGB"
nodeR3dm1_VIRIDIS_out.format.quality = 100
nodeR3dm1_VIRIDIS_out.file_slots[0].path = "Cam-##_R3_DM1-VIRIDIS"
nodeR3dm1_VIRIDIS_out.file_slots.new("Cam-##_R3_DM2-VIRIDIS")


# connections
nodetree.links.new(node2.outputs[3], nodeR3.inputs[0])

## DM1
nodeR3_nodetree.links.new(nodeR3_in.outputs[0], nodeR3dm1A.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1A.outputs[0], nodeR3dm1B.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1B.outputs[0], nodeR3dm1C.inputs[0])
### DM1-grey
nodeR3_nodetree.links.new(nodeR3dm1A.outputs[0], nodeR3dm1_grey.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1_grey.outputs[0], nodeR3dm1_grey_out.inputs[0])
### DM1-BBR
nodeR3_nodetree.links.new(nodeR3dm1C.outputs[0], nodeR3dm1_BBR.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1_BBR.outputs[0], nodeR3dm1_BBR_out.inputs[0])
### DM1-BVJR
nodeR3_nodetree.links.new(nodeR3dm1C.outputs[0], nodeR3dm1_BVJR.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1_BVJR.outputs[0], nodeR3dm1_BVJR_out.inputs[0])
### DM1-Magma
nodeR3_nodetree.links.new(nodeR3dm1C.outputs[0], nodeR3dm1_MAGMA.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1_MAGMA.outputs[0], nodeR3dm1_MAGMA_out.inputs[0])
### DM1-Spectral
nodeR3_nodetree.links.new(nodeR3dm1C.outputs[0], nodeR3dm1_SPECTRAL.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1_SPECTRAL.outputs[0], nodeR3dm1_SPECTRAL_out.inputs[0])
### DM1-Viridis
nodeR3_nodetree.links.new(nodeR3dm1C.outputs[0], nodeR3dm1_VIRIDIS.inputs[0])
nodeR3_nodetree.links.new(nodeR3dm1_VIRIDIS.outputs[0], nodeR3dm1_VIRIDIS_out.inputs[0])

## DM2
#nodeR3_nodetree.links.new(nodeR3_in.outputs[1], nodeR3dm2A.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2A.outputs[0], nodeR3dm2B.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2B.outputs[0], nodeR3dm2C.inputs[0])
### DM2-grey
#nodeR3_nodetree.links.new(nodeR3dm2A.outputs[0], nodeR3dm2_grey.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2_grey.outputs[0], nodeR3dm2_grey_out.inputs[0])
### DM2-BBR
#nodeR3_nodetree.links.new(nodeR3dm2C.outputs[0], nodeR3dm2_BBR.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2_BBR.outputs[0], nodeR3dm2_BBR_out.inputs[0])
### DM2-BVJR
#nodeR3_nodetree.links.new(nodeR3dm2C.outputs[0], nodeR3dm2_BVJR.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2_BVJR.outputs[0], nodeR3dm2_BVJR_out.inputs[0])
### DM2-Magma
#nodeR3_nodetree.links.new(nodeR3dm2C.outputs[0], nodeR3dm2_MAGMA.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2_MAGMA.outputs[0], nodeR3dm2_MAGMA_out.inputs[0])
### DM2-Spectral
#nodeR3_nodetree.links.new(nodeR3dm2C.outputs[0], nodeR3dm2_SPECTRAL.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2_SPECTRAL.outputs[0], nodeR3dm2_SPECTRAL_out.inputs[0])
### DM2-Viridis
#nodeR3_nodetree.links.new(nodeR3dm2C.outputs[0], nodeR3dm2_VIRIDIS.inputs[0])
#nodeR3_nodetree.links.new(nodeR3dm2_VIRIDIS.outputs[0], nodeR3dm2_VIRIDIS_out.inputs[0])


# ------------------------------------------------------------------
# R4: POINTINESS
# ------------------------------------------------------------------
# adding nodegroup, node R4
nodeR4 = nodetree.nodes.new("CompositorNodeGroup")
nodeR4.location = (400, -220)

# subtree description
nodeR4.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R4: Pointiness")
nodeR4_nodetree = nodeR4.node_tree  # shortcut; akin to `nodetree`

# create input
nodeR4_in = nodeR4_nodetree.nodes.new("NodeGroupInput")
nodeR4_in.location = (0, 0)
nodeR4_nodetree.inputs.new("NodeSocketColor", "Cam-##_R4_POI-100%")
nodeR4_nodetree.inputs.new("NodeSocketColor", "Cam-##_R4_POI-25%")
nodeR4_nodetree.inputs.new("NodeSocketColor", "Cam-##_R4_POI-10%")

# hide input values
for nodeR4_input in nodeR4_nodetree.inputs:
    nodeR4_input.hide_value = True

# inside the group
nodeR4a = nodeR4_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR4a.location = (180, 160)

nodeR4b = nodeR4_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR4b.location = (180, 0)

nodeR4c = nodeR4_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR4c.location = (180, -160)

## File Output
nodeR4z = nodeR4_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR4z.location = (360, 0)
nodeR4z.base_path = "//tmp"
nodeR4z.format.file_format = "JPEG"
nodeR4z.format.color_mode = "BW"
nodeR4z.format.quality = 100
nodeR4z.file_slots[0].path = "Cam-##_R4_POI-100pc"
nodeR4z.file_slots.new("Cam-##_R4_POI-25pc")
nodeR4z.file_slots.new("Cam-##_R4_POI-10pc")

# connections
nodetree.links.new(node2.outputs[4], nodeR4.inputs[0])
nodeR4_nodetree.links.new(nodeR4_in.outputs[0], nodeR4a.inputs[0])
nodeR4_nodetree.links.new(nodeR4_in.outputs[1], nodeR4b.inputs[0])
nodeR4_nodetree.links.new(nodeR4_in.outputs[2], nodeR4c.inputs[0])
nodeR4_nodetree.links.new(nodeR4a.outputs[0], nodeR4z.inputs[0])
nodeR4_nodetree.links.new(nodeR4b.outputs[0], nodeR4z.inputs[1])
nodeR4_nodetree.links.new(nodeR4c.outputs[0], nodeR4z.inputs[2])

# ------------------------------------------------------------------
# R5: ASPECT
# ------------------------------------------------------------------
# adding nodegroup, node R4
nodeR5 = nodetree.nodes.new("CompositorNodeGroup")
nodeR5.location = (400, -360)

# subtree description
nodeR5.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="R5: Aspect")
nodeR5_nodetree = nodeR5.node_tree  # shortcut; akin to `nodetree`

# create inputs
nodeR5_in = nodeR5_nodetree.nodes.new("NodeGroupInput")
nodeR5_in.location = (0, 0)
nodeR5_nodetree.inputs.new("NodeSocketColor", "Cam-##_R4_POI-100%")
nodeR5_nodetree.inputs.new("NodeSocketColor", "Cam-##_R4_POI-25%")
nodeR5_nodetree.inputs.new("NodeSocketColor", "Cam-##_R4_POI-10%")

# hide input values
for nodeR5_input in nodeR5_nodetree.inputs:
    nodeR5_input.hide_value = True

# inside the group
nodeR5a = nodeR5_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR5a.location = (180, 180)

nodeR5b = nodeR5_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR5b.location = (180, 0)

nodeR5c = nodeR5_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR5c.location = (180, -180)

## File Output
nodeR5z = nodeR5_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR5z.location = (360, 0)
nodeR5z.base_path = "//tmp"
nodeR5z.format.file_format = "JPEG"
nodeR5z.format.color_mode = "BW"
nodeR5z.format.quality = 100
nodeR5z.file_slots[0].path = "Cam-##_R5_ASP-100pc"
nodeR5z.file_slots.new("Cam-##_R5_ASP-25pc")
nodeR5z.file_slots.new("Cam-##_R5_ASP-10pc")

# connections
nodetree.links.new(node2.outputs[5], nodeR5.inputs[0])
nodeR5_nodetree.links.new(nodeR5_in.outputs[0], nodeR5a.inputs[0])
nodeR5_nodetree.links.new(nodeR5_in.outputs[1], nodeR5b.inputs[0])
nodeR5_nodetree.links.new(nodeR5_in.outputs[2], nodeR5c.inputs[0])
nodeR5_nodetree.links.new(nodeR5a.outputs[0], nodeR5z.inputs[0])
nodeR5_nodetree.links.new(nodeR5b.outputs[0], nodeR5z.inputs[1])
nodeR5_nodetree.links.new(nodeR5c.outputs[0], nodeR5z.inputs[2])