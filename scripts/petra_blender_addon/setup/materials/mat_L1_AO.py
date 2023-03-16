import bpy

C = bpy.context
D = bpy.data

# Create a new material
L1 = D.materials.new(name='L1_AO')
L1.use_nodes = True
nt = L1.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Texture coordinate
input1 = nt.nodes.new("ShaderNodeAmbientOcclusion")
input1.location = (0, 0)
input1.label = "AO_input"
input1.name = "AO_input"

# Multiply
input2 = nt.nodes.new("ShaderNodeMath")
input2.location = (200, 0)
input2.label = "math1"
input2.name = "math1"
input2.operation = "MULTIPLY"
input2.inputs[1].default_value = 0.8

# Add
input3 = nt.nodes.new("ShaderNodeMath")
input3.location = (400, 0)
input3.label = "math2"
input3.name = "math2"
input3.operation = "ADD"
input3.inputs[1].default_value = 0.2

# Bright/Contrast
input4 = nt.nodes.new("ShaderNodeBrightContrast")
input4.location = (600,0)
input4.label = "Brigth_Contrast"
input4.name = "Brigth_Contrast"
input4.inputs[1].default_value = -1
input4.inputs[2].default_value = 1.5

# Shader Emission1
input5 = nt.nodes.new("ShaderNodeEmission")
input5.location = (800, 0)
input5.label = "emission1"
input5.name = "emission1"

# Shader Emission2
input6 = nt.nodes.new("ShaderNodeEmission")
input6.location = (800, -120)
input6.label = "emission2"
input6.name = "emission2"

# Input geometry
input7 = nt.nodes.new("ShaderNodeNewGeometry")
input7.location = (800, 240)
input7.label = "inputGeometry"
input7.name = "inputGeometry"

# Mix shader
input8 = nt.nodes.new("ShaderNodeMixShader")
input8.location = (1000, 0)

# Output
input9 = nt.nodes.new("ShaderNodeOutputMaterial")
input9.location = (1200, 0)

# ---------------------------------------------
# links
nt.links.new(input1.outputs[1], input2.inputs[0])
nt.links.new(input2.outputs[0], input3.inputs[0])
nt.links.new(input3.outputs[0], input4.inputs[0])
nt.links.new(input4.outputs[0], input5.inputs[0])
nt.links.new(input5.outputs[0], input8.inputs[1])
nt.links.new(input6.outputs[0], input8.inputs[2])
nt.links.new(input7.outputs[6], input8.inputs[0])
nt.links.new(input8.outputs[0], input9.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["L1_AO"].use_fake_user = True
