import bpy

# MATERIAL
l1_ao = bpy.data.materials.new(name='l1_ao')
l1_ao.use_nodes = True
node_tree0 = l1_ao.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
mix_shader_001_0 = node_tree0.nodes.new('ShaderNodeMixShader')
if hasattr(mix_shader_001_0, 'active_preview'):
    mix_shader_001_0.active_preview = False
if hasattr(mix_shader_001_0, 'color'):
    mix_shader_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_shader_001_0, 'hide'):
    mix_shader_001_0.hide = False
if hasattr(mix_shader_001_0, 'location'):
    mix_shader_001_0.location = (0.0, 0.0)
if hasattr(mix_shader_001_0, 'mute'):
    mix_shader_001_0.mute = False
if hasattr(mix_shader_001_0, 'name'):
    mix_shader_001_0.name = 'Mix Shader.001'
if hasattr(mix_shader_001_0, 'use_custom_color'):
    mix_shader_001_0.use_custom_color = False
if hasattr(mix_shader_001_0, 'width'):
    mix_shader_001_0.width = 140.0
mix_shader_001_0.inputs[0].default_value = 0.5

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
    material_output_0.location = (180.0, 0.0)
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

emission_003_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_003_0, 'active_preview'):
    emission_003_0.active_preview = False
if hasattr(emission_003_0, 'color'):
    emission_003_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_003_0, 'hide'):
    emission_003_0.hide = False
if hasattr(emission_003_0, 'location'):
    emission_003_0.location = (-180.0, 0.0)
if hasattr(emission_003_0, 'mute'):
    emission_003_0.mute = False
if hasattr(emission_003_0, 'name'):
    emission_003_0.name = 'Emission.003'
if hasattr(emission_003_0, 'use_custom_color'):
    emission_003_0.use_custom_color = False
if hasattr(emission_003_0, 'width'):
    emission_003_0.width = 140.0
emission_003_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
emission_003_0.inputs[1].default_value = 1.0

geometry_001_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_001_0, 'active_preview'):
    geometry_001_0.active_preview = False
if hasattr(geometry_001_0, 'color'):
    geometry_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_001_0, 'hide'):
    geometry_001_0.hide = False
if hasattr(geometry_001_0, 'location'):
    geometry_001_0.location = (-180.0, 240.0)
if hasattr(geometry_001_0, 'mute'):
    geometry_001_0.mute = False
if hasattr(geometry_001_0, 'name'):
    geometry_001_0.name = 'Geometry.001'
if hasattr(geometry_001_0, 'use_custom_color'):
    geometry_001_0.use_custom_color = False
if hasattr(geometry_001_0, 'width'):
    geometry_001_0.width = 140.0
geometry_001_0.outputs[0].default_value = (0.0, 0.0, 0.0)
geometry_001_0.outputs[1].default_value = (0.0, 0.0, 0.0)
geometry_001_0.outputs[2].default_value = (0.0, 0.0, 0.0)
geometry_001_0.outputs[3].default_value = (0.0, 0.0, 0.0)
geometry_001_0.outputs[4].default_value = (0.0, 0.0, 0.0)
geometry_001_0.outputs[5].default_value = (0.0, 0.0, 0.0)
geometry_001_0.outputs[6].default_value = 0.0
geometry_001_0.outputs[7].default_value = 0.0
geometry_001_0.outputs[8].default_value = 0.0

emission_002_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_002_0, 'active_preview'):
    emission_002_0.active_preview = False
if hasattr(emission_002_0, 'color'):
    emission_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_002_0, 'hide'):
    emission_002_0.hide = False
if hasattr(emission_002_0, 'location'):
    emission_002_0.location = (-180.0, -120.0)
if hasattr(emission_002_0, 'mute'):
    emission_002_0.mute = False
if hasattr(emission_002_0, 'name'):
    emission_002_0.name = 'Emission.002'
if hasattr(emission_002_0, 'use_custom_color'):
    emission_002_0.use_custom_color = False
if hasattr(emission_002_0, 'width'):
    emission_002_0.width = 140.0
emission_002_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
emission_002_0.inputs[1].default_value = 1.0

bright_contrast_0 = node_tree0.nodes.new('ShaderNodeBrightContrast')
if hasattr(bright_contrast_0, 'active_preview'):
    bright_contrast_0.active_preview = False
if hasattr(bright_contrast_0, 'color'):
    bright_contrast_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(bright_contrast_0, 'hide'):
    bright_contrast_0.hide = False
if hasattr(bright_contrast_0, 'location'):
    bright_contrast_0.location = (-360.0, 0.0)
if hasattr(bright_contrast_0, 'mute'):
    bright_contrast_0.mute = False
if hasattr(bright_contrast_0, 'name'):
    bright_contrast_0.name = 'Bright/Contrast'
if hasattr(bright_contrast_0, 'use_custom_color'):
    bright_contrast_0.use_custom_color = False
if hasattr(bright_contrast_0, 'width'):
    bright_contrast_0.width = 140.0
bright_contrast_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
bright_contrast_0.inputs[1].default_value = -0.30000001192092896
bright_contrast_0.inputs[2].default_value = 0.6000000238418579
bright_contrast_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

ambient_occlusion_001_0 = node_tree0.nodes.new('ShaderNodeAmbientOcclusion')
if hasattr(ambient_occlusion_001_0, 'active_preview'):
    ambient_occlusion_001_0.active_preview = False
if hasattr(ambient_occlusion_001_0, 'color'):
    ambient_occlusion_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(ambient_occlusion_001_0, 'hide'):
    ambient_occlusion_001_0.hide = False
if hasattr(ambient_occlusion_001_0, 'inside'):
    ambient_occlusion_001_0.inside = False
if hasattr(ambient_occlusion_001_0, 'location'):
    ambient_occlusion_001_0.location = (-540.0, 0.0)
if hasattr(ambient_occlusion_001_0, 'mute'):
    ambient_occlusion_001_0.mute = False
if hasattr(ambient_occlusion_001_0, 'name'):
    ambient_occlusion_001_0.name = 'Ambient Occlusion.001'
if hasattr(ambient_occlusion_001_0, 'only_local'):
    ambient_occlusion_001_0.only_local = False
if hasattr(ambient_occlusion_001_0, 'samples'):
    ambient_occlusion_001_0.samples = 64
if hasattr(ambient_occlusion_001_0, 'use_custom_color'):
    ambient_occlusion_001_0.use_custom_color = False
if hasattr(ambient_occlusion_001_0, 'width'):
    ambient_occlusion_001_0.width = 140.0
ambient_occlusion_001_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
ambient_occlusion_001_0.inputs[1].default_value = 1.0
ambient_occlusion_001_0.inputs[2].default_value = (0.0, 0.0, 0.0)
ambient_occlusion_001_0.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
ambient_occlusion_001_0.outputs[1].default_value = 0.0

# LINKS
node_tree0.links.new(emission_002_0.outputs[0], mix_shader_001_0.inputs[2])
node_tree0.links.new(geometry_001_0.outputs[6], mix_shader_001_0.inputs[0])
node_tree0.links.new(mix_shader_001_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(emission_003_0.outputs[0], mix_shader_001_0.inputs[1])
node_tree0.links.new(ambient_occlusion_001_0.outputs[1], bright_contrast_0.inputs[0])
node_tree0.links.new(bright_contrast_0.outputs[0], emission_003_0.inputs[1])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = l1_ao

# FAKE USER
bpy.data.materials['l1_ao'].use_fake_user = True