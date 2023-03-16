import bpy

C = bpy.context
D = bpy.data

# Create a new material
H2 = D.materials.new(name='H2_OBN')
H2.use_nodes = True
nt = H2.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Texture coordinate
input1 = nt.nodes.new("ShaderNodeTexCoord")
input1.location = (0, 0)
input1.label = "TexCoordinate"
input1.name = "TexCoordinate"

# Texture invert1
input2 = nt.nodes.new("ShaderNodeInvert")
input2.location = (200, -60)
input2.label = "invert1"
input2.name = "invert1"

# Texture invert2
input3 = nt.nodes.new("ShaderNodeInvert")
input3.location = (200, -180)
input3.label = "invert2"
input3.name = "invert2"

# Mix - différence1
input4 = nt.nodes.new("ShaderNodeMixRGB")
input4.location = (400, -60)
input4.label = "difference1"
input4.name = "difference1"
input4.blend_type = "DIFFERENCE"

# Mix - différence2
input5 = nt.nodes.new("ShaderNodeMixRGB")
input5.location = (600, 100)
input5.label = "difference2"
input5.name = "difference2"
input4.blend_type = "DIFFERENCE"

# Shader Emission1
input6 = nt.nodes.new("ShaderNodeEmission")
input6.location = (800, 100)
input6.label = "emission1"
input6.name = "emission1"

# Shader Emission
input7 = nt.nodes.new("ShaderNodeEmission")
input7.location = (800, -20)
input7.label = "emission2"
input7.name = "emission2"

# Input geometry
input8 = nt.nodes.new("ShaderNodeNewGeometry")
input8.location = (800, 340)
input8.label = "inputGeometry"
input8.name = "inputGeometry"

# Mix shader
input9 = nt.nodes.new("ShaderNodeMixShader")
input9.location = (1000, 100)

# Output
input10 = nt.nodes.new("ShaderNodeOutputMaterial")
input10.location = (1200, 100)

# ---------------------------------------------
# links
nt.links.new(input1.outputs[0], input5.inputs[1])
nt.links.new(input1.outputs[1], input2.inputs[1])
nt.links.new(input1.outputs[2], input3.inputs[1])
nt.links.new(input2.outputs[0], input4.inputs[1])
nt.links.new(input3.outputs[0], input4.inputs[2])
nt.links.new(input4.outputs[0], input5.inputs[2])
nt.links.new(input5.outputs[0], input6.inputs[0])
nt.links.new(input6.outputs[0], input9.inputs[1])
nt.links.new(input8.outputs[6], input9.inputs[0])
nt.links.new(input7.outputs[0], input9.inputs[2])
nt.links.new(input9.outputs[0], input10.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["H2_OBN"].use_fake_user = True
