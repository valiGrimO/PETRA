import bpy

# MATERIAL
r2_contourline = bpy.data.materials.new(name='r2_contourline')
r2_contourline.use_nodes = True
node_tree0 = r2_contourline.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
checker_texture_0 = node_tree0.nodes.new('ShaderNodeTexChecker')
if hasattr(checker_texture_0, 'color'):
    checker_texture_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(checker_texture_0, 'hide'):
    checker_texture_0.hide = False
if hasattr(checker_texture_0, 'location'):
    checker_texture_0.location = (185.0, 229.0)
if hasattr(checker_texture_0, 'mute'):
    checker_texture_0.mute = False
if hasattr(checker_texture_0, 'name'):
    checker_texture_0.name = 'Checker Texture'
if hasattr(checker_texture_0, 'use_custom_color'):
    checker_texture_0.use_custom_color = False
if hasattr(checker_texture_0, 'width'):
    checker_texture_0.width = 140.0
checker_texture_0.inputs[0].default_value = (0.0, 0.0, 0.0)
checker_texture_0.inputs[1].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
checker_texture_0.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
checker_texture_0.inputs[3].default_value = 5.0
checker_texture_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
checker_texture_0.outputs[1].default_value = 0.0

mapping_0 = node_tree0.nodes.new('ShaderNodeMapping')
if hasattr(mapping_0, 'color'):
    mapping_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mapping_0, 'hide'):
    mapping_0.hide = False
if hasattr(mapping_0, 'location'):
    mapping_0.location = (-155.0, 229.0)
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
mapping_0.inputs[1].default_value = (0.0, 0.0, 0.0)
mapping_0.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
mapping_0.inputs[3].default_value = (1.0, 1.0, 1.0)
mapping_0.outputs[0].default_value = (0.0, 0.0, 0.0)

texture_coordinate_0 = node_tree0.nodes.new('ShaderNodeTexCoord')
if hasattr(texture_coordinate_0, 'color'):
    texture_coordinate_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(texture_coordinate_0, 'from_instancer'):
    texture_coordinate_0.from_instancer = False
if hasattr(texture_coordinate_0, 'hide'):
    texture_coordinate_0.hide = False
if hasattr(texture_coordinate_0, 'location'):
    texture_coordinate_0.location = (-495.0, 229.0)
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

vector_transform_0 = node_tree0.nodes.new('ShaderNodeVectorTransform')
if hasattr(vector_transform_0, 'color'):
    vector_transform_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(vector_transform_0, 'convert_from'):
    vector_transform_0.convert_from = 'WORLD'
if hasattr(vector_transform_0, 'convert_to'):
    vector_transform_0.convert_to = 'OBJECT'
if hasattr(vector_transform_0, 'hide'):
    vector_transform_0.hide = False
if hasattr(vector_transform_0, 'location'):
    vector_transform_0.location = (-325.0, 229.0)
if hasattr(vector_transform_0, 'mute'):
    vector_transform_0.mute = False
if hasattr(vector_transform_0, 'name'):
    vector_transform_0.name = 'Vector Transform'
if hasattr(vector_transform_0, 'use_custom_color'):
    vector_transform_0.use_custom_color = False
if hasattr(vector_transform_0, 'vector_type'):
    vector_transform_0.vector_type = 'VECTOR'
if hasattr(vector_transform_0, 'width'):
    vector_transform_0.width = 140.0
vector_transform_0.inputs[0].default_value = (0.5, 0.5, 0.5)
vector_transform_0.outputs[0].default_value = (0.0, 0.0, 0.0)

geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_0, 'color'):
    geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_0, 'hide'):
    geometry_0.hide = False
if hasattr(geometry_0, 'location'):
    geometry_0.location = (355.0, 229.0)
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
    emission_0.location = (355.0, -17.0)
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
    emission_001_0.location = (355.0, -133.0)
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
    mix_shader_0.location = (525.0, 229.0)
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
    material_output_0.location = (695.0, 229.0)
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

separate_xyz_0 = node_tree0.nodes.new('ShaderNodeSeparateXYZ')
if hasattr(separate_xyz_0, 'color'):
    separate_xyz_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(separate_xyz_0, 'hide'):
    separate_xyz_0.hide = False
if hasattr(separate_xyz_0, 'location'):
    separate_xyz_0.location = (15.0, 229.0)
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

value_0 = node_tree0.nodes.new('ShaderNodeValue')
if hasattr(value_0, 'color'):
    value_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(value_0, 'hide'):
    value_0.hide = False
if hasattr(value_0, 'label'):
    value_0.label = '... mm'
if hasattr(value_0, 'location'):
    value_0.location = (-850.386474609375, -20.698165893554688)
if hasattr(value_0, 'mute'):
    value_0.mute = False
if hasattr(value_0, 'name'):
    value_0.name = 'Value'
if hasattr(value_0, 'use_custom_color'):
    value_0.use_custom_color = False
if hasattr(value_0, 'width'):
    value_0.width = 140.0
value_0.outputs[0].default_value = 1.0

math_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_0, 'color'):
    math_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_0, 'hide'):
    math_0.hide = False
if hasattr(math_0, 'label'):
    math_0.label = 'x1'
if hasattr(math_0, 'location'):
    math_0.location = (-672.5130615234375, -20.809133529663086)
if hasattr(math_0, 'mute'):
    math_0.mute = False
if hasattr(math_0, 'name'):
    math_0.name = 'Math'
if hasattr(math_0, 'operation'):
    math_0.operation = 'DIVIDE'
if hasattr(math_0, 'use_clamp'):
    math_0.use_clamp = False
if hasattr(math_0, 'use_custom_color'):
    math_0.use_custom_color = False
if hasattr(math_0, 'width'):
    math_0.width = 140.0
math_0.inputs[0].default_value = 200.0
math_0.inputs[1].default_value = 1.0
math_0.inputs[2].default_value = 0.0
math_0.outputs[0].default_value = 0.0

math_001_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_001_0, 'color'):
    math_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_001_0, 'hide'):
    math_001_0.hide = False
if hasattr(math_001_0, 'label'):
    math_001_0.label = 'x5'
if hasattr(math_001_0, 'location'):
    math_001_0.location = (-497.0649719238281, -20.809133529663086)
if hasattr(math_001_0, 'mute'):
    math_001_0.mute = True
if hasattr(math_001_0, 'name'):
    math_001_0.name = 'Math.001'
if hasattr(math_001_0, 'operation'):
    math_001_0.operation = 'DIVIDE'
if hasattr(math_001_0, 'use_clamp'):
    math_001_0.use_clamp = False
if hasattr(math_001_0, 'use_custom_color'):
    math_001_0.use_custom_color = False
if hasattr(math_001_0, 'width'):
    math_001_0.width = 140.0
math_001_0.inputs[0].default_value = 100.0
math_001_0.inputs[1].default_value = 5.0
math_001_0.inputs[2].default_value = 0.0
math_001_0.outputs[0].default_value = 0.0

math_002_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_002_0, 'color'):
    math_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_002_0, 'hide'):
    math_002_0.hide = False
if hasattr(math_002_0, 'label'):
    math_002_0.label = 'x10'
if hasattr(math_002_0, 'location'):
    math_002_0.location = (-326.4674987792969, -20.0)
if hasattr(math_002_0, 'mute'):
    math_002_0.mute = True
if hasattr(math_002_0, 'name'):
    math_002_0.name = 'Math.002'
if hasattr(math_002_0, 'operation'):
    math_002_0.operation = 'DIVIDE'
if hasattr(math_002_0, 'use_clamp'):
    math_002_0.use_clamp = False
if hasattr(math_002_0, 'use_custom_color'):
    math_002_0.use_custom_color = False
if hasattr(math_002_0, 'width'):
    math_002_0.width = 140.0
math_002_0.inputs[0].default_value = 100.0
math_002_0.inputs[1].default_value = 2.0
math_002_0.inputs[2].default_value = 0.0
math_002_0.outputs[0].default_value = 0.0

# LINKS
node_tree0.links.new(mapping_0.outputs[0], separate_xyz_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[0], checker_texture_0.inputs[0])
node_tree0.links.new(vector_transform_0.outputs[0], mapping_0.inputs[0])
node_tree0.links.new(texture_coordinate_0.outputs[4], vector_transform_0.inputs[0])
node_tree0.links.new(checker_texture_0.outputs[0], emission_0.inputs[0])
node_tree0.links.new(value_0.outputs[0], math_0.inputs[1])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(math_001_0.outputs[0], math_002_0.inputs[0])
node_tree0.links.new(math_002_0.outputs[0], mapping_0.inputs[3])
node_tree0.links.new(math_0.outputs[0], math_001_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r2_contourline
