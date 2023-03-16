import bpy

C = bpy.context
D = bpy.data

# Create a new material
R4 = D.materials.new(name='R4_POI')
R4.use_nodes = True
nt = R4.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Color attribute
input1 = nt.nodes.new("ShaderNodeNewGeometry")
input1.location = (0, 0)
input1.label = "geometry"
input1.name = "geometry"

# Color ramp
input2 = nt.nodes.new("ShaderNodeValToRGB")
input2.location = (200, 0)
input2.label = "colorRamp"
input2.name = "colorRamp"
input2.color_ramp.elements[0].position = 0.47
input2.color_ramp.elements[1].position = 0.53

# Gamma
input3 = nt.nodes.new("ShaderNodeGamma")
input3.location = (500, 0)
input3.label = "gamma"
input3.name = "gamma"
input3.inputs[1].default_value = 2.3

# Bright/Contrast
input4 = nt.nodes.new("ShaderNodeBrightContrast")
input4.location = (700, 0)
input4.label = "bright_contrast"
input4.name = "bright_contrast"
input4.inputs[1].default_value = 0.5
input4.inputs[2].default_value = 1.2

# Emission 1
input5 = nt.nodes.new("ShaderNodeEmission")
input5.location = (900, 0)
input5.label = "emission1"
input5.name = "emission1"

# Emission 2
input6 = nt.nodes.new("ShaderNodeEmission")
input6.location = (900, -120)
input6.label = "emission2"
input6.name = "emission2"

# Mix
input7 = nt.nodes.new("ShaderNodeMixShader")
input7.location = (1100, 0)
input7.label = "mix"
input7.name = "mix"

# Material output
input8 = nt.nodes.new("ShaderNodeOutputMaterial")
input8.location = (1300, 0)
input8.label = "output"
input8.name = "output"

# ---------------------------------------------
# links
nt.links.new(input1.outputs[7], input2.inputs[0])
nt.links.new(input1.outputs[6], input7.inputs[0])
nt.links.new(input2.outputs[0], input3.inputs[0])
nt.links.new(input3.outputs[0], input4.inputs[0])
nt.links.new(input4.outputs[0], input5.inputs[0])
nt.links.new(input5.outputs[0], input7.inputs[1])
nt.links.new(input6.outputs[0], input7.inputs[2])
nt.links.new(input7.outputs[0], input8.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["R4_POI"].use_fake_user = True
