import bpy

# MATERIAL
r1_nmc = bpy.data.materials.new(name='r1_nmc')
r1_nmc.use_nodes = True
node_tree0 = r1_nmc.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
reroute_003_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_003_0, 'color'):
    reroute_003_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_003_0, 'hide'):
    reroute_003_0.hide = False
if hasattr(reroute_003_0, 'location'):
    reroute_003_0.location = (400.0, -680.0)
if hasattr(reroute_003_0, 'mute'):
    reroute_003_0.mute = False
if hasattr(reroute_003_0, 'name'):
    reroute_003_0.name = 'Reroute.003'
if hasattr(reroute_003_0, 'use_custom_color'):
    reroute_003_0.use_custom_color = False
if hasattr(reroute_003_0, 'width'):
    reroute_003_0.width = 16.0

reroute_005_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_005_0, 'color'):
    reroute_005_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_005_0, 'hide'):
    reroute_005_0.hide = False
if hasattr(reroute_005_0, 'location'):
    reroute_005_0.location = (400.0, -300.0)
if hasattr(reroute_005_0, 'mute'):
    reroute_005_0.mute = False
if hasattr(reroute_005_0, 'name'):
    reroute_005_0.name = 'Reroute.005'
if hasattr(reroute_005_0, 'use_custom_color'):
    reroute_005_0.use_custom_color = False
if hasattr(reroute_005_0, 'width'):
    reroute_005_0.width = 16.0

reroute_004_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_004_0, 'color'):
    reroute_004_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_004_0, 'hide'):
    reroute_004_0.hide = False
if hasattr(reroute_004_0, 'location'):
    reroute_004_0.location = (400.0, -400.0)
if hasattr(reroute_004_0, 'mute'):
    reroute_004_0.mute = False
if hasattr(reroute_004_0, 'name'):
    reroute_004_0.name = 'Reroute.004'
if hasattr(reroute_004_0, 'use_custom_color'):
    reroute_004_0.use_custom_color = False
if hasattr(reroute_004_0, 'width'):
    reroute_004_0.width = 16.0

reroute_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_0, 'color'):
    reroute_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_0, 'hide'):
    reroute_0.hide = False
if hasattr(reroute_0, 'location'):
    reroute_0.location = (360.0, -520.0)
if hasattr(reroute_0, 'mute'):
    reroute_0.mute = False
if hasattr(reroute_0, 'name'):
    reroute_0.name = 'Reroute'
if hasattr(reroute_0, 'use_custom_color'):
    reroute_0.use_custom_color = False
if hasattr(reroute_0, 'width'):
    reroute_0.width = 16.0

reroute_001_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_001_0, 'color'):
    reroute_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_001_0, 'hide'):
    reroute_001_0.hide = False
if hasattr(reroute_001_0, 'location'):
    reroute_001_0.location = (360.0, -280.0)
if hasattr(reroute_001_0, 'mute'):
    reroute_001_0.mute = False
if hasattr(reroute_001_0, 'name'):
    reroute_001_0.name = 'Reroute.001'
if hasattr(reroute_001_0, 'use_custom_color'):
    reroute_001_0.use_custom_color = False
if hasattr(reroute_001_0, 'width'):
    reroute_001_0.width = 16.0

value_0 = node_tree0.nodes.new('ShaderNodeValue')
if hasattr(value_0, 'color'):
    value_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(value_0, 'hide'):
    value_0.hide = False
if hasattr(value_0, 'location'):
    value_0.location = (220.0, -640.0)
if hasattr(value_0, 'mute'):
    value_0.mute = False
if hasattr(value_0, 'name'):
    value_0.name = 'Value'
if hasattr(value_0, 'use_custom_color'):
    value_0.use_custom_color = False
if hasattr(value_0, 'width'):
    value_0.width = 140.0
value_0.outputs[0].default_value = 0.5

mapping_001_0 = node_tree0.nodes.new('ShaderNodeMapping')
if hasattr(mapping_001_0, 'color'):
    mapping_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mapping_001_0, 'hide'):
    mapping_001_0.hide = False
if hasattr(mapping_001_0, 'location'):
    mapping_001_0.location = (440.0, -180.0)
if hasattr(mapping_001_0, 'mute'):
    mapping_001_0.mute = False
if hasattr(mapping_001_0, 'name'):
    mapping_001_0.name = 'Mapping.001'
if hasattr(mapping_001_0, 'use_custom_color'):
    mapping_001_0.use_custom_color = False
if hasattr(mapping_001_0, 'vector_type'):
    mapping_001_0.vector_type = 'POINT'
if hasattr(mapping_001_0, 'width'):
    mapping_001_0.width = 140.0
mapping_001_0.inputs[0].default_value = (0.0, 0.0, 0.0)
mapping_001_0.inputs[1].default_value = (0.5, 0.5, 0.5)
mapping_001_0.inputs[2].default_value = (0.0, 0.0, 0.0)
mapping_001_0.inputs[3].default_value = (0.49000000953674316, 0.49000000953674316, 0.49000000953674316)
mapping_001_0.outputs[0].default_value = (0.0, 0.0, 0.0)

mapping_002_0 = node_tree0.nodes.new('ShaderNodeMapping')
if hasattr(mapping_002_0, 'color'):
    mapping_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mapping_002_0, 'hide'):
    mapping_002_0.hide = False
if hasattr(mapping_002_0, 'location'):
    mapping_002_0.location = (440.0, -420.0)
if hasattr(mapping_002_0, 'mute'):
    mapping_002_0.mute = False
if hasattr(mapping_002_0, 'name'):
    mapping_002_0.name = 'Mapping.002'
if hasattr(mapping_002_0, 'use_custom_color'):
    mapping_002_0.use_custom_color = False
if hasattr(mapping_002_0, 'vector_type'):
    mapping_002_0.vector_type = 'POINT'
if hasattr(mapping_002_0, 'width'):
    mapping_002_0.width = 140.0
mapping_002_0.inputs[0].default_value = (0.0, 0.0, 0.0)
mapping_002_0.inputs[1].default_value = (0.0, 0.0, 0.5)
mapping_002_0.inputs[2].default_value = (0.0, 0.0, 0.0)
mapping_002_0.inputs[3].default_value = (0.49000000953674316, 0.49000000953674316, 0.49000000953674316)
mapping_002_0.outputs[0].default_value = (0.0, 0.0, 0.0)

separate_xyz_0 = node_tree0.nodes.new('ShaderNodeSeparateXYZ')
if hasattr(separate_xyz_0, 'color'):
    separate_xyz_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(separate_xyz_0, 'hide'):
    separate_xyz_0.hide = False
if hasattr(separate_xyz_0, 'location'):
    separate_xyz_0.location = (600.0, -180.0)
if hasattr(separate_xyz_0, 'mute'):
    separate_xyz_0.mute = False
if hasattr(separate_xyz_0, 'name'):
    separate_xyz_0.name = 'Separate XYZ'
if hasattr(separate_xyz_0, 'use_custom_color'):
    separate_xyz_0.use_custom_color = False
if hasattr(separate_xyz_0, 'width'):
    separate_xyz_0.width = 140.0
separate_xyz_0.inputs[0].default_value = (0.0, 0.0, 0.0)
separate_xyz_0.outputs[0].default_value = 0.0
separate_xyz_0.outputs[1].default_value = 0.0
separate_xyz_0.outputs[2].default_value = 0.0

combine_xyz_0 = node_tree0.nodes.new('ShaderNodeCombineXYZ')
if hasattr(combine_xyz_0, 'color'):
    combine_xyz_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(combine_xyz_0, 'hide'):
    combine_xyz_0.hide = False
if hasattr(combine_xyz_0, 'location'):
    combine_xyz_0.location = (760.0, -180.0)
if hasattr(combine_xyz_0, 'mute'):
    combine_xyz_0.mute = False
if hasattr(combine_xyz_0, 'name'):
    combine_xyz_0.name = 'Combine XYZ'
if hasattr(combine_xyz_0, 'use_custom_color'):
    combine_xyz_0.use_custom_color = False
if hasattr(combine_xyz_0, 'width'):
    combine_xyz_0.width = 140.0
combine_xyz_0.inputs[0].default_value = 0.0
combine_xyz_0.inputs[1].default_value = 0.0
combine_xyz_0.inputs[2].default_value = 0.0
combine_xyz_0.outputs[0].default_value = (0.0, 0.0, 0.0)

gradient_texture_001_0 = node_tree0.nodes.new('ShaderNodeTexGradient')
if hasattr(gradient_texture_001_0, 'color'):
    gradient_texture_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(gradient_texture_001_0, 'gradient_type'):
    gradient_texture_001_0.gradient_type = 'QUADRATIC'
if hasattr(gradient_texture_001_0, 'hide'):
    gradient_texture_001_0.hide = False
if hasattr(gradient_texture_001_0, 'location'):
    gradient_texture_001_0.location = (920.0, -180.0)
if hasattr(gradient_texture_001_0, 'mute'):
    gradient_texture_001_0.mute = False
if hasattr(gradient_texture_001_0, 'name'):
    gradient_texture_001_0.name = 'Gradient Texture.001'
if hasattr(gradient_texture_001_0, 'use_custom_color'):
    gradient_texture_001_0.use_custom_color = False
if hasattr(gradient_texture_001_0, 'width'):
    gradient_texture_001_0.width = 140.0
gradient_texture_001_0.inputs[0].default_value = (0.0, 0.0, 0.0)
gradient_texture_001_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
gradient_texture_001_0.outputs[1].default_value = 0.0

gradient_texture_002_0 = node_tree0.nodes.new('ShaderNodeTexGradient')
if hasattr(gradient_texture_002_0, 'color'):
    gradient_texture_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(gradient_texture_002_0, 'gradient_type'):
    gradient_texture_002_0.gradient_type = 'SPHERICAL'
if hasattr(gradient_texture_002_0, 'hide'):
    gradient_texture_002_0.hide = False
if hasattr(gradient_texture_002_0, 'location'):
    gradient_texture_002_0.location = (920.0, -320.0)
if hasattr(gradient_texture_002_0, 'mute'):
    gradient_texture_002_0.mute = False
if hasattr(gradient_texture_002_0, 'name'):
    gradient_texture_002_0.name = 'Gradient Texture.002'
if hasattr(gradient_texture_002_0, 'use_custom_color'):
    gradient_texture_002_0.use_custom_color = False
if hasattr(gradient_texture_002_0, 'width'):
    gradient_texture_002_0.width = 140.0
gradient_texture_002_0.inputs[0].default_value = (0.0, 0.0, 0.0)
gradient_texture_002_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
gradient_texture_002_0.outputs[1].default_value = 0.0

gradient_texture_0 = node_tree0.nodes.new('ShaderNodeTexGradient')
if hasattr(gradient_texture_0, 'color'):
    gradient_texture_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(gradient_texture_0, 'gradient_type'):
    gradient_texture_0.gradient_type = 'QUADRATIC'
if hasattr(gradient_texture_0, 'hide'):
    gradient_texture_0.hide = False
if hasattr(gradient_texture_0, 'location'):
    gradient_texture_0.location = (920.0, -40.0)
if hasattr(gradient_texture_0, 'mute'):
    gradient_texture_0.mute = False
if hasattr(gradient_texture_0, 'name'):
    gradient_texture_0.name = 'Gradient Texture'
if hasattr(gradient_texture_0, 'use_custom_color'):
    gradient_texture_0.use_custom_color = False
if hasattr(gradient_texture_0, 'width'):
    gradient_texture_0.width = 140.0
gradient_texture_0.inputs[0].default_value = (0.0, 0.0, 0.0)
gradient_texture_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
gradient_texture_0.outputs[1].default_value = 0.0

mapping_0 = node_tree0.nodes.new('ShaderNodeMapping')
if hasattr(mapping_0, 'color'):
    mapping_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mapping_0, 'hide'):
    mapping_0.hide = False
if hasattr(mapping_0, 'location'):
    mapping_0.location = (440.0, 60.0)
if hasattr(mapping_0, 'mute'):
    mapping_0.mute = False
if hasattr(mapping_0, 'name'):
    mapping_0.name = 'Mapping'
if hasattr(mapping_0, 'use_custom_color'):
    mapping_0.use_custom_color = False
if hasattr(mapping_0, 'vector_type'):
    mapping_0.vector_type = 'POINT'
if hasattr(mapping_0, 'width'):
    mapping_0.width = 140.0
mapping_0.inputs[0].default_value = (0.0, 0.0, 0.0)
mapping_0.inputs[1].default_value = (0.5, 0.5, 0.5)
mapping_0.inputs[2].default_value = (0.0, 0.0, 0.0)
mapping_0.inputs[3].default_value = (0.49000000953674316, 0.49000000953674316, 0.49000000953674316)
mapping_0.outputs[0].default_value = (0.0, 0.0, 0.0)

reroute_007_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_007_0, 'color'):
    reroute_007_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_007_0, 'hide'):
    reroute_007_0.hide = False
if hasattr(reroute_007_0, 'location'):
    reroute_007_0.location = (400.0, -60.0)
if hasattr(reroute_007_0, 'mute'):
    reroute_007_0.mute = False
if hasattr(reroute_007_0, 'name'):
    reroute_007_0.name = 'Reroute.007'
if hasattr(reroute_007_0, 'use_custom_color'):
    reroute_007_0.use_custom_color = False
if hasattr(reroute_007_0, 'width'):
    reroute_007_0.width = 16.0

reroute_006_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_006_0, 'color'):
    reroute_006_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_006_0, 'hide'):
    reroute_006_0.hide = False
if hasattr(reroute_006_0, 'location'):
    reroute_006_0.location = (400.0, -160.0)
if hasattr(reroute_006_0, 'mute'):
    reroute_006_0.mute = False
if hasattr(reroute_006_0, 'name'):
    reroute_006_0.name = 'Reroute.006'
if hasattr(reroute_006_0, 'use_custom_color'):
    reroute_006_0.use_custom_color = False
if hasattr(reroute_006_0, 'width'):
    reroute_006_0.width = 16.0

reroute_002_0 = node_tree0.nodes.new('NodeReroute')
if hasattr(reroute_002_0, 'color'):
    reroute_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(reroute_002_0, 'hide'):
    reroute_002_0.hide = False
if hasattr(reroute_002_0, 'location'):
    reroute_002_0.location = (360.0, -40.0)
if hasattr(reroute_002_0, 'mute'):
    reroute_002_0.mute = False
if hasattr(reroute_002_0, 'name'):
    reroute_002_0.name = 'Reroute.002'
if hasattr(reroute_002_0, 'use_custom_color'):
    reroute_002_0.use_custom_color = False
if hasattr(reroute_002_0, 'width'):
    reroute_002_0.width = 16.0

vector_transform_0 = node_tree0.nodes.new('ShaderNodeVectorTransform')
if hasattr(vector_transform_0, 'color'):
    vector_transform_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(vector_transform_0, 'convert_from'):
    vector_transform_0.convert_from = 'OBJECT'
if hasattr(vector_transform_0, 'convert_to'):
    vector_transform_0.convert_to = 'CAMERA'
if hasattr(vector_transform_0, 'hide'):
    vector_transform_0.hide = False
if hasattr(vector_transform_0, 'location'):
    vector_transform_0.location = (180.0, 0.0)
if hasattr(vector_transform_0, 'mute'):
    vector_transform_0.mute = False
if hasattr(vector_transform_0, 'name'):
    vector_transform_0.name = 'Vector Transform'
if hasattr(vector_transform_0, 'use_custom_color'):
    vector_transform_0.use_custom_color = False
if hasattr(vector_transform_0, 'vector_type'):
    vector_transform_0.vector_type = 'NORMAL'
if hasattr(vector_transform_0, 'width'):
    vector_transform_0.width = 140.0
vector_transform_0.inputs[0].default_value = (0.5, 0.5, 0.5)
vector_transform_0.outputs[0].default_value = (0.0, 0.0, 0.0)

combine_rgb_0 = node_tree0.nodes.new('ShaderNodeCombineRGB')
if hasattr(combine_rgb_0, 'color'):
    combine_rgb_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(combine_rgb_0, 'hide'):
    combine_rgb_0.hide = False
if hasattr(combine_rgb_0, 'location'):
    combine_rgb_0.location = (1100.0, -180.0)
if hasattr(combine_rgb_0, 'mute'):
    combine_rgb_0.mute = False
if hasattr(combine_rgb_0, 'name'):
    combine_rgb_0.name = 'Combine RGB'
if hasattr(combine_rgb_0, 'use_custom_color'):
    combine_rgb_0.use_custom_color = False
if hasattr(combine_rgb_0, 'width'):
    combine_rgb_0.width = 140.0
combine_rgb_0.inputs[0].default_value = 0.0
combine_rgb_0.inputs[1].default_value = 0.0
combine_rgb_0.inputs[2].default_value = 0.0
combine_rgb_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_0, 'color'):
    geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_0, 'hide'):
    geometry_0.hide = False
if hasattr(geometry_0, 'location'):
    geometry_0.location = (1280.0, 60.0)
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
    emission_0.location = (1280.0, -180.0)
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
if hasattr(emission_001_0, 'color'):
    emission_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_001_0, 'hide'):
    emission_001_0.hide = False
if hasattr(emission_001_0, 'location'):
    emission_001_0.location = (1280.0, -300.0)
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
if hasattr(mix_shader_0, 'color'):
    mix_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_shader_0, 'hide'):
    mix_shader_0.hide = False
if hasattr(mix_shader_0, 'location'):
    mix_shader_0.location = (1460.0, -180.0)
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
    material_output_0.location = (1640.0, -180.0)
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

texture_coordinate_0 = node_tree0.nodes.new('ShaderNodeTexCoord')
if hasattr(texture_coordinate_0, 'color'):
    texture_coordinate_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(texture_coordinate_0, 'from_instancer'):
    texture_coordinate_0.from_instancer = False
if hasattr(texture_coordinate_0, 'hide'):
    texture_coordinate_0.hide = False
if hasattr(texture_coordinate_0, 'location'):
    texture_coordinate_0.location = (0.0, 0.0)
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
node_tree0.links.new(mapping_0.outputs[0], gradient_texture_0.inputs[0])
node_tree0.links.new(mapping_001_0.outputs[0], separate_xyz_0.inputs[0])
node_tree0.links.new(combine_xyz_0.outputs[0], gradient_texture_001_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[0], combine_xyz_0.inputs[1])
node_tree0.links.new(separate_xyz_0.outputs[1], combine_xyz_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[2], combine_xyz_0.inputs[2])
node_tree0.links.new(mapping_002_0.outputs[0], gradient_texture_002_0.inputs[0])
node_tree0.links.new(gradient_texture_001_0.outputs[0], combine_rgb_0.inputs[1])
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])
node_tree0.links.new(combine_rgb_0.outputs[0], emission_0.inputs[0])
node_tree0.links.new(gradient_texture_0.outputs[0], combine_rgb_0.inputs[0])
node_tree0.links.new(gradient_texture_002_0.outputs[0], combine_rgb_0.inputs[2])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(texture_coordinate_0.outputs[1], vector_transform_0.inputs[0])
node_tree0.links.new(reroute_0.outputs[0], mapping_002_0.inputs[0])
node_tree0.links.new(reroute_001_0.outputs[0], mapping_001_0.inputs[0])
node_tree0.links.new(reroute_001_0.outputs[0], reroute_0.inputs[0])
node_tree0.links.new(reroute_002_0.outputs[0], reroute_001_0.inputs[0])
node_tree0.links.new(reroute_002_0.outputs[0], mapping_0.inputs[0])
node_tree0.links.new(vector_transform_0.outputs[0], reroute_002_0.inputs[0])
node_tree0.links.new(value_0.outputs[0], reroute_003_0.inputs[0])
node_tree0.links.new(reroute_003_0.outputs[0], mapping_002_0.inputs[3])
node_tree0.links.new(reroute_003_0.outputs[0], reroute_004_0.inputs[0])
node_tree0.links.new(reroute_004_0.outputs[0], mapping_001_0.inputs[3])
node_tree0.links.new(reroute_005_0.outputs[0], mapping_001_0.inputs[1])
node_tree0.links.new(reroute_004_0.outputs[0], reroute_005_0.inputs[0])
node_tree0.links.new(reroute_006_0.outputs[0], reroute_007_0.inputs[0])
node_tree0.links.new(reroute_005_0.outputs[0], reroute_006_0.inputs[0])
node_tree0.links.new(reroute_006_0.outputs[0], mapping_0.inputs[3])
node_tree0.links.new(reroute_007_0.outputs[0], mapping_0.inputs[1])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r1_nmc
