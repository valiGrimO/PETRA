import bpy

# MATERIAL
r3_ec = bpy.data.materials.new(name='r3_ec')
r3_ec.use_nodes = True
node_tree0 = r3_ec.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
frame_0 = node_tree0.nodes.new('NodeFrame')
if hasattr(frame_0, 'color'):
    frame_0.color = (1.0, 0.0, 0.0)
if hasattr(frame_0, 'hide'):
    frame_0.hide = False
if hasattr(frame_0, 'label'):
    frame_0.label = 'ATTENTION!'
if hasattr(frame_0, 'label_size'):
    frame_0.label_size = 15
if hasattr(frame_0, 'location'):
    frame_0.location = (-1360.0, -80.0)
if hasattr(frame_0, 'mute'):
    frame_0.mute = False
if hasattr(frame_0, 'name'):
    frame_0.name = 'Frame'
if hasattr(frame_0, 'shrink'):
    frame_0.shrink = True
if hasattr(frame_0, 'text'):
    frame_0.text = bpy.data.texts.get('renduEEVEE')
if hasattr(frame_0, 'use_custom_color'):
    frame_0.use_custom_color = True
if hasattr(frame_0, 'width'):
    frame_0.width = 176.025390625

vertex_color_0 = node_tree0.nodes.new('ShaderNodeVertexColor')
if hasattr(vertex_color_0, 'color'):
    vertex_color_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(vertex_color_0, 'hide'):
    vertex_color_0.hide = False
if hasattr(vertex_color_0, 'location'):
    vertex_color_0.location = (-1014.1768188476562, -20.0)
if hasattr(vertex_color_0, 'mute'):
    vertex_color_0.mute = False
if hasattr(vertex_color_0, 'name'):
    vertex_color_0.name = 'Vertex Color'
if hasattr(vertex_color_0, 'use_custom_color'):
    vertex_color_0.use_custom_color = False
if hasattr(vertex_color_0, 'width'):
    vertex_color_0.width = 314.17681884765625
vertex_color_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
vertex_color_0.outputs[1].default_value = 0.0

material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
if hasattr(material_output_0, 'color'):
    material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(material_output_0, 'hide'):
    material_output_0.hide = False
if hasattr(material_output_0, 'is_active_output'):
    material_output_0.is_active_output = True
if hasattr(material_output_0, 'location'):
    material_output_0.location = (880.0, 0.0)
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

separate_rgb_0 = node_tree0.nodes.new('ShaderNodeSeparateRGB')
if hasattr(separate_rgb_0, 'color'):
    separate_rgb_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(separate_rgb_0, 'hide'):
    separate_rgb_0.hide = False
if hasattr(separate_rgb_0, 'location'):
    separate_rgb_0.location = (-660.0, -20.0)
if hasattr(separate_rgb_0, 'mute'):
    separate_rgb_0.mute = False
if hasattr(separate_rgb_0, 'name'):
    separate_rgb_0.name = 'Separate RGB'
if hasattr(separate_rgb_0, 'use_custom_color'):
    separate_rgb_0.use_custom_color = False
if hasattr(separate_rgb_0, 'width'):
    separate_rgb_0.width = 140.0
separate_rgb_0.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
separate_rgb_0.outputs[0].default_value = 0.0
separate_rgb_0.outputs[1].default_value = 0.0
separate_rgb_0.outputs[2].default_value = 0.0

colorramp_0 = node_tree0.nodes.new('ShaderNodeValToRGB')
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
            colorramp_0.color_ramp.elements.new(1.0)
        if hasattr(colorramp_0.color_ramp.elements[1], 'alpha'):
            colorramp_0.color_ramp.elements[1].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[1], 'color'):
            colorramp_0.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[1], 'position'):
            colorramp_0.color_ramp.elements[1].position = 1.0
    if hasattr(colorramp_0.color_ramp, 'hue_interpolation'):
        colorramp_0.color_ramp.hue_interpolation = 'NEAR'
    if hasattr(colorramp_0.color_ramp, 'interpolation'):
        colorramp_0.color_ramp.interpolation = 'LINEAR'
if hasattr(colorramp_0, 'hide'):
    colorramp_0.hide = False
if hasattr(colorramp_0, 'location'):
    colorramp_0.location = (240.0, 60.0)
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

geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_0, 'color'):
    geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_0, 'hide'):
    geometry_0.hide = False
if hasattr(geometry_0, 'location'):
    geometry_0.location = (520.0, 60.0)
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
    emission_0.location = (520.0, 0.0)
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
    emission_001_0.location = (520.0, -100.0)
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
    mix_shader_0.location = (700.0, 0.0)
if hasattr(mix_shader_0, 'mute'):
    mix_shader_0.mute = False
if hasattr(mix_shader_0, 'name'):
    mix_shader_0.name = 'Mix Shader'
if hasattr(mix_shader_0, 'use_custom_color'):
    mix_shader_0.use_custom_color = False
if hasattr(mix_shader_0, 'width'):
    mix_shader_0.width = 140.0
mix_shader_0.inputs[0].default_value = 0.5

math_003_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_003_0, 'color'):
    math_003_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_003_0, 'hide'):
    math_003_0.hide = False
if hasattr(math_003_0, 'location'):
    math_003_0.location = (60.0, 60.0)
if hasattr(math_003_0, 'mute'):
    math_003_0.mute = False
if hasattr(math_003_0, 'name'):
    math_003_0.name = 'Math.003'
if hasattr(math_003_0, 'operation'):
    math_003_0.operation = 'MULTIPLY'
if hasattr(math_003_0, 'use_clamp'):
    math_003_0.use_clamp = False
if hasattr(math_003_0, 'use_custom_color'):
    math_003_0.use_custom_color = False
if hasattr(math_003_0, 'width'):
    math_003_0.width = 140.0
math_003_0.inputs[0].default_value = -1.0
math_003_0.inputs[1].default_value = 0.5
math_003_0.inputs[2].default_value = 0.0
math_003_0.outputs[0].default_value = 0.0

math_002_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_002_0, 'color'):
    math_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_002_0, 'hide'):
    math_002_0.hide = False
if hasattr(math_002_0, 'location'):
    math_002_0.location = (-120.0, 60.0)
if hasattr(math_002_0, 'mute'):
    math_002_0.mute = False
if hasattr(math_002_0, 'name'):
    math_002_0.name = 'Math.002'
if hasattr(math_002_0, 'operation'):
    math_002_0.operation = 'ADD'
if hasattr(math_002_0, 'use_clamp'):
    math_002_0.use_clamp = False
if hasattr(math_002_0, 'use_custom_color'):
    math_002_0.use_custom_color = False
if hasattr(math_002_0, 'width'):
    math_002_0.width = 140.0
math_002_0.inputs[0].default_value = -1.0
math_002_0.inputs[1].default_value = 1.0
math_002_0.inputs[2].default_value = 0.0
math_002_0.outputs[0].default_value = 0.0

math_001_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_001_0, 'color'):
    math_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_001_0, 'hide'):
    math_001_0.hide = False
if hasattr(math_001_0, 'location'):
    math_001_0.location = (-300.0, 60.0)
if hasattr(math_001_0, 'mute'):
    math_001_0.mute = False
if hasattr(math_001_0, 'name'):
    math_001_0.name = 'Math.001'
if hasattr(math_001_0, 'operation'):
    math_001_0.operation = 'ADD'
if hasattr(math_001_0, 'use_clamp'):
    math_001_0.use_clamp = False
if hasattr(math_001_0, 'use_custom_color'):
    math_001_0.use_custom_color = False
if hasattr(math_001_0, 'width'):
    math_001_0.width = 140.0
math_001_0.inputs[0].default_value = -1.0
math_001_0.inputs[1].default_value = 0.5
math_001_0.inputs[2].default_value = 0.0
math_001_0.outputs[0].default_value = 0.0

math_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_0, 'color'):
    math_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_0, 'hide'):
    math_0.hide = False
if hasattr(math_0, 'location'):
    math_0.location = (-480.0, 80.0)
if hasattr(math_0, 'mute'):
    math_0.mute = False
if hasattr(math_0, 'name'):
    math_0.name = 'Math'
if hasattr(math_0, 'operation'):
    math_0.operation = 'MULTIPLY'
if hasattr(math_0, 'use_clamp'):
    math_0.use_clamp = False
if hasattr(math_0, 'use_custom_color'):
    math_0.use_custom_color = False
if hasattr(math_0, 'width'):
    math_0.width = 140.0
math_0.inputs[0].default_value = -1.0
math_0.inputs[1].default_value = 0.5
math_0.inputs[2].default_value = 0.0
math_0.outputs[0].default_value = 0.0

# LINKS
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(vertex_color_0.outputs[0], separate_rgb_0.inputs[0])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(separate_rgb_0.outputs[0], math_0.inputs[1])
node_tree0.links.new(math_001_0.outputs[0], math_002_0.inputs[0])
node_tree0.links.new(separate_rgb_0.outputs[1], math_001_0.inputs[1])
node_tree0.links.new(math_0.outputs[0], math_001_0.inputs[0])
node_tree0.links.new(math_002_0.outputs[0], math_003_0.inputs[0])
node_tree0.links.new(math_003_0.outputs[0], colorramp_0.inputs[0])
node_tree0.links.new(colorramp_0.outputs[0], emission_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r3_ec
