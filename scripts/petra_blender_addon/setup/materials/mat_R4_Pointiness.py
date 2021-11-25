import bpy

# MATERIAL
r4_pointiness = bpy.data.materials.new(name='r4_pointiness')
r4_pointiness.use_nodes = True
node_tree0 = r4_pointiness.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
colorramp_0 = node_tree0.nodes.new('ShaderNodeValToRGB')
if hasattr(colorramp_0, 'active_preview'):
    colorramp_0.active_preview = False
if hasattr(colorramp_0, 'color'):
    colorramp_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(colorramp_0, 'color_ramp'):
    if hasattr(colorramp_0.color_ramp, 'color_mode'):
        colorramp_0.color_ramp.color_mode = 'RGB'
    if hasattr(colorramp_0.color_ramp, 'elements'):
        if 0 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.46999984979629517)
        if hasattr(colorramp_0.color_ramp.elements[0], 'alpha'):
            colorramp_0.color_ramp.elements[0].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[0], 'color'):
            colorramp_0.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[0], 'position'):
            colorramp_0.color_ramp.elements[0].position = 0.46999984979629517
        if 1 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.5299997329711914)
        if hasattr(colorramp_0.color_ramp.elements[1], 'alpha'):
            colorramp_0.color_ramp.elements[1].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[1], 'color'):
            colorramp_0.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[1], 'position'):
            colorramp_0.color_ramp.elements[1].position = 0.5299997329711914
    if hasattr(colorramp_0.color_ramp, 'hue_interpolation'):
        colorramp_0.color_ramp.hue_interpolation = 'NEAR'
    if hasattr(colorramp_0.color_ramp, 'interpolation'):
        colorramp_0.color_ramp.interpolation = 'LINEAR'
if hasattr(colorramp_0, 'hide'):
    colorramp_0.hide = False
if hasattr(colorramp_0, 'location'):
    colorramp_0.location = (180.0, 0.0)
if hasattr(colorramp_0, 'mute'):
    colorramp_0.mute = False
if hasattr(colorramp_0, 'name'):
    colorramp_0.name = 'ColorRamp'
if hasattr(colorramp_0, 'use_custom_color'):
    colorramp_0.use_custom_color = False
if hasattr(colorramp_0, 'width'):
    colorramp_0.width = 240.0
colorramp_0.inputs[0].default_value = 0.5
colorramp_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
colorramp_0.outputs[1].default_value = 0.0

gamma_0 = node_tree0.nodes.new('ShaderNodeGamma')
if hasattr(gamma_0, 'active_preview'):
    gamma_0.active_preview = False
if hasattr(gamma_0, 'color'):
    gamma_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(gamma_0, 'hide'):
    gamma_0.hide = False
if hasattr(gamma_0, 'location'):
    gamma_0.location = (460.0, 0.0)
if hasattr(gamma_0, 'mute'):
    gamma_0.mute = False
if hasattr(gamma_0, 'name'):
    gamma_0.name = 'Gamma'
if hasattr(gamma_0, 'use_custom_color'):
    gamma_0.use_custom_color = False
if hasattr(gamma_0, 'width'):
    gamma_0.width = 140.0
gamma_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
gamma_0.inputs[1].default_value = 2.299999952316284
gamma_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

bright_contrast_0 = node_tree0.nodes.new('ShaderNodeBrightContrast')
if hasattr(bright_contrast_0, 'active_preview'):
    bright_contrast_0.active_preview = False
if hasattr(bright_contrast_0, 'color'):
    bright_contrast_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(bright_contrast_0, 'hide'):
    bright_contrast_0.hide = False
if hasattr(bright_contrast_0, 'location'):
    bright_contrast_0.location = (640.0, 0.0)
if hasattr(bright_contrast_0, 'mute'):
    bright_contrast_0.mute = False
if hasattr(bright_contrast_0, 'name'):
    bright_contrast_0.name = 'Bright/Contrast'
if hasattr(bright_contrast_0, 'use_custom_color'):
    bright_contrast_0.use_custom_color = False
if hasattr(bright_contrast_0, 'width'):
    bright_contrast_0.width = 140.0
bright_contrast_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
bright_contrast_0.inputs[1].default_value = 0.5
bright_contrast_0.inputs[2].default_value = 1.2000000476837158
bright_contrast_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_0, 'active_preview'):
    geometry_0.active_preview = False
if hasattr(geometry_0, 'color'):
    geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_0, 'hide'):
    geometry_0.hide = False
if hasattr(geometry_0, 'location'):
    geometry_0.location = (0.0, 0.0)
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

emission_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_0, 'active_preview'):
    emission_0.active_preview = False
if hasattr(emission_0, 'color'):
    emission_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_0, 'hide'):
    emission_0.hide = False
if hasattr(emission_0, 'location'):
    emission_0.location = (820.0, 0.0)
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
    emission_001_0.location = (820.0, -120.0)
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

mix_shader_0 = node_tree0.nodes.new('ShaderNodeMixShader')
if hasattr(mix_shader_0, 'active_preview'):
    mix_shader_0.active_preview = False
if hasattr(mix_shader_0, 'color'):
    mix_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_shader_0, 'hide'):
    mix_shader_0.hide = False
if hasattr(mix_shader_0, 'location'):
    mix_shader_0.location = (1000.0, 0.0)
if hasattr(mix_shader_0, 'mute'):
    mix_shader_0.mute = False
if hasattr(mix_shader_0, 'name'):
    mix_shader_0.name = 'Mix Shader'
if hasattr(mix_shader_0, 'use_custom_color'):
    mix_shader_0.use_custom_color = False
if hasattr(mix_shader_0, 'width'):
    mix_shader_0.width = 140.0
mix_shader_0.inputs[0].default_value = 0.5

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
    material_output_0.location = (1180.0, 0.0)
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

# LINKS
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(bright_contrast_0.outputs[0], emission_0.inputs[0])
node_tree0.links.new(geometry_0.outputs[7], colorramp_0.inputs[0])
node_tree0.links.new(colorramp_0.outputs[0], gamma_0.inputs[0])
node_tree0.links.new(gamma_0.outputs[0], bright_contrast_0.inputs[0])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r4_pointiness

# FAKE USER
bpy.data.materials['r4_pointiness'].use_fake_user = True