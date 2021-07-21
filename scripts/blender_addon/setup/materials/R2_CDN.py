import bpy

# MATERIAL
r2 = bpy.data.materials.new(name='r2')
r2.use_nodes = True
node_tree0 = r2.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
texture_coordinate_0 = node_tree0.nodes.new('ShaderNodeTexCoord')
if hasattr(texture_coordinate_0, 'color'):
    texture_coordinate_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(texture_coordinate_0, 'from_instancer'):
    texture_coordinate_0.from_instancer = False
if hasattr(texture_coordinate_0, 'hide'):
    texture_coordinate_0.hide = False
if hasattr(texture_coordinate_0, 'location'):
    texture_coordinate_0.location = (180.0, -320.0)
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
    vector_transform_0.location = (360.0, -320.0)
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

mapping_0 = node_tree0.nodes.new('ShaderNodeMapping')
if hasattr(mapping_0, 'color'):
    mapping_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mapping_0, 'hide'):
    mapping_0.hide = False
if hasattr(mapping_0, 'location'):
    mapping_0.location = (540.0, -320.0)
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

separate_xyz_0 = node_tree0.nodes.new('ShaderNodeSeparateXYZ')
if hasattr(separate_xyz_0, 'color'):
    separate_xyz_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(separate_xyz_0, 'hide'):
    separate_xyz_0.hide = False
if hasattr(separate_xyz_0, 'location'):
    separate_xyz_0.location = (720.0, -320.0)
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

checker_texture_0 = node_tree0.nodes.new('ShaderNodeTexChecker')
if hasattr(checker_texture_0, 'color'):
    checker_texture_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(checker_texture_0, 'hide'):
    checker_texture_0.hide = False
if hasattr(checker_texture_0, 'location'):
    checker_texture_0.location = (900.0, -320.0)
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

emission_001_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_001_0, 'color'):
    emission_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_001_0, 'hide'):
    emission_001_0.hide = False
if hasattr(emission_001_0, 'location'):
    emission_001_0.location = (1080.0, -440.0)
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

emission_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_0, 'color'):
    emission_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_0, 'hide'):
    emission_0.hide = False
if hasattr(emission_0, 'location'):
    emission_0.location = (1080.0, -320.0)
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

geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_0, 'color'):
    geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_0, 'hide'):
    geometry_0.hide = False
if hasattr(geometry_0, 'location'):
    geometry_0.location = (1080.0, -80.0)
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

mix_shader_0 = node_tree0.nodes.new('ShaderNodeMixShader')
if hasattr(mix_shader_0, 'color'):
    mix_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_shader_0, 'hide'):
    mix_shader_0.hide = False
if hasattr(mix_shader_0, 'location'):
    mix_shader_0.location = (1260.0, -320.0)
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
    material_output_0.location = (1440.0, -320.0)
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

value_0 = node_tree0.nodes.new('ShaderNodeValue')
if hasattr(value_0, 'color'):
    value_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(value_0, 'hide'):
    value_0.hide = False
if hasattr(value_0, 'label'):
    value_0.label = '... mm'
if hasattr(value_0, 'location'):
    value_0.location = (180.0, -580.0)
if hasattr(value_0, 'mute'):
    value_0.mute = False
if hasattr(value_0, 'name'):
    value_0.name = 'Value'
if hasattr(value_0, 'use_custom_color'):
    value_0.use_custom_color = False
if hasattr(value_0, 'width'):
    value_0.width = 140.0
value_0.outputs[0].default_value = 1.0

node_tree1 = bpy.data.node_groups.get('Spacing control')
if not node_tree1:
    node_tree1 = bpy.data.node_groups.new('Spacing control', 'ShaderNodeTree')
    # INPUTS
    node_tree1.inputs.new('NodeSocketFloat', 'Value')
    # OUTPUTS
    node_tree1.outputs.new('NodeSocketFloat', 'x1')
    node_tree1.outputs.new('NodeSocketFloat', 'x5')
    node_tree1.outputs.new('NodeSocketFloat', 'x10')
    # NODES
    group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
    if hasattr(group_output_1, 'color'):
        group_output_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(group_output_1, 'hide'):
        group_output_1.hide = False
    if hasattr(group_output_1, 'is_active_output'):
        group_output_1.is_active_output = True
    if hasattr(group_output_1, 'location'):
        group_output_1.location = (370.0, -0.0)
    if hasattr(group_output_1, 'mute'):
        group_output_1.mute = False
    if hasattr(group_output_1, 'name'):
        group_output_1.name = 'Group Output'
    if hasattr(group_output_1, 'use_custom_color'):
        group_output_1.use_custom_color = False
    if hasattr(group_output_1, 'width'):
        group_output_1.width = 140.0
    group_output_1.inputs[0].default_value = 0.0
    group_output_1.inputs[1].default_value = 0.0
    group_output_1.inputs[2].default_value = 0.0

    math_001_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_001_1, 'color'):
        math_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_001_1, 'hide'):
        math_001_1.hide = False
    if hasattr(math_001_1, 'location'):
        math_001_1.location = (0.0, -60.0)
    if hasattr(math_001_1, 'mute'):
        math_001_1.mute = False
    if hasattr(math_001_1, 'name'):
        math_001_1.name = 'Math.001'
    if hasattr(math_001_1, 'operation'):
        math_001_1.operation = 'DIVIDE'
    if hasattr(math_001_1, 'use_clamp'):
        math_001_1.use_clamp = False
    if hasattr(math_001_1, 'use_custom_color'):
        math_001_1.use_custom_color = False
    if hasattr(math_001_1, 'width'):
        math_001_1.width = 140.0
    math_001_1.inputs[0].default_value = 100.0
    math_001_1.inputs[1].default_value = 5.0
    math_001_1.inputs[2].default_value = 0.0
    math_001_1.outputs[0].default_value = 0.0

    math_002_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_002_1, 'color'):
        math_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_002_1, 'hide'):
        math_002_1.hide = False
    if hasattr(math_002_1, 'location'):
        math_002_1.location = (180.0, -100.0)
    if hasattr(math_002_1, 'mute'):
        math_002_1.mute = False
    if hasattr(math_002_1, 'name'):
        math_002_1.name = 'Math.002'
    if hasattr(math_002_1, 'operation'):
        math_002_1.operation = 'DIVIDE'
    if hasattr(math_002_1, 'use_clamp'):
        math_002_1.use_clamp = False
    if hasattr(math_002_1, 'use_custom_color'):
        math_002_1.use_custom_color = False
    if hasattr(math_002_1, 'width'):
        math_002_1.width = 140.0
    math_002_1.inputs[0].default_value = 100.0
    math_002_1.inputs[1].default_value = 2.0
    math_002_1.inputs[2].default_value = 0.0
    math_002_1.outputs[0].default_value = 0.0

    math_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_1, 'color'):
        math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_1, 'hide'):
        math_1.hide = False
    if hasattr(math_1, 'location'):
        math_1.location = (-180.0, 0.0)
    if hasattr(math_1, 'mute'):
        math_1.mute = False
    if hasattr(math_1, 'name'):
        math_1.name = 'Math'
    if hasattr(math_1, 'operation'):
        math_1.operation = 'DIVIDE'
    if hasattr(math_1, 'use_clamp'):
        math_1.use_clamp = False
    if hasattr(math_1, 'use_custom_color'):
        math_1.use_custom_color = False
    if hasattr(math_1, 'width'):
        math_1.width = 140.0
    math_1.inputs[0].default_value = 200.0
    math_1.inputs[1].default_value = 1.0
    math_1.inputs[2].default_value = 0.0
    math_1.outputs[0].default_value = 0.0

    group_input_1 = node_tree1.nodes.new('NodeGroupInput')
    if hasattr(group_input_1, 'color'):
        group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(group_input_1, 'hide'):
        group_input_1.hide = False
    if hasattr(group_input_1, 'location'):
        group_input_1.location = (-380.0, -80.0)
    if hasattr(group_input_1, 'mute'):
        group_input_1.mute = False
    if hasattr(group_input_1, 'name'):
        group_input_1.name = 'Group Input'
    if hasattr(group_input_1, 'use_custom_color'):
        group_input_1.use_custom_color = False
    if hasattr(group_input_1, 'width'):
        group_input_1.width = 140.0
    group_input_1.outputs[0].default_value = 1.0

    # LINKS
    node_tree1.links.new(math_001_1.outputs[0], math_002_1.inputs[0])
    node_tree1.links.new(math_1.outputs[0], math_001_1.inputs[0])
    node_tree1.links.new(math_002_1.outputs[0], group_output_1.inputs[2])
    node_tree1.links.new(math_001_1.outputs[0], group_output_1.inputs[1])
    node_tree1.links.new(math_1.outputs[0], group_output_1.inputs[0])
    node_tree1.links.new(group_input_1.outputs[0], math_1.inputs[1])

group_0 = node_tree0.nodes.new('ShaderNodeGroup')
if hasattr(group_0, 'node_tree'):
    group_0.node_tree = bpy.data.node_groups.get('Spacing control')
if hasattr(group_0, 'color'):
    group_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(group_0, 'hide'):
    group_0.hide = False
if hasattr(group_0, 'location'):
    group_0.location = (360.0, -520.0)
if hasattr(group_0, 'mute'):
    group_0.mute = False
if hasattr(group_0, 'name'):
    group_0.name = 'Group'
if hasattr(group_0, 'use_custom_color'):
    group_0.use_custom_color = False
if hasattr(group_0, 'width'):
    group_0.width = 140.0
group_0.inputs[0].default_value = 1.0
group_0.outputs[0].default_value = 0.0
group_0.outputs[1].default_value = 0.0
group_0.outputs[2].default_value = 0.0

# LINKS
node_tree0.links.new(mapping_0.outputs[0], separate_xyz_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[0], checker_texture_0.inputs[0])
node_tree0.links.new(vector_transform_0.outputs[0], mapping_0.inputs[0])
node_tree0.links.new(texture_coordinate_0.outputs[4], vector_transform_0.inputs[0])
node_tree0.links.new(checker_texture_0.outputs[0], emission_0.inputs[0])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(value_0.outputs[0], group_0.inputs[0])
node_tree0.links.new(group_0.outputs[0], mapping_0.inputs[3])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r2
