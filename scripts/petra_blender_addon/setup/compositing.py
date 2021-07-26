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
node1.location = (-300, -200)



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
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeR1a.inputs[0])
nodeR1_nodetree.links.new(nodeR1a.outputs[0], nodeR1zA.inputs[0])


## ---------------------
## B1
## ---------------------




# adding nodegroup, node R6
nodeB1 = nodeR1_nodetree.nodes.new("CompositorNodeGroup")
nodeB1.location = (1000, 1180)

# subtree description
nodeB1.node_tree = bpy.data.node_groups.new(type="CompositorNodeTree", name="B1")
nodeB1_nodetree = nodeB1.node_tree  # shortcut; akin to `nodetree`

# create group's inputs
nodeB1_in = nodeB1_nodetree.nodes.new("NodeGroupInput")
nodeB1_in.location = (0, 0)
nodeB1_nodetree.inputs.new("NodeSocketColor", "input")

# inside the group
nodeB1a = nodeR6_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeB1a.location = (200, 0)

# create group's output
nodeB1_out = nodeB1_nodetree.nodes.new("NodeGroupOutput")
nodeB1_out.location = (1000, 0)
nodeB1_nodetree.outputs.new("NodeSocketColor", "output")



## File Output
nodeB1z = nodeR1_nodetree.nodes.new("CompositorNodeOutputFile")
nodeB1z.location = (1400, 1180)
nodeB1z.base_path = "//tmp"
nodeB1z.format.file_format = "JPEG"
nodeB1z.format.color_mode = "BW"
nodeB1z.format.quality = 100
nodeB1z.file_slots[0].path = "Cam-##_R1_NMC_B1"

# connections
nodeR1_nodetree.links.new(nodeR1_in.outputs[0], nodeB1.inputs[0])
#nodeB1_nodetree.links.new(nodeB1_out.outputs[0], nodeB1z.inputs[0])
#nodeB1_nodetree.links.new(nodeB1a.outputs[0], nodeB1b.inputs[0])






## ---------------------
## B2
## ---------------------


## ---------------------
## Cb1
## ---------------------


## ---------------------
## Cb2
## ---------------------


## ---------------------
## Cr1
## ---------------------


## ---------------------
## Cr2
## ---------------------


## ---------------------
## G1
## ---------------------


## ---------------------
## G2
## ---------------------


## ---------------------
## R1
## ---------------------


## ---------------------
## R2
## ---------------------


## ---------------------
## S1
## ---------------------


## ---------------------
## S2
## ---------------------


## ---------------------
## U1
## ---------------------


## ---------------------
## U2
## ---------------------


## ---------------------
## V1
## ---------------------


## ---------------------
## V2
## ---------------------


## ---------------------
## Y1
## ---------------------


## ---------------------
## Y2
## ---------------------







# connections
nodetree.links.new(node2.outputs[1], nodeR1.inputs[0])


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
# nodeR2_nodetree.links.new(nodeR2Bb.outputs[0], nodeR2z.inputs[1])
# nodeR2_nodetree.links.new(nodeR2Cb.outputs[0], nodeR2z.inputs[2])


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

#-----
## DM1
#-----
nodeR3dm1A = nodeR3_nodetree.nodes.new("CompositorNodeRGBToBW")
nodeR3dm1A.location = (200, 720)   # DM2 y: -620)

nodeR3dm1B = nodeR3_nodetree.nodes.new("CompositorNodeGamma")
nodeR3dm1B.location = (340, 720)   # DM2 y: -620)

nodeR3dm1C = nodeR3_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR3dm1C.location = (520, 720)   # DM2 y: -620)

### DM1-grey
nodeR3dm1_grey = nodeR3_nodetree.nodes.new("CompositorNodeBrightContrast")
nodeR3dm1_grey.location = (800, 1360)   # DM2 y: 0)

nodeR3dm1_grey_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_grey_out.location = (1080, 1360)   # DM2 y: 0)
nodeR3dm1_grey_out.base_path = "//tmp"
nodeR3dm1_grey_out.format.file_format = "PNG"
nodeR3dm1_grey_out.format.color_mode = "RGBA"
nodeR3dm1_grey_out.format.compression = 0
nodeR3dm1_grey_out.file_slots[0].path = "Cam-##_R3_DM1"

### DM1-BBR
nodeR3dm1_BBR = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_BBR.location = (800, 1200)   # DM2 y: -180)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 0000FA)
# cursor2 (loc = 0.425 ; colorHex = 4FF0F0)
# cursor3 (loc = 0.5 ; colorHex = FFFFFF)
# cursor4 (loc = 0.575 ; colorHex = F0F000)
# cursor5 (loc = 1.0 ; colorHex = FF0500)

nodeR3dm1_BBR_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_BBR_out.location = (1080, 1200)   # DM2 y: -180)
nodeR3dm1_BBR_out.base_path = "//tmp"
nodeR3dm1_BBR_out.format.file_format = "JPEG"
nodeR3dm1_BBR_out.format.color_mode = "RGB"
nodeR3dm1_BBR_out.format.quality = 100
nodeR3dm1_BBR_out.file_slots[0].path = "Cam-##_R3_DM1-BBR"

### DM1-BVJR
nodeR3dm1_BVJR = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_BVJR.location = (800, 960)   # DM2 y: -400)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 0000FF)
# cursor2 (loc = 0.4 ; colorHex = 00CC00)
# cursor3 (loc = 0.6 ; colorHex = FFFF00)
# cursor4 (loc = 1.0 ; colorHex = FF0000)

nodeR3dm1_BVJR_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_BVJR_out.location = (1080, 960)   # DM2 y: -400)
nodeR3dm1_BVJR_out.base_path = "//tmp"
nodeR3dm1_BVJR_out.format.file_format = "JPEG"
nodeR3dm1_BVJR_out.format.color_mode = "RGB"
nodeR3dm1_BVJR_out.format.quality = 100
nodeR3dm1_BVJR_out.file_slots[0].path = "Cam-##_R3_DM1-BVJR"

### DM1-Magma
nodeR3dm1_MAGMA = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_MAGMA.location = (800, 720)   # DM2 y: -620)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.25 ; colorHex = 50127B)
# cursor3 (loc = 0.5 ; colorHex = B63679)
# cursor4 (loc = 0.75 ; colorHex = FC8761)
# cursor5 (loc = 1.0 ; colorHex = FCFDBF)

nodeR3dm1_MAGMA_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_MAGMA_out.location = (1080, 720)   # DM2 y: -620)
nodeR3dm1_MAGMA_out.base_path = "//tmp"
nodeR3dm1_MAGMA_out.format.file_format = "JPEG"
nodeR3dm1_MAGMA_out.format.color_mode = "RGB"
nodeR3dm1_MAGMA_out.format.quality = 100
nodeR3dm1_MAGMA_out.file_slots[0].path = "Cam-##_R3_DM1-MAGMA"

### DM1-Spectral
nodeR3dm1_SPECTRAL = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_SPECTRAL.location = (800, 480)   # DM2 y: -840)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.25 ; colorHex = 50127B)
# cursor3 (loc = 0.5 ; colorHex = B63679)
# cursor4 (loc = 0.75 ; colorHex = FC8761)
# cursor5 (loc = 1.0 ; colorHex = FCFDBF)

nodeR3dm1_SPECTRAL_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_SPECTRAL_out.location = (1080, 480)   # DM2 y: -840)
nodeR3dm1_SPECTRAL_out.base_path = "//tmp"
nodeR3dm1_SPECTRAL_out.format.file_format = "JPEG"
nodeR3dm1_SPECTRAL_out.format.color_mode = "RGB"
nodeR3dm1_SPECTRAL_out.format.quality = 100
nodeR3dm1_SPECTRAL_out.file_slots[0].path = "Cam-##_R3_DM1-SPECTRAL"


### DM1-Viridis
nodeR3dm1_VIRIDIS = nodeR3_nodetree.nodes.new("CompositorNodeValToRGB")
nodeR3dm1_VIRIDIS.location = (800, 240)   # DM2 y: -1060)
# interpolation: B-Spline
# cursor1 (loc = 0.0 ; colorHex = 000000)
# cursor2 (loc = 0.25 ; colorHex = 50127B)
# cursor3 (loc = 0.5 ; colorHex = B63679)
# cursor4 (loc = 0.75 ; colorHex = FC8761)
# cursor5 (loc = 1.0 ; colorHex = FCFDBF)

nodeR3dm1_VIRIDIS_out = nodeR3_nodetree.nodes.new("CompositorNodeOutputFile")
nodeR3dm1_VIRIDIS_out.location = (1080, 240)   # DM2 y: -1060)
nodeR3dm1_VIRIDIS_out.base_path = "//tmp"
nodeR3dm1_VIRIDIS_out.format.file_format = "JPEG"
nodeR3dm1_VIRIDIS_out.format.color_mode = "RGB"
nodeR3dm1_VIRIDIS_out.format.quality = 100
nodeR3dm1_VIRIDIS_out.file_slots[0].path = "Cam-##_R3_DM1-VIRIDIS"


#-----
## DM2
#-----
# The same, just change "R3dm1" to R3dm2", and y positions


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