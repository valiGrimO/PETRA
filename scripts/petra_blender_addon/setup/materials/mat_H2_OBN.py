import bpy

# MATERIAL
h2_obn = bpy.data.materials.new(name='h2_obn')
h2_obn.use_nodes = True
node_tree0 = h2_obn.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
if hasattr(material_output_0, 'active_preview'):
    material_output_0.active_preview = False
if hasattr(material_output_0, 'color'):
    material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(material_output_0, 'hide'):
    material_output_0.hide = False
if hasattr(material_output_0, 'is_active_output'):
    material_output_0.is_active_output = True
if hasattr(material_output_0, 'location'):
    material_output_0.location = (460.0, 80.0)
if hasattr(material_output_0, 'mute'):
    material_output_0.mute = False
if hasattr(material_output_0, 'name'):
    material_output_0.name = 'Material Output'
if hasattr(material_output_0, 'target'):
    material_output_0.target = 'ALL'
if hasattr(material_output_0, 'use_custom_color'):
    material_output_0.use_custom_color = False
if hasattr(material_output_0, 'width'):
    material_output_0.width = 140.0
material_output_0.inputs[2].default_value = (0.0, 0.0, 0.0)

mix_shader_0 = node_tree0.nodes.new('ShaderNodeMixShader')
if hasattr(mix_shader_0, 'active_preview'):
    mix_shader_0.active_preview = False
if hasattr(mix_shader_0, 'color'):
    mix_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_shader_0, 'hide'):
    mix_shader_0.hide = False
if hasattr(mix_shader_0, 'location'):
    mix_shader_0.location = (280.0, 80.0)
if hasattr(mix_shader_0, 'mute'):
    mix_shader_0.mute = False
if hasattr(mix_shader_0, 'name'):
    mix_shader_0.name = 'Mix Shader'
if hasattr(mix_shader_0, 'use_custom_color'):
    mix_shader_0.use_custom_color = False
if hasattr(mix_shader_0, 'width'):
    mix_shader_0.width = 140.0
mix_shader_0.inputs[0].default_value = 0.5

emission_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_0, 'active_preview'):
    emission_0.active_preview = False
if hasattr(emission_0, 'color'):
    emission_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_0, 'hide'):
    emission_0.hide = False
if hasattr(emission_0, 'location'):
    emission_0.location = (100.0, 80.0)
if hasattr(emission_0, 'mute'):
    emission_0.mute = False
if hasattr(emission_0, 'name'):
    emission_0.name = 'Emission'
if hasattr(emission_0, 'use_custom_color'):
    emission_0.use_custom_color = False
if hasattr(emission_0, 'width'):
    emission_0.width = 140.0
emission_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
emission_0.inputs[1].default_value = 1.0

emission_001_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_001_0, 'active_preview'):
    emission_001_0.active_preview = False
if hasattr(emission_001_0, 'color'):
    emission_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_001_0, 'hide'):
    emission_001_0.hide = False
if hasattr(emission_001_0, 'location'):
    emission_001_0.location = (100.0, -40.0)
if hasattr(emission_001_0, 'mute'):
    emission_001_0.mute = False
if hasattr(emission_001_0, 'name'):
    emission_001_0.name = 'Emission.001'
if hasattr(emission_001_0, 'use_custom_color'):
    emission_001_0.use_custom_color = False
if hasattr(emission_001_0, 'width'):
    emission_001_0.width = 140.0
emission_001_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
emission_001_0.inputs[1].default_value = 1.0

geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_0, 'active_preview'):
    geometry_0.active_preview = False
if hasattr(geometry_0, 'color'):
    geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_0, 'hide'):
    geometry_0.hide = False
if hasattr(geometry_0, 'location'):
    geometry_0.location = (100.0, 320.0)
if hasattr(geometry_0, 'mute'):
    geometry_0.mute = False
if hasattr(geometry_0, 'name'):
    geometry_0.name = 'Geometry'
if hasattr(geometry_0, 'use_custom_color'):
    geometry_0.use_custom_color = False
if hasattr(geometry_0, 'width'):
    geometry_0.width = 140.0
geometry_0.outputs[0].default_value = (0.0, 0.0, 0.0)
geometry_0.outputs[1].default_value = (0.0, 0.0, 0.0)
geometry_0.outputs[2].default_value = (0.0, 0.0, 0.0)
geometry_0.outputs[3].default_value = (0.0, 0.0, 0.0)
geometry_0.outputs[4].default_value = (0.0, 0.0, 0.0)
geometry_0.outputs[5].default_value = (0.0, 0.0, 0.0)
geometry_0.outputs[6].default_value = 0.0
geometry_0.outputs[7].default_value = 0.0
geometry_0.outputs[8].default_value = 0.0

mix_001_0 = node_tree0.nodes.new('ShaderNodeMixRGB')
if hasattr(mix_001_0, 'active_preview'):
    mix_001_0.active_preview = False
if hasattr(mix_001_0, 'blend_type'):
    mix_001_0.blend_type = 'DIFFERENCE'
if hasattr(mix_001_0, 'color'):
    mix_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_001_0, 'hide'):
    mix_001_0.hide = False
if hasattr(mix_001_0, 'location'):
    mix_001_0.location = (-80.0, 80.0)
if hasattr(mix_001_0, 'mute'):
    mix_001_0.mute = False
if hasattr(mix_001_0, 'name'):
    mix_001_0.name = 'Mix.001'
if hasattr(mix_001_0, 'use_alpha'):
    mix_001_0.use_alpha = False
if hasattr(mix_001_0, 'use_clamp'):
    mix_001_0.use_clamp = False
if hasattr(mix_001_0, 'use_custom_color'):
    mix_001_0.use_custom_color = False
if hasattr(mix_001_0, 'width'):
    mix_001_0.width = 140.0
mix_001_0.inputs[0].default_value = 0.5
mix_001_0.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
mix_001_0.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
mix_001_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

mix_0 = node_tree0.nodes.new('ShaderNodeMixRGB')
if hasattr(mix_0, 'active_preview'):
    mix_0.active_preview = False
if hasattr(mix_0, 'blend_type'):
    mix_0.blend_type = 'DIFFERENCE'
if hasattr(mix_0, 'color'):
    mix_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_0, 'hide'):
    mix_0.hide = False
if hasattr(mix_0, 'location'):
    mix_0.location = (-260.0, -80.0)
if hasattr(mix_0, 'mute'):
    mix_0.mute = False
if hasattr(mix_0, 'name'):
    mix_0.name = 'Mix'
if hasattr(mix_0, 'use_alpha'):
    mix_0.use_alpha = False
if hasattr(mix_0, 'use_clamp'):
    mix_0.use_clamp = False
if hasattr(mix_0, 'use_custom_color'):
    mix_0.use_custom_color = False
if hasattr(mix_0, 'width'):
    mix_0.width = 140.0
mix_0.inputs[0].default_value = 0.5
mix_0.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
mix_0.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
mix_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

invert_001_0 = node_tree0.nodes.new('ShaderNodeInvert')
if hasattr(invert_001_0, 'active_preview'):
    invert_001_0.active_preview = False
if hasattr(invert_001_0, 'color'):
    invert_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(invert_001_0, 'hide'):
    invert_001_0.hide = False
if hasattr(invert_001_0, 'location'):
    invert_001_0.location = (-440.0, -200.0)
if hasattr(invert_001_0, 'mute'):
    invert_001_0.mute = False
if hasattr(invert_001_0, 'name'):
    invert_001_0.name = 'Invert.001'
if hasattr(invert_001_0, 'use_custom_color'):
    invert_001_0.use_custom_color = False
if hasattr(invert_001_0, 'width'):
    invert_001_0.width = 140.0
invert_001_0.inputs[0].default_value = 1.0
invert_001_0.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
invert_001_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

invert_0 = node_tree0.nodes.new('ShaderNodeInvert')
if hasattr(invert_0, 'active_preview'):
    invert_0.active_preview = False
if hasattr(invert_0, 'color'):
    invert_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(invert_0, 'hide'):
    invert_0.hide = False
if hasattr(invert_0, 'location'):
    invert_0.location = (-440.0, -80.0)
if hasattr(invert_0, 'mute'):
    invert_0.mute = False
if hasattr(invert_0, 'name'):
    invert_0.name = 'Invert'
if hasattr(invert_0, 'use_custom_color'):
    invert_0.use_custom_color = False
if hasattr(invert_0, 'width'):
    invert_0.width = 140.0
invert_0.inputs[0].default_value = 1.0
invert_0.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
invert_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

texture_coordinate_0 = node_tree0.nodes.new('ShaderNodeTexCoord')
if hasattr(texture_coordinate_0, 'active_preview'):
    texture_coordinate_0.active_preview = False
if hasattr(texture_coordinate_0, 'color'):
    texture_coordinate_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(texture_coordinate_0, 'from_instancer'):
    texture_coordinate_0.from_instancer = False
if hasattr(texture_coordinate_0, 'hide'):
    texture_coordinate_0.hide = False
if hasattr(texture_coordinate_0, 'location'):
    texture_coordinate_0.location = (-620.0, -20.0)
if hasattr(texture_coordinate_0, 'mute'):
    texture_coordinate_0.mute = False
if hasattr(texture_coordinate_0, 'name'):
    texture_coordinate_0.name = 'Texture Coordinate'
if hasattr(texture_coordinate_0, 'use_custom_color'):
    texture_coordinate_0.use_custom_color = False
if hasattr(texture_coordinate_0, 'width'):
    texture_coordinate_0.width = 140.0
texture_coordinate_0.outputs[0].default_value = (0.0, 0.0, 0.0)
texture_coordinate_0.outputs[1].default_value = (0.0, 0.0, 0.0)
texture_coordinate_0.outputs[2].default_value = (0.0, 0.0, 0.0)
texture_coordinate_0.outputs[3].default_value = (0.0, 0.0, 0.0)
texture_coordinate_0.outputs[4].default_value = (0.0, 0.0, 0.0)
texture_coordinate_0.outputs[5].default_value = (0.0, 0.0, 0.0)
texture_coordinate_0.outputs[6].default_value = (0.0, 0.0, 0.0)

# LINKS
node_tree0.links.new(texture_coordinate_0.outputs[1], invert_0.inputs[1])
node_tree0.links.new(texture_coordinate_0.outputs[2], invert_001_0.inputs[1])
node_tree0.links.new(invert_0.outputs[0], mix_0.inputs[1])
node_tree0.links.new(invert_001_0.outputs[0], mix_0.inputs[2])
node_tree0.links.new(texture_coordinate_0.outputs[0], mix_001_0.inputs[1])
node_tree0.links.new(mix_0.outputs[0], mix_001_0.inputs[2])
node_tree0.links.new(mix_001_0.outputs[0], emission_0.inputs[0])
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = h2_obn

# FAKE USER
bpy.data.materials['h2_obn'].use_fake_user = True