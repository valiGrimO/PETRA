import bpy

C = bpy.context
D = bpy.data

# Create a new material
R1 = D.materials.new(name='R1_NMC')
R1.use_nodes = True
nt = R1.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Color attribute
input1 = nt.nodes.new("ShaderNodeTexCoord")
input1.location = (0, 0)
input1.label = "TexCoord"
input1.name = "TexCoord"

input2 = nt.nodes.new("ShaderNodeVectorTransform")
input2.location = (200, 100)
input2.label = "vecTrans"
input2.name = "vecTrans"
input2.vector_type = "NORMAL"
input2.convert_from = 'OBJECT'
input2.convert_to = 'CAMERA'

input3 = nt.nodes.new("ShaderNodeValue")
input3.location = (200, -80)
input3.label = "value1"
input3.name = "value1"
input3.outputs[0].default_value = 0.5

input4 = nt.nodes.new("ShaderNodeValue")
input4.location = (200, -180)
input4.label = "value2"
input4.name = "value2"
input4.outputs[0].default_value = 0

input5 = nt.nodes.new("ShaderNodeValue")
input5.location = (200, -280)
input5.label = "value3"
input5.name = "value3"
input5.outputs[0].default_value = 0.49

input6 = nt.nodes.new("ShaderNodeMapping")
input6.location = (600, 200)
input6.label = "mapping1"
input6.name = "mapping1"

input7 = nt.nodes.new("ShaderNodeMapping")
input7.location = (600, 0)
input7.label = "mapping2"
input7.name = "mapping2"

input8 = nt.nodes.new("ShaderNodeMapping")
input8.location = (600, -200)
input8.label = "mapping3"
input8.name = "mapping3"
input8.inputs[1].default_value[2] = 0.5

input9 = nt.nodes.new("ShaderNodeSeparateXYZ")
input9.location = (800, 0)
input9.label = "sepXYZ"
input9.name = "sepXYZ"

input10 = nt.nodes.new("ShaderNodeCombineXYZ")
input10.location = (1000, 0)
input10.label = "combXYZ"
input10.name = "combXYZ"

input11 = nt.nodes.new("ShaderNodeTexGradient")
input11.location = (1200, 200)
input11.label = "texGradient1"
input11.name = "texGradient1"
input11.gradient_type = "QUADRATIC"

input12 = nt.nodes.new("ShaderNodeTexGradient")
input12.location = (1200, 0)
input12.label = "texGradient2"
input12.name = "texGradient2"
input12.gradient_type = "QUADRATIC"

input13 = nt.nodes.new("ShaderNodeTexGradient")
input13.location = (1200, -200)
input13.label = "texGradient3"
input13.name = "texGradient3"
input13.gradient_type = "SPHERICAL"

input14 = nt.nodes.new("ShaderNodeCombineRGB")
input14.location = (1400, 0)

# Shader Emission1
input15 = nt.nodes.new("ShaderNodeEmission")
input15.location = (1600, 0)
input15.label = "emission1"
input15.name = "emission1"

# Shader Emission
input16 = nt.nodes.new("ShaderNodeEmission")
input16.location = (1600, -120)
input16.label = "emission2"
input16.name = "emission2"

# Input geometry
input17 = nt.nodes.new("ShaderNodeNewGeometry")
input17.location = (1600, 240)
input17.label = "inputGeometry"
input17.name = "inputGeometry"

# Mix shader
input18 = nt.nodes.new("ShaderNodeMixShader")
input18.location = (1800, 0)

# Output
input19 = nt.nodes.new("ShaderNodeOutputMaterial")
input19.location = (2000, 0)

# ---------------------------------------------
# links
nt.links.new(input1.outputs[1], input2.inputs[0])
nt.links.new(input2.outputs[0], input6.inputs[0])
nt.links.new(input2.outputs[0], input7.inputs[0])
nt.links.new(input2.outputs[0], input8.inputs[0])
nt.links.new(input3.outputs[0], input6.inputs[1])
nt.links.new(input3.outputs[0], input7.inputs[1])
nt.links.new(input4.outputs[0], input6.inputs[2])
nt.links.new(input4.outputs[0], input7.inputs[2])
nt.links.new(input4.outputs[0], input8.inputs[2])
nt.links.new(input5.outputs[0], input6.inputs[3])
nt.links.new(input5.outputs[0], input7.inputs[3])
nt.links.new(input5.outputs[0], input8.inputs[3])
nt.links.new(input6.outputs[0], input11.inputs[0])
nt.links.new(input7.outputs[0], input9.inputs[0])
nt.links.new(input8.outputs[0], input13.inputs[0])
nt.links.new(input9.outputs[0], input10.inputs[1])
nt.links.new(input9.outputs[1], input10.inputs[0])
nt.links.new(input9.outputs[2], input10.inputs[2])
nt.links.new(input10.outputs[0], input12.inputs[0])
nt.links.new(input11.outputs[0], input14.inputs[0])
nt.links.new(input12.outputs[0], input14.inputs[1])
nt.links.new(input13.outputs[0], input14.inputs[2])
nt.links.new(input14.outputs[0], input15.inputs[0])
nt.links.new(input15.outputs[0], input18.inputs[1])
nt.links.new(input16.outputs[0], input18.inputs[2])
nt.links.new(input17.outputs[6], input18.inputs[0])
nt.links.new(input18.outputs[0], input19.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["R1_NMC"].use_fake_user = True
