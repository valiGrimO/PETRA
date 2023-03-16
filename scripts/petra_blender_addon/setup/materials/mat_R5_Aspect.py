import bpy

C = bpy.context
D = bpy.data

# Create a new material
R5 = D.materials.new(name='R5_ASP')
R5.use_nodes = True
nt = R5.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Color attribute
input1 = nt.nodes.new("ShaderNodeTexCoord")
input1.location = (0, 0)
input1.label = "texCoord"
input1.name = "texCoord"

# Vector transform
input2 = nt.nodes.new("ShaderNodeVectorTransform")
input2.location = (200, 0)
input2.label = "vecTrans"
input2.name = "vecTrans"
input2.vector_type = "NORMAL"
input2.convert_from = "OBJECT"
input2.convert_to = "CAMERA"

# Separate XYZ
input3 = nt.nodes.new("ShaderNodeSeparateXYZ")
input3.location = (400, 0)
input3.label = "sepXYZ"
input3.name = "sepXYZ"

# Math 1
input4 = nt.nodes.new("ShaderNodeMath")
input4.location = (700, 300)
input4.label = "x negative?"
input4.name = "math1"
input4.operation = "LESS_THAN"
input4.inputs[1].default_value = 0

# Math 2
input5 = nt.nodes.new("ShaderNodeMath")
input5.location = (700, 120)
input5.label = "y positive?"
input5.name = "math2"
input5.operation = "GREATER_THAN"
input5.inputs[1].default_value = 0

# Math 3
input6 = nt.nodes.new("ShaderNodeMath")
input6.location = (900, 300)
input6.label = "Multiply"
input6.name = "math3"
input6.operation = "MULTIPLY"

# Math 4
input7 = nt.nodes.new("ShaderNodeMath")
input7.location = (1100, 300)
input7.label = "Multiply"
input7.name = "math4"
input7.operation = "MULTIPLY"
input7.inputs[1].default_value = 360

# Math 5
input8 = nt.nodes.new("ShaderNodeMath")
input8.location = (900, 60)
input8.label = "y negative?"
input8.name = "math5"
input8.operation = "LESS_THAN"
input8.inputs[1].default_value = 0

# Math 6
input9 = nt.nodes.new("ShaderNodeMath")
input9.location = (1100, 60)
input9.label = "multiply"
input9.name = "math6"
input9.operation = "MULTIPLY"
input9.inputs[1].default_value = 180

# Math 7
input10 = nt.nodes.new("ShaderNodeMath")
input10.location = (1300, 60)
input10.label = "multiply"
input10.name = "math7"
input10.operation = "ADD"

# Math 8
input11 = nt.nodes.new("ShaderNodeMath")
input11.location = (700, -120)
input11.label = "divide"
input11.name = "math8"
input11.operation = "DIVIDE"

# Math 9
input12 = nt.nodes.new("ShaderNodeMath")
input12.location = (900, -120)
input12.label = "aspect radians"
input12.name = "math9"
input12.operation = "ARCTANGENT"

# Math 10
input13 = nt.nodes.new("ShaderNodeMath")
input13.location = (1100, -120)
input13.label = "aspect degrees"
input13.name = "math10"
input13.operation = "MULTIPLY"
input13.inputs[1].default_value = 57.2958

# Math 11
input14 = nt.nodes.new("ShaderNodeMath")
input14.location = (1500, 300)
input14.label = "add"
input14.name = "math11"
input14.operation = "ADD"

# Math 12
input15 = nt.nodes.new("ShaderNodeMath")
input15.location = (1700, 300)
input15.label = "normalize"
input15.name = "math12"
input15.operation = "DIVIDE"
input15.inputs[1].default_value = 360

# Color Ramp
input16 = nt.nodes.new("ShaderNodeValToRGB")
input16.location = (1900, 300)
input16.label = "colorRamp"
input16.name = "colorRamp"
input16.color_ramp.interpolation = "CONSTANT"
input16.color_ramp.elements[0].position = 0
input16.color_ramp.elements[0].color = (1, 0, 0, 1)
input16.color_ramp.elements[1].position = 0.0625
input16.color_ramp.elements[1].color = (1, 0.5, 0, 1)
input16.color_ramp.elements.new(0.1875)
input16.color_ramp.elements[2].color = (1, 1, 0, 1)
input16.color_ramp.elements.new(0.3125)
input16.color_ramp.elements[3].color = (0, 1, 0, 1)
input16.color_ramp.elements.new(0.4375)
input16.color_ramp.elements[4].color = (0, 1, 1, 1)
input16.color_ramp.elements.new(0.5625)
input16.color_ramp.elements[5].color = (0, 0.5, 1, 1)
input16.color_ramp.elements.new(0.6875)
input16.color_ramp.elements[6].color = (0, 0, 1, 1)
input16.color_ramp.elements.new(0.8125)
input16.color_ramp.elements[7].color = (1, 0, 1, 1)
input16.color_ramp.elements.new(0.9375)
input16.color_ramp.elements[8].color = (1, 0, 0, 1)

# Shader Emission1
input17 = nt.nodes.new("ShaderNodeEmission")
input17.location = (2200, 300)
input17.label = "emission1"
input17.name = "emission1"

# Shader Emission
input18 = nt.nodes.new("ShaderNodeEmission")
input18.location = (2200, 180)
input18.label = "emission2"
input18.name = "emission2"

# Input geometry
input19 = nt.nodes.new("ShaderNodeNewGeometry")
input19.location = (2200, 540)
input19.label = "inputGeometry"
input19.name = "inputGeometry"

# Mix shader
input20 = nt.nodes.new("ShaderNodeMixShader")
input20.location = (2400, 300)

# Output
input21 = nt.nodes.new("ShaderNodeOutputMaterial")
input21.location = (2600, 300)

# ---------------------------------------------
# links
nt.links.new(input1.outputs[1], input2.inputs[0])
nt.links.new(input2.outputs[0], input3.inputs[0])
nt.links.new(input3.outputs[0], input4.inputs[0])
nt.links.new(input3.outputs[1], input5.inputs[0])
nt.links.new(input3.outputs[1], input8.inputs[0])
nt.links.new(input3.outputs[0], input11.inputs[0])
nt.links.new(input3.outputs[1], input11.inputs[1])
nt.links.new(input4.outputs[0], input6.inputs[0])
nt.links.new(input5.outputs[0], input6.inputs[1])
nt.links.new(input6.outputs[0], input7.inputs[0])
nt.links.new(input7.outputs[0], input14.inputs[0])
nt.links.new(input8.outputs[0], input9.inputs[0])
nt.links.new(input9.outputs[0], input10.inputs[0])
nt.links.new(input10.outputs[0], input14.inputs[1])
nt.links.new(input11.outputs[0], input12.inputs[0])
nt.links.new(input12.outputs[0], input13.inputs[0])
nt.links.new(input13.outputs[0], input10.inputs[1])
nt.links.new(input14.outputs[0], input15.inputs[0])
nt.links.new(input15.outputs[0], input16.inputs[0])
nt.links.new(input16.outputs[0], input17.inputs[0])
nt.links.new(input17.outputs[0], input20.inputs[1])
nt.links.new(input18.outputs[0], input20.inputs[2])
nt.links.new(input19.outputs[6], input20.inputs[0])
nt.links.new(input20.outputs[0], input21.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["R5_ASP"].use_fake_user = True
