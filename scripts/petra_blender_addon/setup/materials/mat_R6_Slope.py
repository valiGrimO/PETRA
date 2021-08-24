import bpy

# MATERIAL
r6_slope = bpy.data.materials.new(name='r6_slope')
r6_slope.use_nodes = True
node_tree0 = r6_slope.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
math_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_0, 'active_preview'):
    math_0.active_preview = False
if hasattr(math_0, 'color'):
    math_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_0, 'hide'):
    math_0.hide = False
if hasattr(math_0, 'location'):
    math_0.location = (-240.0, 0.0)
if hasattr(math_0, 'mute'):
    math_0.mute = False
if hasattr(math_0, 'name'):
    math_0.name = 'Math'
if hasattr(math_0, 'operation'):
    math_0.operation = 'ARCCOSINE'
if hasattr(math_0, 'use_clamp'):
    math_0.use_clamp = False
if hasattr(math_0, 'use_custom_color'):
    math_0.use_custom_color = False
if hasattr(math_0, 'width'):
    math_0.width = 140.0
math_0.inputs[0].default_value = 0.5
math_0.inputs[1].default_value = 0.5
math_0.inputs[2].default_value = 0.0
math_0.outputs[0].default_value = 0.0

math_001_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_001_0, 'active_preview'):
    math_001_0.active_preview = False
if hasattr(math_001_0, 'color'):
    math_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_001_0, 'hide'):
    math_001_0.hide = False
if hasattr(math_001_0, 'label'):
    math_001_0.label = 'Radians to degrees'
if hasattr(math_001_0, 'location'):
    math_001_0.location = (-60.0, 0.0)
if hasattr(math_001_0, 'mute'):
    math_001_0.mute = False
if hasattr(math_001_0, 'name'):
    math_001_0.name = 'Math.001'
if hasattr(math_001_0, 'operation'):
    math_001_0.operation = 'MULTIPLY'
if hasattr(math_001_0, 'use_clamp'):
    math_001_0.use_clamp = False
if hasattr(math_001_0, 'use_custom_color'):
    math_001_0.use_custom_color = False
if hasattr(math_001_0, 'width'):
    math_001_0.width = 140.0
math_001_0.inputs[0].default_value = 0.5
math_001_0.inputs[1].default_value = 57.295780181884766
math_001_0.inputs[2].default_value = 0.0
math_001_0.outputs[0].default_value = 0.0

math_002_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_002_0, 'active_preview'):
    math_002_0.active_preview = False
if hasattr(math_002_0, 'color'):
    math_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_002_0, 'hide'):
    math_002_0.hide = False
if hasattr(math_002_0, 'label'):
    math_002_0.label = 'Normalize'
if hasattr(math_002_0, 'location'):
    math_002_0.location = (120.0, 0.0)
if hasattr(math_002_0, 'mute'):
    math_002_0.mute = False
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
math_002_0.inputs[0].default_value = 0.5
math_002_0.inputs[1].default_value = 100.0
math_002_0.inputs[2].default_value = 0.0
math_002_0.outputs[0].default_value = 0.0

separate_xyz_0 = node_tree0.nodes.new('ShaderNodeSeparateXYZ')
if hasattr(separate_xyz_0, 'active_preview'):
    separate_xyz_0.active_preview = False
if hasattr(separate_xyz_0, 'color'):
    separate_xyz_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(separate_xyz_0, 'hide'):
    separate_xyz_0.hide = False
if hasattr(separate_xyz_0, 'location'):
    separate_xyz_0.location = (-420.0, 0.0)
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
            colorramp_0.color_ramp.elements.new(0.0)
        if hasattr(colorramp_0.color_ramp.elements[0], 'alpha'):
            colorramp_0.color_ramp.elements[0].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[0], 'color'):
            colorramp_0.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[0], 'position'):
            colorramp_0.color_ramp.elements[0].position = 0.0
        if 1 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.49999940395355225)
        if hasattr(colorramp_0.color_ramp.elements[1], 'alpha'):
            colorramp_0.color_ramp.elements[1].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[1], 'color'):
            colorramp_0.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[1], 'position'):
            colorramp_0.color_ramp.elements[1].position = 0.49999940395355225
    if hasattr(colorramp_0.color_ramp, 'hue_interpolation'):
        colorramp_0.color_ramp.hue_interpolation = 'NEAR'
    if hasattr(colorramp_0.color_ramp, 'interpolation'):
        colorramp_0.color_ramp.interpolation = 'EASE'
if hasattr(colorramp_0, 'hide'):
    colorramp_0.hide = False
if hasattr(colorramp_0, 'location'):
    colorramp_0.location = (300.0, 0.0)
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

emission_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_0, 'active_preview'):
    emission_0.active_preview = False
if hasattr(emission_0, 'color'):
    emission_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_0, 'hide'):
    emission_0.hide = False
if hasattr(emission_0, 'location'):
    emission_0.location = (580.0, 0.0)
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
    emission_001_0.location = (580.0, -120.0)
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
    mix_shader_0.location = (760.0, 0.0)
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
    material_output_0.location = (940.0, 0.0)
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

geometry_001_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_001_0, 'active_preview'):
    geometry_001_0.active_preview = False
if hasattr(geometry_001_0, 'color'):
    geometry_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_001_0, 'hide'):
    geometry_001_0.hide = False
if hasattr(geometry_001_0, 'location'):
    geometry_001_0.location = (580.0, 60.0)
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

mapping_0 = node_tree0.nodes.new('ShaderNodeMapping')
if hasattr(mapping_0, 'active_preview'):
    mapping_0.active_preview = False
if hasattr(mapping_0, 'color'):
    mapping_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mapping_0, 'hide'):
    mapping_0.hide = False
if hasattr(mapping_0, 'location'):
    mapping_0.location = (-600.0, 0.0)
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
mapping_0.inputs[2].default_value = (0.0, -1.5707963705062866, 0.0)
mapping_0.inputs[3].default_value = (1.0, 1.0, 1.0)
mapping_0.outputs[0].default_value = (0.0, 0.0, 0.0)

vector_transform_0 = node_tree0.nodes.new('ShaderNodeVectorTransform')
if hasattr(vector_transform_0, 'active_preview'):
    vector_transform_0.active_preview = False
if hasattr(vector_transform_0, 'color'):
    vector_transform_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(vector_transform_0, 'convert_from'):
    vector_transform_0.convert_from = 'OBJECT'
if hasattr(vector_transform_0, 'convert_to'):
    vector_transform_0.convert_to = 'CAMERA'
if hasattr(vector_transform_0, 'hide'):
    vector_transform_0.hide = False
if hasattr(vector_transform_0, 'location'):
    vector_transform_0.location = (-780.0, 0.0)
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
    texture_coordinate_0.location = (-960.0, 0.0)
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
node_tree0.links.new(math_0.outputs[0], math_001_0.inputs[0])
node_tree0.links.new(math_001_0.outputs[0], math_002_0.inputs[0])
node_tree0.links.new(math_002_0.outputs[0], colorramp_0.inputs[0])
node_tree0.links.new(texture_coordinate_0.outputs[1], vector_transform_0.inputs[0])
node_tree0.links.new(vector_transform_0.outputs[0], mapping_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[0], math_0.inputs[0])
node_tree0.links.new(mapping_0.outputs[0], separate_xyz_0.inputs[0])
node_tree0.links.new(colorramp_0.outputs[0], emission_0.inputs[0])
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_001_0.outputs[6], mix_shader_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r6_slope
