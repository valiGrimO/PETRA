import bpy

C = bpy.context
D = bpy.data

# Create a new material
H1 = D.materials.new(name='H1_Masks')
H1.use_nodes = True
nt = H1.node_tree
for node in nt.nodes:
    nt.nodes.remove(node)

# ---------------------------------------------
# Shader Emission1
input2 = nt.nodes.new("ShaderNodeEmission")
input2.location = (200, 0)
input2.label = "emission1"
input2.name = "emission1"
input2.inputs[0].default_value = (0, 0, 1, 1)

# Shader Emission
input3 = nt.nodes.new("ShaderNodeEmission")
input3.location = (200, -120)
input3.label = "emission2"
input3.name = "emission2"
input3.inputs[0].default_value = (1, 0, 0, 1)

# Input geometry
input4 = nt.nodes.new("ShaderNodeNewGeometry")
input4.location = (200, 240)
input4.label = "inputGeometry"
input4.name = "inputGeometry"

# Mix shader
input5 = nt.nodes.new("ShaderNodeMixShader")
input5.location = (400, 0)

# Output
input6 = nt.nodes.new("ShaderNodeOutputMaterial")
input6.location = (600, 0)

# ---------------------------------------------
# links
nt.links.new(input4.outputs[6], input5.inputs[0])
nt.links.new(input2.outputs[0], input5.inputs[1])
nt.links.new(input3.outputs[0], input5.inputs[2])
nt.links.new(input5.outputs[0], input6.inputs[0])

# ---------------------------------------------
# Set it as Fake user
D.materials["H1_Masks"].use_fake_user = True
