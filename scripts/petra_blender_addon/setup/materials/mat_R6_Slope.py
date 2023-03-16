import bpy

C = bpy.context
D = bpy.data

# Create a new material
R6 = D.materials.new(name='R6_SLO')
R6.use_nodes = True
nt = R6.node_tree
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

# Mapping
input3 = nt.nodes.new("ShaderNodeMapping")
input3.location = (400, 0)
input3.label = "mapping"
input3.name = "mapping"
input3.inputs[2].default_value[1] = -1.5708


# Separate XYZ
input4 = nt.nodes.new("ShaderNodeSeparateXYZ")
input4.location = (600, 0)
input4.label = "sepXYZ"
input4.name = "sepXYZ"

# Math1 - Arccosine
input5 = nt.nodes.new("ShaderNodeMath")
input5.location = (800, 0)
input5.label = "Arccosine"
input5.name = "math1"
input5.operation = 'ARCCOSINE'

# Math2 - Radians to Degrees
input6 = nt.nodes.new("ShaderNodeMath")
input6.location = (1000, 0)
input6.label = "Radians to Degrees"
input6.name = "math2"
input6.operation = 'MULTIPLY'
input6.inputs[1].default_value = 57.2958

# Math3 - Normalize
input7 = nt.nodes.new("ShaderNodeMath")
input7.location = (1200, 0)
input7.label = "Normalize"
input7.name = "math3"
input7.operation = 'DIVIDE'
input7.inputs[1].default_value = 100

# Color Ramp
input8 = nt.nodes.new("ShaderNodeValToRGB")
input8.location = (1400, 0)
input8.label = "colorRamp"
input8.name = "colorRamp"
input8.color_ramp.interpolation = "EASE"
input8.color_ramp.elements[0].position = 0
input8.color_ramp.elements[0].color = (0, 0, 0, 1)
input8.color_ramp.elements[1].position = 0.5
input8.color_ramp.elements[1].color = (1, 1, 1, 1)

# Shader Emission1
input9 = nt.nodes.new("ShaderNodeEmission")
input9.location = (1700, 0)
input9.label = "emission1"
input9.name = "emission1"

# Shader Emission
input10 = nt.nodes.new("ShaderNodeEmission")
input10.location = (1700, -120)
input10.label = "emission2"
input10.name = "emission2"

# Input geometry
input11 = nt.nodes.new("ShaderNodeNewGeometry")
input11.location = (1700, 240)
input11.label = "inputGeometry"
input11.name = "inputGeometry"

# Mix shader
input12 = nt.nodes.new("ShaderNodeMixShader")
input12.location = (1900, 0)

# Output
input13 = nt.nodes.new("ShaderNodeOutputMaterial")
input13.location = (2100, 0)

# ---------------------------------------------
# links
nt.links.new(input1.outputs[1], input2.inputs[0])
nt.links.new(input2.outputs[0], input3.inputs[0])
nt.links.new(input3.outputs[0], input4.inputs[0])
nt.links.new(input4.outputs[0], input5.inputs[0])
nt.links.new(input5.outputs[0], input6.inputs[0])
nt.links.new(input6.outputs[0], input7.inputs[0])
nt.links.new(input7.outputs[0], input8.inputs[0])
nt.links.new(input8.outputs[0], input9.inputs[0])
nt.links.new(input9.outputs[0], input12.inputs[1])
nt.links.new(input10.outputs[0], input12.inputs[2])
nt.links.new(input11.outputs[6], input12.inputs[0])
nt.links.new(input12.outputs[0], input13.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["R6_SLO"].use_fake_user = True
