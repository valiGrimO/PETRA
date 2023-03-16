import bpy

C = bpy.context
D = bpy.data

# Create a new material
R2 = D.materials.new(name='R2_CL')
R2.use_nodes = True
nt = R2.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Input Value
input1 = nt.nodes.new("ShaderNodeValue")
input1.location = (0, 0)
input1.label = "... mm"
input1.name = "value"
input1.outputs[0].default_value = 2

# Math1 - x2
input2 = nt.nodes.new("ShaderNodeMath")
input2.location = (200, 0)
input2.label = "x1"
input2.name = "math1"
input2.operation = 'DIVIDE'
input2.inputs[0].default_value = 200

# Math2 - x5
input3 = nt.nodes.new("ShaderNodeMath")
input3.location = (400, 0)
input3.label = "x5"
input3.name = "math2"
input3.operation = 'DIVIDE'
input3.inputs[1].default_value = 5

# Math3 - x10
input4 = nt.nodes.new("ShaderNodeMath")
input4.location = (600, 0)
input4.label = "x10"
input4.name = "math3"
input4.operation = 'DIVIDE'
input4.inputs[1].default_value = 2

# Texture Coordinate
input5 = nt.nodes.new("ShaderNodeTexCoord")
input5.location = (400, 280)
input5.label = "texCoord"
input5.name = "texCoord"

# Vector Transform
input6 = nt.nodes.new("ShaderNodeVectorTransform")
input6.location = (600, 200)
input6.label = "vecTransform"
input6.name = "vecTransform"
input6.convert_from = 'CAMERA'
input6.convert_to = 'CAMERA'

# Mapping
input7 = nt.nodes.new("ShaderNodeMapping")
input7.location = (800, 200)
input7.label = "mapping"
input7.name = "mapping"
input7.inputs[2].default_value[1] = 1.5708

# separate XYZ
input8 = nt.nodes.new("ShaderNodeSeparateXYZ")
input8.location = (1000, 200)
input8.label = "sepXYZ"
input8.name = "sepXYZ"

# checker texture
input9 = nt.nodes.new("ShaderNodeTexChecker")
input9.location = (1200, 200)
input9.label = "texChecker"
input9.name = "texChecker"
input9.inputs[2].default_value = (0, 0, 0, 1)

# Shader Emission1
input10 = nt.nodes.new("ShaderNodeEmission")
input10.location = (1400, 200)
input10.label = "emission1"
input10.name = "emission1"

# Shader Emission
input11 = nt.nodes.new("ShaderNodeEmission")
input11.location = (1400, 80)
input11.label = "emission2"
input11.name = "emission2"

# Input geometry
input12 = nt.nodes.new("ShaderNodeNewGeometry")
input12.location = (1400, 440)
input12.label = "inputGeometry"
input12.name = "inputGeometry"

# Mix shader
input13 = nt.nodes.new("ShaderNodeMixShader")
input13.location = (1600, 200)
input13.label = "mixShader"
input13.name = "mixShader"

# Output CL1
input14 = nt.nodes.new("ShaderNodeOutputMaterial")
input14.location = (1800, 340)
input14.label = "CL1"
input14.name = "CL1"

# Output CL2
input15 = nt.nodes.new("ShaderNodeOutputMaterial")
input15.location = (1800, 200)
input15.label = "CL2"
input15.name = "CL2"

# Output CL3
input16 = nt.nodes.new("ShaderNodeOutputMaterial")
input16.location = (1800, 60)
input16.label = "CL3"
input16.name = "CL3"

# ---------------------------------------------
# links
nt.links.new(input1.outputs[0], input2.inputs[1])
nt.links.new(input2.outputs[0], input3.inputs[0])
nt.links.new(input3.outputs[0], input4.inputs[0])
nt.links.new(input4.outputs[0], input7.inputs[3])
nt.links.new(input5.outputs[4], input6.inputs[0])
nt.links.new(input6.outputs[0], input7.inputs[0])
nt.links.new(input7.outputs[0], input8.inputs[0])
nt.links.new(input8.outputs[0], input9.inputs[0])
nt.links.new(input9.outputs[0], input10.inputs[0])
nt.links.new(input10.outputs[0], input13.inputs[1])
nt.links.new(input11.outputs[0], input13.inputs[2])
nt.links.new(input12.outputs[6], input13.inputs[0])
nt.links.new(input13.outputs[0], input14.inputs[0])
nt.links.new(input13.outputs[0], input15.inputs[0])
nt.links.new(input13.outputs[0], input16.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["R2_CL"].use_fake_user = True
