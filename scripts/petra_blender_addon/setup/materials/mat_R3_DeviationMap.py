import bpy

C = bpy.context
D = bpy.data

# Create a new material
R3 = D.materials.new(name='R3_DM')
R3.use_nodes = True
nt = R3.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Color attribute
input1 = nt.nodes.new("ShaderNodeVertexColor")
input1.location = (0, 0)
input1.label = "inputColor"
input1.name = "inputColor"

input2 = nt.nodes.new("ShaderNodeSeparateRGB")
input2.location = (200, 0)
input2.label = "sepRGB"
input2.name = "sepRGB"

input3 = nt.nodes.new("ShaderNodeMath")
input3.location = (400, 100)
input3.label = "multiply1"
input3.name = "multiply1"
input3.operation = "MULTIPLY"
input3.inputs[0].default_value = -1

input4 = nt.nodes.new("ShaderNodeMath")
input4.location = (600, 0)
input4.label = "add1"
input4.name = "add1"
input4.operation = "ADD"

input5 = nt.nodes.new("ShaderNodeMath")
input5.location = (800, 0)
input5.label = "add2"
input5.name = "add2"
input5.operation = "ADD"
input5.inputs[1].default_value = 1

input6 = nt.nodes.new("ShaderNodeMath")
input6.location = (1000, 0)
input6.label = "multiply2"
input6.name = "multiply2"
input6.operation = "MULTIPLY"
input6.inputs[1].default_value = 0.5

input7 = nt.nodes.new("ShaderNodeValToRGB")
input7.location = (1200, 0)
input7.label = "colorRamp"
input7.name = "colorRamp"
input7.color_ramp.elements[0].position = 0
input7.color_ramp.elements[0].color = (1, 0, 0, 1)
input7.color_ramp.elements[1].position = 0.01
input7.color_ramp.elements[1].color = (1, 1, 1, 1)
input7.color_ramp.elements.new(0.99)
input7.color_ramp.elements[2].color = (0, 0, 0, 1)
input7.color_ramp.elements.new(1)
input7.color_ramp.elements[3].color = (1, 0, 0, 1)

# Shader Emission1
input8 = nt.nodes.new("ShaderNodeEmission")
input8.location = (1500, 0)
input8.label = "emission1"
input8.name = "emission1"

# Shader Emission
input9 = nt.nodes.new("ShaderNodeEmission")
input9.location = (1500, -120)
input9.label = "emission2"
input9.name = "emission2"

# Input geometry
input10 = nt.nodes.new("ShaderNodeNewGeometry")
input10.location = (1500, 240)
input10.label = "inputGeometry"
input10.name = "inputGeometry"

# Mix shader
input11 = nt.nodes.new("ShaderNodeMixShader")
input11.location = (1700, 0)

# Output
input12 = nt.nodes.new("ShaderNodeOutputMaterial")
input12.location = (1900, 0)

# ---------------------------------------------
# links
nt.links.new(input1.outputs[0], input2.inputs[0])
nt.links.new(input2.outputs[0], input3.inputs[1])
nt.links.new(input2.outputs[1], input4.inputs[1])
nt.links.new(input3.outputs[0], input4.inputs[0])
nt.links.new(input4.outputs[0], input5.inputs[0])
nt.links.new(input5.outputs[0], input6.inputs[0])
nt.links.new(input6.outputs[0], input7.inputs[0])
nt.links.new(input7.outputs[0], input8.inputs[0])
nt.links.new(input8.outputs[0], input11.inputs[1])
nt.links.new(input9.outputs[0], input11.inputs[2])
nt.links.new(input10.outputs[6], input11.inputs[0])
nt.links.new(input11.outputs[0], input12.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["R3_DM"].use_fake_user = True
