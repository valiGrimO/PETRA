import bpy

# MATERIAL
r5_aspect = bpy.data.materials.new(name='r5_aspect')
r5_aspect.use_nodes = True
node_tree0 = r5_aspect.node_tree
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
            colorramp_0.color_ramp.elements.new(0.0)
        if hasattr(colorramp_0.color_ramp.elements[0], 'alpha'):
            colorramp_0.color_ramp.elements[0].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[0], 'color'):
            colorramp_0.color_ramp.elements[0].color = (1.0, 0.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[0], 'position'):
            colorramp_0.color_ramp.elements[0].position = 0.0
        if 1 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.0625)
        if hasattr(colorramp_0.color_ramp.elements[1], 'alpha'):
            colorramp_0.color_ramp.elements[1].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[1], 'color'):
            colorramp_0.color_ramp.elements[1].color = (1.0, 0.5, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[1], 'position'):
            colorramp_0.color_ramp.elements[1].position = 0.0625
        if 2 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.1875)
        if hasattr(colorramp_0.color_ramp.elements[2], 'alpha'):
            colorramp_0.color_ramp.elements[2].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[2], 'color'):
            colorramp_0.color_ramp.elements[2].color = (1.0, 1.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[2], 'position'):
            colorramp_0.color_ramp.elements[2].position = 0.1875
        if 3 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.3125)
        if hasattr(colorramp_0.color_ramp.elements[3], 'alpha'):
            colorramp_0.color_ramp.elements[3].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[3], 'color'):
            colorramp_0.color_ramp.elements[3].color = (0.0, 1.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[3], 'position'):
            colorramp_0.color_ramp.elements[3].position = 0.3125
        if 4 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.4375)
        if hasattr(colorramp_0.color_ramp.elements[4], 'alpha'):
            colorramp_0.color_ramp.elements[4].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[4], 'color'):
            colorramp_0.color_ramp.elements[4].color = (0.0, 1.0, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[4], 'position'):
            colorramp_0.color_ramp.elements[4].position = 0.4375
        if 5 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.5625)
        if hasattr(colorramp_0.color_ramp.elements[5], 'alpha'):
            colorramp_0.color_ramp.elements[5].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[5], 'color'):
            colorramp_0.color_ramp.elements[5].color = (0.0, 0.5, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[5], 'position'):
            colorramp_0.color_ramp.elements[5].position = 0.5625
        if 6 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.6875)
        if hasattr(colorramp_0.color_ramp.elements[6], 'alpha'):
            colorramp_0.color_ramp.elements[6].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[6], 'color'):
            colorramp_0.color_ramp.elements[6].color = (0.0, 0.0, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[6], 'position'):
            colorramp_0.color_ramp.elements[6].position = 0.6875
        if 7 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.8125)
        if hasattr(colorramp_0.color_ramp.elements[7], 'alpha'):
            colorramp_0.color_ramp.elements[7].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[7], 'color'):
            colorramp_0.color_ramp.elements[7].color = (1.0, 0.0, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[7], 'position'):
            colorramp_0.color_ramp.elements[7].position = 0.8125
        if 8 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.9375)
        if hasattr(colorramp_0.color_ramp.elements[8], 'alpha'):
            colorramp_0.color_ramp.elements[8].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[8], 'color'):
            colorramp_0.color_ramp.elements[8].color = (1.0, 0.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[8], 'position'):
            colorramp_0.color_ramp.elements[8].position = 0.9375
    if hasattr(colorramp_0.color_ramp, 'hue_interpolation'):
        colorramp_0.color_ramp.hue_interpolation = 'NEAR'
    if hasattr(colorramp_0.color_ramp, 'interpolation'):
        colorramp_0.color_ramp.interpolation = 'CONSTANT'
if hasattr(colorramp_0, 'hide'):
    colorramp_0.hide = False
if hasattr(colorramp_0, 'location'):
    colorramp_0.location = (-460.0, 0.0)
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

math_011_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_011_0, 'active_preview'):
    math_011_0.active_preview = False
if hasattr(math_011_0, 'color'):
    math_011_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_011_0, 'hide'):
    math_011_0.hide = False
if hasattr(math_011_0, 'label'):
    math_011_0.label = 'Normalize'
if hasattr(math_011_0, 'location'):
    math_011_0.location = (-640.0, 0.0)
if hasattr(math_011_0, 'mute'):
    math_011_0.mute = False
if hasattr(math_011_0, 'name'):
    math_011_0.name = 'Math.011'
if hasattr(math_011_0, 'operation'):
    math_011_0.operation = 'DIVIDE'
if hasattr(math_011_0, 'use_clamp'):
    math_011_0.use_clamp = False
if hasattr(math_011_0, 'use_custom_color'):
    math_011_0.use_custom_color = False
if hasattr(math_011_0, 'width'):
    math_011_0.width = 140.0
math_011_0.inputs[0].default_value = 0.5
math_011_0.inputs[1].default_value = 360.0
math_011_0.inputs[2].default_value = 0.0
math_011_0.outputs[0].default_value = 0.0

math_010_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_010_0, 'active_preview'):
    math_010_0.active_preview = False
if hasattr(math_010_0, 'color'):
    math_010_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_010_0, 'hide'):
    math_010_0.hide = False
if hasattr(math_010_0, 'location'):
    math_010_0.location = (-820.0, 0.0)
if hasattr(math_010_0, 'mute'):
    math_010_0.mute = False
if hasattr(math_010_0, 'name'):
    math_010_0.name = 'Math.010'
if hasattr(math_010_0, 'operation'):
    math_010_0.operation = 'ADD'
if hasattr(math_010_0, 'use_clamp'):
    math_010_0.use_clamp = False
if hasattr(math_010_0, 'use_custom_color'):
    math_010_0.use_custom_color = False
if hasattr(math_010_0, 'width'):
    math_010_0.width = 140.0
math_010_0.inputs[0].default_value = 0.5
math_010_0.inputs[1].default_value = 0.5
math_010_0.inputs[2].default_value = 0.0
math_010_0.outputs[0].default_value = 0.0

math_005_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_005_0, 'active_preview'):
    math_005_0.active_preview = False
if hasattr(math_005_0, 'color'):
    math_005_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_005_0, 'hide'):
    math_005_0.hide = False
if hasattr(math_005_0, 'location'):
    math_005_0.location = (-1000.0, -180.0)
if hasattr(math_005_0, 'mute'):
    math_005_0.mute = False
if hasattr(math_005_0, 'name'):
    math_005_0.name = 'Math.005'
if hasattr(math_005_0, 'operation'):
    math_005_0.operation = 'ADD'
if hasattr(math_005_0, 'use_clamp'):
    math_005_0.use_clamp = False
if hasattr(math_005_0, 'use_custom_color'):
    math_005_0.use_custom_color = False
if hasattr(math_005_0, 'width'):
    math_005_0.width = 140.0
math_005_0.inputs[0].default_value = 0.5
math_005_0.inputs[1].default_value = 0.5
math_005_0.inputs[2].default_value = 0.0
math_005_0.outputs[0].default_value = 0.0

math_002_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_002_0, 'active_preview'):
    math_002_0.active_preview = False
if hasattr(math_002_0, 'color'):
    math_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_002_0, 'hide'):
    math_002_0.hide = False
if hasattr(math_002_0, 'label'):
    math_002_0.label = 'Aspect degrees'
if hasattr(math_002_0, 'location'):
    math_002_0.location = (-1180.0, -380.0)
if hasattr(math_002_0, 'mute'):
    math_002_0.mute = False
if hasattr(math_002_0, 'name'):
    math_002_0.name = 'Math.002'
if hasattr(math_002_0, 'operation'):
    math_002_0.operation = 'MULTIPLY'
if hasattr(math_002_0, 'use_clamp'):
    math_002_0.use_clamp = False
if hasattr(math_002_0, 'use_custom_color'):
    math_002_0.use_custom_color = False
if hasattr(math_002_0, 'width'):
    math_002_0.width = 140.0
math_002_0.inputs[0].default_value = 0.5
math_002_0.inputs[1].default_value = 57.295780181884766
math_002_0.inputs[2].default_value = 0.0
math_002_0.outputs[0].default_value = 0.0

math_004_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_004_0, 'active_preview'):
    math_004_0.active_preview = False
if hasattr(math_004_0, 'color'):
    math_004_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_004_0, 'hide'):
    math_004_0.hide = False
if hasattr(math_004_0, 'location'):
    math_004_0.location = (-1180.0, -180.0)
if hasattr(math_004_0, 'mute'):
    math_004_0.mute = False
if hasattr(math_004_0, 'name'):
    math_004_0.name = 'Math.004'
if hasattr(math_004_0, 'operation'):
    math_004_0.operation = 'MULTIPLY'
if hasattr(math_004_0, 'use_clamp'):
    math_004_0.use_clamp = False
if hasattr(math_004_0, 'use_custom_color'):
    math_004_0.use_custom_color = False
if hasattr(math_004_0, 'width'):
    math_004_0.width = 140.0
math_004_0.inputs[0].default_value = 0.5
math_004_0.inputs[1].default_value = 180.0
math_004_0.inputs[2].default_value = 0.0
math_004_0.outputs[0].default_value = 0.0

math_001_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_001_0, 'active_preview'):
    math_001_0.active_preview = False
if hasattr(math_001_0, 'color'):
    math_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_001_0, 'hide'):
    math_001_0.hide = False
if hasattr(math_001_0, 'label'):
    math_001_0.label = 'Aspect radians'
if hasattr(math_001_0, 'location'):
    math_001_0.location = (-1360.0, -380.0)
if hasattr(math_001_0, 'mute'):
    math_001_0.mute = False
if hasattr(math_001_0, 'name'):
    math_001_0.name = 'Math.001'
if hasattr(math_001_0, 'operation'):
    math_001_0.operation = 'ARCTANGENT'
if hasattr(math_001_0, 'use_clamp'):
    math_001_0.use_clamp = False
if hasattr(math_001_0, 'use_custom_color'):
    math_001_0.use_custom_color = False
if hasattr(math_001_0, 'width'):
    math_001_0.width = 140.0
math_001_0.inputs[0].default_value = 0.5
math_001_0.inputs[1].default_value = 0.5
math_001_0.inputs[2].default_value = 0.0
math_001_0.outputs[0].default_value = 0.0

math_003_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_003_0, 'active_preview'):
    math_003_0.active_preview = False
if hasattr(math_003_0, 'color'):
    math_003_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_003_0, 'hide'):
    math_003_0.hide = False
if hasattr(math_003_0, 'label'):
    math_003_0.label = 'y negative ?'
if hasattr(math_003_0, 'location'):
    math_003_0.location = (-1360.0, -180.0)
if hasattr(math_003_0, 'mute'):
    math_003_0.mute = False
if hasattr(math_003_0, 'name'):
    math_003_0.name = 'Math.003'
if hasattr(math_003_0, 'operation'):
    math_003_0.operation = 'LESS_THAN'
if hasattr(math_003_0, 'use_clamp'):
    math_003_0.use_clamp = False
if hasattr(math_003_0, 'use_custom_color'):
    math_003_0.use_custom_color = False
if hasattr(math_003_0, 'width'):
    math_003_0.width = 140.0
math_003_0.inputs[0].default_value = 0.5
math_003_0.inputs[1].default_value = 0.0
math_003_0.inputs[2].default_value = 0.0
math_003_0.outputs[0].default_value = 0.0

math_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_0, 'active_preview'):
    math_0.active_preview = False
if hasattr(math_0, 'color'):
    math_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_0, 'hide'):
    math_0.hide = False
if hasattr(math_0, 'location'):
    math_0.location = (-1540.0, -380.0)
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
math_0.inputs[0].default_value = 0.5
math_0.inputs[1].default_value = 0.5
math_0.inputs[2].default_value = 0.0
math_0.outputs[0].default_value = 0.0

math_009_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_009_0, 'active_preview'):
    math_009_0.active_preview = False
if hasattr(math_009_0, 'color'):
    math_009_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_009_0, 'hide'):
    math_009_0.hide = False
if hasattr(math_009_0, 'location'):
    math_009_0.location = (-1180.0, 0.0)
if hasattr(math_009_0, 'mute'):
    math_009_0.mute = False
if hasattr(math_009_0, 'name'):
    math_009_0.name = 'Math.009'
if hasattr(math_009_0, 'operation'):
    math_009_0.operation = 'MULTIPLY'
if hasattr(math_009_0, 'use_clamp'):
    math_009_0.use_clamp = False
if hasattr(math_009_0, 'use_custom_color'):
    math_009_0.use_custom_color = False
if hasattr(math_009_0, 'width'):
    math_009_0.width = 140.0
math_009_0.inputs[0].default_value = 0.5
math_009_0.inputs[1].default_value = 360.0
math_009_0.inputs[2].default_value = 0.0
math_009_0.outputs[0].default_value = 0.0

math_008_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_008_0, 'active_preview'):
    math_008_0.active_preview = False
if hasattr(math_008_0, 'color'):
    math_008_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_008_0, 'hide'):
    math_008_0.hide = False
if hasattr(math_008_0, 'location'):
    math_008_0.location = (-1360.0, 0.0)
if hasattr(math_008_0, 'mute'):
    math_008_0.mute = False
if hasattr(math_008_0, 'name'):
    math_008_0.name = 'Math.008'
if hasattr(math_008_0, 'operation'):
    math_008_0.operation = 'MULTIPLY'
if hasattr(math_008_0, 'use_clamp'):
    math_008_0.use_clamp = False
if hasattr(math_008_0, 'use_custom_color'):
    math_008_0.use_custom_color = False
if hasattr(math_008_0, 'width'):
    math_008_0.width = 140.0
math_008_0.inputs[0].default_value = 0.5
math_008_0.inputs[1].default_value = 0.5
math_008_0.inputs[2].default_value = 0.0
math_008_0.outputs[0].default_value = 0.0

separate_xyz_0 = node_tree0.nodes.new('ShaderNodeSeparateXYZ')
if hasattr(separate_xyz_0, 'active_preview'):
    separate_xyz_0.active_preview = False
if hasattr(separate_xyz_0, 'color'):
    separate_xyz_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(separate_xyz_0, 'hide'):
    separate_xyz_0.hide = False
if hasattr(separate_xyz_0, 'location'):
    separate_xyz_0.location = (-1760.0, -260.0)
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
    vector_transform_0.location = (-1940.0, -260.0)
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

math_006_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_006_0, 'active_preview'):
    math_006_0.active_preview = False
if hasattr(math_006_0, 'color'):
    math_006_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_006_0, 'hide'):
    math_006_0.hide = False
if hasattr(math_006_0, 'label'):
    math_006_0.label = 'x negative ?'
if hasattr(math_006_0, 'location'):
    math_006_0.location = (-1540.0, 60.0)
if hasattr(math_006_0, 'mute'):
    math_006_0.mute = False
if hasattr(math_006_0, 'name'):
    math_006_0.name = 'Math.006'
if hasattr(math_006_0, 'operation'):
    math_006_0.operation = 'LESS_THAN'
if hasattr(math_006_0, 'use_clamp'):
    math_006_0.use_clamp = False
if hasattr(math_006_0, 'use_custom_color'):
    math_006_0.use_custom_color = False
if hasattr(math_006_0, 'width'):
    math_006_0.width = 140.0
math_006_0.inputs[0].default_value = 0.5
math_006_0.inputs[1].default_value = 0.0
math_006_0.inputs[2].default_value = 0.0
math_006_0.outputs[0].default_value = 0.0

math_007_0 = node_tree0.nodes.new('ShaderNodeMath')
if hasattr(math_007_0, 'active_preview'):
    math_007_0.active_preview = False
if hasattr(math_007_0, 'color'):
    math_007_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(math_007_0, 'hide'):
    math_007_0.hide = False
if hasattr(math_007_0, 'label'):
    math_007_0.label = 'y positive ?'
if hasattr(math_007_0, 'location'):
    math_007_0.location = (-1540.0, -120.0)
if hasattr(math_007_0, 'mute'):
    math_007_0.mute = False
if hasattr(math_007_0, 'name'):
    math_007_0.name = 'Math.007'
if hasattr(math_007_0, 'operation'):
    math_007_0.operation = 'GREATER_THAN'
if hasattr(math_007_0, 'use_clamp'):
    math_007_0.use_clamp = False
if hasattr(math_007_0, 'use_custom_color'):
    math_007_0.use_custom_color = False
if hasattr(math_007_0, 'width'):
    math_007_0.width = 140.0
math_007_0.inputs[0].default_value = 0.5
math_007_0.inputs[1].default_value = 0.0
math_007_0.inputs[2].default_value = 0.0
math_007_0.outputs[0].default_value = 0.0

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
    texture_coordinate_0.location = (-2120.0, -260.0)
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

emission_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_0, 'active_preview'):
    emission_0.active_preview = False
if hasattr(emission_0, 'color'):
    emission_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_0, 'hide'):
    emission_0.hide = False
if hasattr(emission_0, 'location'):
    emission_0.location = (-180.0, 0.0)
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
    emission_001_0.location = (-180.0, -120.0)
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
    mix_shader_0.location = (0.0, 0.0)
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

geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
if hasattr(geometry_0, 'active_preview'):
    geometry_0.active_preview = False
if hasattr(geometry_0, 'color'):
    geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(geometry_0, 'hide'):
    geometry_0.hide = False
if hasattr(geometry_0, 'location'):
    geometry_0.location = (-180.0, 240.0)
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

# LINKS
node_tree0.links.new(separate_xyz_0.outputs[0], math_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[1], math_0.inputs[1])
node_tree0.links.new(math_0.outputs[0], math_001_0.inputs[0])
node_tree0.links.new(math_001_0.outputs[0], math_002_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[1], math_003_0.inputs[0])
node_tree0.links.new(math_003_0.outputs[0], math_004_0.inputs[0])
node_tree0.links.new(math_004_0.outputs[0], math_005_0.inputs[0])
node_tree0.links.new(math_002_0.outputs[0], math_005_0.inputs[1])
node_tree0.links.new(separate_xyz_0.outputs[0], math_006_0.inputs[0])
node_tree0.links.new(separate_xyz_0.outputs[1], math_007_0.inputs[0])
node_tree0.links.new(math_006_0.outputs[0], math_008_0.inputs[0])
node_tree0.links.new(math_007_0.outputs[0], math_008_0.inputs[1])
node_tree0.links.new(math_008_0.outputs[0], math_009_0.inputs[0])
node_tree0.links.new(math_009_0.outputs[0], math_010_0.inputs[0])
node_tree0.links.new(math_005_0.outputs[0], math_010_0.inputs[1])
node_tree0.links.new(math_010_0.outputs[0], math_011_0.inputs[0])
node_tree0.links.new(math_011_0.outputs[0], colorramp_0.inputs[0])
node_tree0.links.new(vector_transform_0.outputs[0], separate_xyz_0.inputs[0])
node_tree0.links.new(texture_coordinate_0.outputs[1], vector_transform_0.inputs[0])
node_tree0.links.new(emission_0.outputs[0], mix_shader_0.inputs[1])
node_tree0.links.new(colorramp_0.outputs[0], emission_0.inputs[0])
node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(emission_001_0.outputs[0], mix_shader_0.inputs[2])
node_tree0.links.new(geometry_0.outputs[6], mix_shader_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r5_aspect
