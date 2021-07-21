import bpy

# MATERIAL
zh_masks = bpy.data.materials.new(name='zh_masks')
zh_masks.use_nodes = True
node_tree0 = zh_masks.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
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
if hasattr(emission_0, 'color'):
    emission_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_0, 'hide'):
    emission_0.hide = False
if hasattr(emission_0, 'location'):
    emission_0.location = (0.0, -240.0)
if hasattr(emission_0, 'mute'):
    emission_0.mute = False
if hasattr(emission_0, 'name'):
    emission_0.name = 'Emission'
if hasattr(emission_0, 'use_custom_color'):
    emission_0.use_custom_color = False
if hasattr(emission_0, 'width'):
    emission_0.width = 140.0
emission_0.inputs[0].default_value = (0.21404114365577698, 0.21404114365577698, 0.21404114365577698, 1.0)
emission_0.inputs[1].default_value = 1.0

emission_001_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_001_0, 'color'):
    emission_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_001_0, 'hide'):
    emission_001_0.hide = False
if hasattr(emission_001_0, 'location'):
    emission_001_0.location = (0.0, -360.0)
if hasattr(emission_001_0, 'mute'):
    emission_001_0.mute = False
if hasattr(emission_001_0, 'name'):
    emission_001_0.name = 'Emission.001'
if hasattr(emission_001_0, 'use_custom_color'):
    emission_001_0.use_custom_color = False
if hasattr(emission_001_0, 'width'):
    emission_001_0.width = 140.0
emission_001_0.inputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
emission_001_0.inputs[1].default_value = 1.0

mix_shader_0 = node_tree0.nodes.new('ShaderNodeMixShader')
if hasattr(mix_shader_0, 'color'):
    mix_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_shader_0, 'hide'):
    mix_shader_0.hide = False
if hasattr(mix_shader_0, 'location'):
    mix_shader_0.location = (180.0, -240.0)
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
if hasattr(material_output_0, 'color'):
    material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(material_output_0, 'hide'):
    material_output_0.hide = False
if hasattr(material_output_0, 'is_active_output'):
    material_output_0.is_active_output = True
if hasattr(material_output_0, 'location'):
    material_output_0.location = (360.0, -240.0)
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
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = zh_masks
