import bpy

# MATERIAL
r2_contourline = bpy.data.materials.new(name='r2_contourline')
r2_contourline.use_nodes = True
node_tree0 = r2_contourline.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
value_0 = node_tree0.nodes.new('ShaderNodeValue')
if hasattr(value_0, 'active_preview'):
    value_0.active_preview = False
if hasattr(value_0, 'color'):
    value_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(value_0, 'hide'):
    value_0.hide = False
if hasattr(value_0, 'label'):
    value_0.label = '... mm'
if hasattr(value_0, 'location'):
    value_0.location = (0.0, 0.0)
if hasattr(value_0, 'mute'):
    value_0.mute = False
if hasattr(value_0, 'name'):
    value_0.name = 'Value'
if hasattr(value_0, 'use_custom_color'):
    value_0.use_custom_color = False
if hasattr(value_0, 'width'):
    value_0.width = 140.0
value_0.outputs[0].default_value = 1.0

math_001_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_001_0, 'active_preview'):
    math_001_0.active_preview = False
if hasattr(math_001_0, 'color'):
    math_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_001_0, 'hide'):
    math_001_0.hide = False
if hasattr(math_001_0, 'label'):
    math_001_0.label = 'x5'
if hasattr(math_001_0, 'location'):
    math_001_0.location = (360.0, 0.0)
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

math_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_0, 'active_preview'):
    math_0.active_preview = False
if hasattr(math_0, 'color'):
    math_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_0, 'hide'):
    math_0.hide = False
if hasattr(math_0, 'label'):
    math_0.label = 'x1'
if hasattr(math_0, 'location'):
    math_0.location = (180.0, 0.0)
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

math_002_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_002_0, 'active_preview'):
    math_002_0.active_preview = False
if hasattr(math_002_0, 'color'):
    math_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_002_0, 'hide'):
    math_002_0.hide = False
if hasattr(math_002_0, 'label'):
    math_002_0.label = 'x10'
if hasattr(math_002_0, 'location'):
    math_002_0.location = (540.0, 0.0)
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

node_tree1 = bpy.data.node_groups.get('NodeGroup')
if not node_tree1:
    node_tree1 = bpy.data.node_groups.new('NodeGroup', 'ShaderNodeTree')
    # INPUTS
    node_tree1.inputs.new('NodeSocketVectorXYZ', 'Scale')
    # OUTPUTS
    node_tree1.outputs.new('NodeSocketShader', 'Shader')
    # NODES
    texture_coordinate_1 = node_tree1.nodes.new('ShaderNodeTexCoord')
    if hasattr(texture_coordinate_1, 'active_preview'):
        texture_coordinate_1.active_preview = False
    if hasattr(texture_coordinate_1, 'color'):
        texture_coordinate_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(texture_coordinate_1, 'from_instancer'):
        texture_coordinate_1.from_instancer = False
    if hasattr(texture_coordinate_1, 'hide'):
        texture_coordinate_1.hide = False
    if hasattr(texture_coordinate_1, 'location'):
        texture_coordinate_1.location = (-510.0, 181.0)
    if hasattr(texture_coordinate_1, 'mute'):
        texture_coordinate_1.mute = False
    if hasattr(texture_coordinate_1, 'name'):
        texture_coordinate_1.name = 'Texture Coordinate'
    if hasattr(texture_coordinate_1, 'use_custom_color'):
        texture_coordinate_1.use_custom_color = False
    if hasattr(texture_coordinate_1, 'width'):
        texture_coordinate_1.width = 140.0
    texture_coordinate_1.outputs[0].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_1.outputs[1].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_1.outputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_1.outputs[3].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_1.outputs[4].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_1.outputs[5].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_1.outputs[6].default_value = (0.0, 0.0, 0.0)

    vector_transform_1 = node_tree1.nodes.new('ShaderNodeVectorTransform')
    if hasattr(vector_transform_1, 'active_preview'):
        vector_transform_1.active_preview = False
    if hasattr(vector_transform_1, 'color'):
        vector_transform_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(vector_transform_1, 'convert_from'):
        vector_transform_1.convert_from = 'WORLD'
    if hasattr(vector_transform_1, 'convert_to'):
        vector_transform_1.convert_to = 'OBJECT'
    if hasattr(vector_transform_1, 'hide'):
        vector_transform_1.hide = False
    if hasattr(vector_transform_1, 'location'):
        vector_transform_1.location = (-340.0, 181.0)
    if hasattr(vector_transform_1, 'mute'):
        vector_transform_1.mute = False
    if hasattr(vector_transform_1, 'name'):
        vector_transform_1.name = 'Vector Transform'
    if hasattr(vector_transform_1, 'use_custom_color'):
        vector_transform_1.use_custom_color = False
    if hasattr(vector_transform_1, 'vector_type'):
        vector_transform_1.vector_type = 'VECTOR'
    if hasattr(vector_transform_1, 'width'):
        vector_transform_1.width = 140.0
    vector_transform_1.inputs[0].default_value = (0.5, 0.5, 0.5)
    vector_transform_1.outputs[0].default_value = (0.0, 0.0, 0.0)

    mapping_1 = node_tree1.nodes.new('ShaderNodeMapping')
    if hasattr(mapping_1, 'active_preview'):
        mapping_1.active_preview = False
    if hasattr(mapping_1, 'color'):
        mapping_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(mapping_1, 'hide'):
        mapping_1.hide = False
    if hasattr(mapping_1, 'location'):
        mapping_1.location = (-170.0, 181.0)
    if hasattr(mapping_1, 'mute'):
        mapping_1.mute = False
    if hasattr(mapping_1, 'name'):
        mapping_1.name = 'Mapping'
    if hasattr(mapping_1, 'use_custom_color'):
        mapping_1.use_custom_color = False
    if hasattr(mapping_1, 'vector_type'):
        mapping_1.vector_type = 'POINT'
    if hasattr(mapping_1, 'width'):
        mapping_1.width = 140.0
    mapping_1.inputs[0].default_value = (0.0, 0.0, 0.0)
    mapping_1.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping_1.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
    mapping_1.inputs[3].default_value = (1.0, 1.0, 1.0)
    mapping_1.outputs[0].default_value = (0.0, 0.0, 0.0)

    separate_xyz_1 = node_tree1.nodes.new('ShaderNodeSeparateXYZ')
    if hasattr(separate_xyz_1, 'active_preview'):
        separate_xyz_1.active_preview = False
    if hasattr(separate_xyz_1, 'color'):
        separate_xyz_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(separate_xyz_1, 'hide'):
        separate_xyz_1.hide = False
    if hasattr(separate_xyz_1, 'location'):
        separate_xyz_1.location = (0.0, 181.0)
    if hasattr(separate_xyz_1, 'mute'):
        separate_xyz_1.mute = False
    if hasattr(separate_xyz_1, 'name'):
        separate_xyz_1.name = 'Separate XYZ'
    if hasattr(separate_xyz_1, 'use_custom_color'):
        separate_xyz_1.use_custom_color = False
    if hasattr(separate_xyz_1, 'width'):
        separate_xyz_1.width = 140.0
    separate_xyz_1.inputs[0].default_value = (0.0, 0.0, 0.0)
    separate_xyz_1.outputs[0].default_value = 0.0
    separate_xyz_1.outputs[1].default_value = 0.0
    separate_xyz_1.outputs[2].default_value = 0.0

    checker_texture_1 = node_tree1.nodes.new('ShaderNodeTexChecker')
    if hasattr(checker_texture_1, 'active_preview'):
        checker_texture_1.active_preview = False
    if hasattr(checker_texture_1, 'color'):
        checker_texture_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(checker_texture_1, 'hide'):
        checker_texture_1.hide = False
    if hasattr(checker_texture_1, 'location'):
        checker_texture_1.location = (170.0, 181.0)
    if hasattr(checker_texture_1, 'mute'):
        checker_texture_1.mute = False
    if hasattr(checker_texture_1, 'name'):
        checker_texture_1.name = 'Checker Texture'
    if hasattr(checker_texture_1, 'use_custom_color'):
        checker_texture_1.use_custom_color = False
    if hasattr(checker_texture_1, 'width'):
        checker_texture_1.width = 140.0
    checker_texture_1.inputs[0].default_value = (0.0, 0.0, 0.0)
    checker_texture_1.inputs[1].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    checker_texture_1.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
    checker_texture_1.inputs[3].default_value = 5.0
    checker_texture_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    checker_texture_1.outputs[1].default_value = 0.0

    geometry_1 = node_tree1.nodes.new('ShaderNodeNewGeometry')
    if hasattr(geometry_1, 'active_preview'):
        geometry_1.active_preview = False
    if hasattr(geometry_1, 'color'):
        geometry_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(geometry_1, 'hide'):
        geometry_1.hide = False
    if hasattr(geometry_1, 'location'):
        geometry_1.location = (340.0, 181.0)
    if hasattr(geometry_1, 'mute'):
        geometry_1.mute = False
    if hasattr(geometry_1, 'name'):
        geometry_1.name = 'Geometry'
    if hasattr(geometry_1, 'use_custom_color'):
        geometry_1.use_custom_color = False
    if hasattr(geometry_1, 'width'):
        geometry_1.width = 140.0
    geometry_1.outputs[0].default_value = (0.0, 0.0, 0.0)
    geometry_1.outputs[1].default_value = (0.0, 0.0, 0.0)
    geometry_1.outputs[2].default_value = (0.0, 0.0, 0.0)
    geometry_1.outputs[3].default_value = (0.0, 0.0, 0.0)
    geometry_1.outputs[4].default_value = (0.0, 0.0, 0.0)
    geometry_1.outputs[5].default_value = (0.0, 0.0, 0.0)
    geometry_1.outputs[6].default_value = 0.0
    geometry_1.outputs[7].default_value = 0.0
    geometry_1.outputs[8].default_value = 0.0

    mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
    if hasattr(mix_shader_1, 'active_preview'):
        mix_shader_1.active_preview = False
    if hasattr(mix_shader_1, 'color'):
        mix_shader_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(mix_shader_1, 'hide'):
        mix_shader_1.hide = False
    if hasattr(mix_shader_1, 'location'):
        mix_shader_1.location = (510.0, 181.0)
    if hasattr(mix_shader_1, 'mute'):
        mix_shader_1.mute = False
    if hasattr(mix_shader_1, 'name'):
        mix_shader_1.name = 'Mix Shader'
    if hasattr(mix_shader_1, 'use_custom_color'):
        mix_shader_1.use_custom_color = False
    if hasattr(mix_shader_1, 'width'):
        mix_shader_1.width = 140.0
    mix_shader_1.inputs[0].default_value = 0.5

    emission_1 = node_tree1.nodes.new('ShaderNodeEmission')
    if hasattr(emission_1, 'active_preview'):
        emission_1.active_preview = False
    if hasattr(emission_1, 'color'):
        emission_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(emission_1, 'hide'):
        emission_1.hide = False
    if hasattr(emission_1, 'location'):
        emission_1.location = (340.0, -65.0)
    if hasattr(emission_1, 'mute'):
        emission_1.mute = False
    if hasattr(emission_1, 'name'):
        emission_1.name = 'Emission'
    if hasattr(emission_1, 'use_custom_color'):
        emission_1.use_custom_color = False
    if hasattr(emission_1, 'width'):
        emission_1.width = 140.0
    emission_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
    emission_1.inputs[1].default_value = 1.0

    emission_001_1 = node_tree1.nodes.new('ShaderNodeEmission')
    if hasattr(emission_001_1, 'active_preview'):
        emission_001_1.active_preview = False
    if hasattr(emission_001_1, 'color'):
        emission_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(emission_001_1, 'hide'):
        emission_001_1.hide = False
    if hasattr(emission_001_1, 'location'):
        emission_001_1.location = (340.0, -181.0)
    if hasattr(emission_001_1, 'mute'):
        emission_001_1.mute = False
    if hasattr(emission_001_1, 'name'):
        emission_001_1.name = 'Emission.001'
    if hasattr(emission_001_1, 'use_custom_color'):
        emission_001_1.use_custom_color = False
    if hasattr(emission_001_1, 'width'):
        emission_001_1.width = 140.0
    emission_001_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
    emission_001_1.inputs[1].default_value = 1.0

    group_input_1 = node_tree1.nodes.new('NodeGroupInput')
    if hasattr(group_input_1, 'active_preview'):
        group_input_1.active_preview = False
    if hasattr(group_input_1, 'color'):
        group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(group_input_1, 'hide'):
        group_input_1.hide = False
    if hasattr(group_input_1, 'location'):
        group_input_1.location = (-710.0, -0.0)
    if hasattr(group_input_1, 'mute'):
        group_input_1.mute = False
    if hasattr(group_input_1, 'name'):
        group_input_1.name = 'Group Input'
    if hasattr(group_input_1, 'use_custom_color'):
        group_input_1.use_custom_color = False
    if hasattr(group_input_1, 'width'):
        group_input_1.width = 140.0
    group_input_1.outputs[0].default_value = (1.0, 1.0, 1.0)

    group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
    if hasattr(group_output_1, 'active_preview'):
        group_output_1.active_preview = False
    if hasattr(group_output_1, 'color'):
        group_output_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(group_output_1, 'hide'):
        group_output_1.hide = False
    if hasattr(group_output_1, 'is_active_output'):
        group_output_1.is_active_output = True
    if hasattr(group_output_1, 'location'):
        group_output_1.location = (700.0, -0.0)
    if hasattr(group_output_1, 'mute'):
        group_output_1.mute = False
    if hasattr(group_output_1, 'name'):
        group_output_1.name = 'Group Output'
    if hasattr(group_output_1, 'use_custom_color'):
        group_output_1.use_custom_color = False
    if hasattr(group_output_1, 'width'):
        group_output_1.width = 140.0

    # LINKS
    node_tree1.links.new(mix_shader_1.outputs[0], group_output_1.inputs[0])
    node_tree1.links.new(group_input_1.outputs[0], mapping_1.inputs[3])
    node_tree1.links.new(mapping_1.outputs[0], separate_xyz_1.inputs[0])
    node_tree1.links.new(separate_xyz_1.outputs[0], checker_texture_1.inputs[0])
    node_tree1.links.new(vector_transform_1.outputs[0], mapping_1.inputs[0])
    node_tree1.links.new(texture_coordinate_1.outputs[4], vector_transform_1.inputs[0])
    node_tree1.links.new(checker_texture_1.outputs[0], emission_1.inputs[0])
    node_tree1.links.new(emission_001_1.outputs[0], mix_shader_1.inputs[2])
    node_tree1.links.new(geometry_1.outputs[6], mix_shader_1.inputs[0])
    node_tree1.links.new(emission_1.outputs[0], mix_shader_1.inputs[1])

group_0 = node_tree0.nodes.new('ShaderNodeGroup')
if hasattr(group_0, 'node_tree'):
    group_0.node_tree = bpy.data.node_groups.get('NodeGroup')
if hasattr(group_0, 'active_preview'):
    group_0.active_preview = False
if hasattr(group_0, 'color'):
    group_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(group_0, 'hide'):
    group_0.hide = False
if hasattr(group_0, 'location'):
    group_0.location = (720.0, 0.0)
if hasattr(group_0, 'mute'):
    group_0.mute = False
if hasattr(group_0, 'name'):
    group_0.name = 'Group'
if hasattr(group_0, 'use_custom_color'):
    group_0.use_custom_color = False
if hasattr(group_0, 'width'):
    group_0.width = 140.0
group_0.inputs[0].default_value = (1.0, 1.0, 1.0)

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
    material_output_0.location = (900.0, 0.0)
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
node_tree0.links.new(value_0.outputs[0], math_0.inputs[1])
node_tree0.links.new(group_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(math_001_0.outputs[0], math_002_0.inputs[0])
node_tree0.links.new(math_002_0.outputs[0], group_0.inputs[0])
node_tree0.links.new(math_0.outputs[0], math_001_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r2_contourline
