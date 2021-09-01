import bpy

# MATERIAL
r3_deviation_map = bpy.data.materials.new(name='r3_deviation_map')
r3_deviation_map.use_nodes = True
node_tree0 = r3_deviation_map.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
vertex_color_0 = node_tree0.nodes.new('ShaderNodeVertexColor')
if hasattr(vertex_color_0, 'active_preview'):
    vertex_color_0.active_preview = False
if hasattr(vertex_color_0, 'color'):
    vertex_color_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(vertex_color_0, 'hide'):
    vertex_color_0.hide = False
if hasattr(vertex_color_0, 'layer_name'):
    vertex_color_0.layer_name = 'DM2-10cm'
if hasattr(vertex_color_0, 'location'):
    vertex_color_0.location = (-220.0, 20.0)
if hasattr(vertex_color_0, 'mute'):
    vertex_color_0.mute = False
if hasattr(vertex_color_0, 'name'):
    vertex_color_0.name = 'Vertex Color'
if hasattr(vertex_color_0, 'use_custom_color'):
    vertex_color_0.use_custom_color = False
if hasattr(vertex_color_0, 'width'):
    vertex_color_0.width = 172.864990234375
vertex_color_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
vertex_color_0.outputs[1].default_value = 0.0

value_0 = node_tree0.nodes.new('ShaderNodeValue')
if hasattr(value_0, 'active_preview'):
    value_0.active_preview = False
if hasattr(value_0, 'color'):
    value_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(value_0, 'hide'):
    value_0.hide = False
if hasattr(value_0, 'label'):
    value_0.label = 'Extreme Value (in mm)'
if hasattr(value_0, 'location'):
    value_0.location = (-180.0, -120.0)
if hasattr(value_0, 'mute'):
    value_0.mute = False
if hasattr(value_0, 'name'):
    value_0.name = 'Value'
if hasattr(value_0, 'use_custom_color'):
    value_0.use_custom_color = False
if hasattr(value_0, 'width'):
    value_0.width = 140.0
value_0.outputs[0].default_value = 6.0

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

node_tree1 = bpy.data.node_groups.get('NodeGroup')
if not node_tree1:
    node_tree1 = bpy.data.node_groups.new('NodeGroup', 'ShaderNodeTree')
    # INPUTS
    node_tree1.inputs.new('NodeSocketColor', 'Image')
    node_tree1.inputs.new('NodeSocketFloat', 'Value')
    # OUTPUTS
    node_tree1.outputs.new('NodeSocketShader', 'Shader')
    # NODES
    group_input_1 = node_tree1.nodes.new('NodeGroupInput')
    if hasattr(group_input_1, 'active_preview'):
        group_input_1.active_preview = False
    if hasattr(group_input_1, 'color'):
        group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(group_input_1, 'hide'):
        group_input_1.hide = False
    if hasattr(group_input_1, 'location'):
        group_input_1.location = (-980.0, -0.0)
    if hasattr(group_input_1, 'mute'):
        group_input_1.mute = False
    if hasattr(group_input_1, 'name'):
        group_input_1.name = 'Group Input'
    if hasattr(group_input_1, 'use_custom_color'):
        group_input_1.use_custom_color = False
    if hasattr(group_input_1, 'width'):
        group_input_1.width = 140.0
    group_input_1.outputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    group_input_1.outputs[1].default_value = 0.5

    separate_rgb_1 = node_tree1.nodes.new('ShaderNodeSeparateRGB')
    if hasattr(separate_rgb_1, 'active_preview'):
        separate_rgb_1.active_preview = False
    if hasattr(separate_rgb_1, 'color'):
        separate_rgb_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(separate_rgb_1, 'hide'):
        separate_rgb_1.hide = False
    if hasattr(separate_rgb_1, 'location'):
        separate_rgb_1.location = (-780.0, -10.0)
    if hasattr(separate_rgb_1, 'mute'):
        separate_rgb_1.mute = False
    if hasattr(separate_rgb_1, 'name'):
        separate_rgb_1.name = 'Separate RGB'
    if hasattr(separate_rgb_1, 'use_custom_color'):
        separate_rgb_1.use_custom_color = False
    if hasattr(separate_rgb_1, 'width'):
        separate_rgb_1.width = 140.0
    separate_rgb_1.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    separate_rgb_1.outputs[0].default_value = 0.0
    separate_rgb_1.outputs[1].default_value = 0.0
    separate_rgb_1.outputs[2].default_value = 0.0

    math_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_1, 'active_preview'):
        math_1.active_preview = False
    if hasattr(math_1, 'color'):
        math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_1, 'hide'):
        math_1.hide = False
    if hasattr(math_1, 'location'):
        math_1.location = (-580.0, 110.0)
    if hasattr(math_1, 'mute'):
        math_1.mute = False
    if hasattr(math_1, 'name'):
        math_1.name = 'Math'
    if hasattr(math_1, 'operation'):
        math_1.operation = 'MULTIPLY'
    if hasattr(math_1, 'use_clamp'):
        math_1.use_clamp = False
    if hasattr(math_1, 'use_custom_color'):
        math_1.use_custom_color = False
    if hasattr(math_1, 'width'):
        math_1.width = 140.0
    math_1.inputs[0].default_value = -1.0
    math_1.inputs[1].default_value = 0.5
    math_1.inputs[2].default_value = 0.0
    math_1.outputs[0].default_value = 0.0

    math_001_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_001_1, 'active_preview'):
        math_001_1.active_preview = False
    if hasattr(math_001_1, 'color'):
        math_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_001_1, 'hide'):
        math_001_1.hide = False
    if hasattr(math_001_1, 'location'):
        math_001_1.location = (-400.0, 70.0)
    if hasattr(math_001_1, 'mute'):
        math_001_1.mute = False
    if hasattr(math_001_1, 'name'):
        math_001_1.name = 'Math.001'
    if hasattr(math_001_1, 'operation'):
        math_001_1.operation = 'ADD'
    if hasattr(math_001_1, 'use_clamp'):
        math_001_1.use_clamp = False
    if hasattr(math_001_1, 'use_custom_color'):
        math_001_1.use_custom_color = False
    if hasattr(math_001_1, 'width'):
        math_001_1.width = 140.0
    math_001_1.inputs[0].default_value = -1.0
    math_001_1.inputs[1].default_value = 0.5
    math_001_1.inputs[2].default_value = 0.0
    math_001_1.outputs[0].default_value = 0.0

    math_002_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_002_1, 'active_preview'):
        math_002_1.active_preview = False
    if hasattr(math_002_1, 'color'):
        math_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_002_1, 'hide'):
        math_002_1.hide = False
    if hasattr(math_002_1, 'location'):
        math_002_1.location = (-220.0, 70.0)
    if hasattr(math_002_1, 'mute'):
        math_002_1.mute = False
    if hasattr(math_002_1, 'name'):
        math_002_1.name = 'Math.002'
    if hasattr(math_002_1, 'operation'):
        math_002_1.operation = 'ADD'
    if hasattr(math_002_1, 'use_clamp'):
        math_002_1.use_clamp = False
    if hasattr(math_002_1, 'use_custom_color'):
        math_002_1.use_custom_color = False
    if hasattr(math_002_1, 'width'):
        math_002_1.width = 140.0
    math_002_1.inputs[0].default_value = -1.0
    math_002_1.inputs[1].default_value = 1.0
    math_002_1.inputs[2].default_value = 0.0
    math_002_1.outputs[0].default_value = 0.0

    math_003_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_003_1, 'active_preview'):
        math_003_1.active_preview = False
    if hasattr(math_003_1, 'color'):
        math_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_003_1, 'hide'):
        math_003_1.hide = False
    if hasattr(math_003_1, 'location'):
        math_003_1.location = (-40.0, 70.0)
    if hasattr(math_003_1, 'mute'):
        math_003_1.mute = False
    if hasattr(math_003_1, 'name'):
        math_003_1.name = 'Math.003'
    if hasattr(math_003_1, 'operation'):
        math_003_1.operation = 'MULTIPLY'
    if hasattr(math_003_1, 'use_clamp'):
        math_003_1.use_clamp = False
    if hasattr(math_003_1, 'use_custom_color'):
        math_003_1.use_custom_color = False
    if hasattr(math_003_1, 'width'):
        math_003_1.width = 140.0
    math_003_1.inputs[0].default_value = -1.0
    math_003_1.inputs[1].default_value = 0.5
    math_003_1.inputs[2].default_value = 0.0
    math_003_1.outputs[0].default_value = 0.0

    math_004_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_004_1, 'active_preview'):
        math_004_1.active_preview = False
    if hasattr(math_004_1, 'color'):
        math_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_004_1, 'hide'):
        math_004_1.hide = False
    if hasattr(math_004_1, 'location'):
        math_004_1.location = (-40.0, -250.0)
    if hasattr(math_004_1, 'mute'):
        math_004_1.mute = False
    if hasattr(math_004_1, 'name'):
        math_004_1.name = 'Math.004'
    if hasattr(math_004_1, 'operation'):
        math_004_1.operation = 'ADD'
    if hasattr(math_004_1, 'use_clamp'):
        math_004_1.use_clamp = False
    if hasattr(math_004_1, 'use_custom_color'):
        math_004_1.use_custom_color = False
    if hasattr(math_004_1, 'width'):
        math_004_1.width = 140.0
    math_004_1.inputs[0].default_value = 0.5
    math_004_1.inputs[1].default_value = 0.5
    math_004_1.inputs[2].default_value = 0.0
    math_004_1.outputs[0].default_value = 0.0

    math_006_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_006_1, 'active_preview'):
        math_006_1.active_preview = False
    if hasattr(math_006_1, 'color'):
        math_006_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_006_1, 'hide'):
        math_006_1.hide = False
    if hasattr(math_006_1, 'location'):
        math_006_1.location = (-240.0, -230.0)
    if hasattr(math_006_1, 'mute'):
        math_006_1.mute = False
    if hasattr(math_006_1, 'name'):
        math_006_1.name = 'Math.006'
    if hasattr(math_006_1, 'operation'):
        math_006_1.operation = 'DIVIDE'
    if hasattr(math_006_1, 'use_clamp'):
        math_006_1.use_clamp = False
    if hasattr(math_006_1, 'use_custom_color'):
        math_006_1.use_custom_color = False
    if hasattr(math_006_1, 'width'):
        math_006_1.width = 140.0
    math_006_1.inputs[0].default_value = 0.5
    math_006_1.inputs[1].default_value = 100.0
    math_006_1.inputs[2].default_value = 0.0
    math_006_1.outputs[0].default_value = 0.0

    math_005_1 = node_tree1.nodes.new('ShaderNodeMath')
    if hasattr(math_005_1, 'active_preview'):
        math_005_1.active_preview = False
    if hasattr(math_005_1, 'color'):
        math_005_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(math_005_1, 'hide'):
        math_005_1.hide = False
    if hasattr(math_005_1, 'location'):
        math_005_1.location = (-40.0, -90.0)
    if hasattr(math_005_1, 'mute'):
        math_005_1.mute = False
    if hasattr(math_005_1, 'name'):
        math_005_1.name = 'Math.005'
    if hasattr(math_005_1, 'operation'):
        math_005_1.operation = 'SUBTRACT'
    if hasattr(math_005_1, 'use_clamp'):
        math_005_1.use_clamp = False
    if hasattr(math_005_1, 'use_custom_color'):
        math_005_1.use_custom_color = False
    if hasattr(math_005_1, 'width'):
        math_005_1.width = 140.0
    math_005_1.inputs[0].default_value = 0.5
    math_005_1.inputs[1].default_value = 0.5
    math_005_1.inputs[2].default_value = 0.0
    math_005_1.outputs[0].default_value = 0.0

    map_range_1 = node_tree1.nodes.new('ShaderNodeMapRange')
    if hasattr(map_range_1, 'active_preview'):
        map_range_1.active_preview = False
    if hasattr(map_range_1, 'clamp'):
        map_range_1.clamp = False
    if hasattr(map_range_1, 'color'):
        map_range_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(map_range_1, 'hide'):
        map_range_1.hide = False
    if hasattr(map_range_1, 'interpolation_type'):
        map_range_1.interpolation_type = 'LINEAR'
    if hasattr(map_range_1, 'location'):
        map_range_1.location = (140.0, 10.0)
    if hasattr(map_range_1, 'mute'):
        map_range_1.mute = False
    if hasattr(map_range_1, 'name'):
        map_range_1.name = 'Map Range'
    if hasattr(map_range_1, 'use_custom_color'):
        map_range_1.use_custom_color = False
    if hasattr(map_range_1, 'width'):
        map_range_1.width = 140.0
    map_range_1.inputs[0].default_value = 1.0
    map_range_1.inputs[1].default_value = 0.4000000059604645
    map_range_1.inputs[2].default_value = 0.6000000238418579
    map_range_1.inputs[3].default_value = 0.0
    map_range_1.inputs[4].default_value = 1.0
    map_range_1.inputs[5].default_value = 4.0
    map_range_1.outputs[0].default_value = 0.0

    colorramp_1 = node_tree1.nodes.new('ShaderNodeValToRGB')
    if hasattr(colorramp_1, 'active_preview'):
        colorramp_1.active_preview = False
    if hasattr(colorramp_1, 'color'):
        colorramp_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(colorramp_1, 'color_ramp'):
        if hasattr(colorramp_1.color_ramp, 'color_mode'):
            colorramp_1.color_ramp.color_mode = 'RGB'
        if hasattr(colorramp_1.color_ramp, 'elements'):
            if 0 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(0.0)
            if hasattr(colorramp_1.color_ramp.elements[0], 'alpha'):
                colorramp_1.color_ramp.elements[0].alpha = 1.0
            if hasattr(colorramp_1.color_ramp.elements[0], 'color'):
                colorramp_1.color_ramp.elements[0].color = (1.0, 0.0, 0.0, 1.0)
            if hasattr(colorramp_1.color_ramp.elements[0], 'position'):
                colorramp_1.color_ramp.elements[0].position = 0.0
            if 1 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(0.009999999776482582)
            if hasattr(colorramp_1.color_ramp.elements[1], 'alpha'):
                colorramp_1.color_ramp.elements[1].alpha = 1.0
            if hasattr(colorramp_1.color_ramp.elements[1], 'color'):
                colorramp_1.color_ramp.elements[1].color = (0.0, 0.0, 0.0, 1.0)
            if hasattr(colorramp_1.color_ramp.elements[1], 'position'):
                colorramp_1.color_ramp.elements[1].position = 0.009999999776482582
            if 2 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(0.9900000095367432)
            if hasattr(colorramp_1.color_ramp.elements[2], 'alpha'):
                colorramp_1.color_ramp.elements[2].alpha = 1.0
            if hasattr(colorramp_1.color_ramp.elements[2], 'color'):
                colorramp_1.color_ramp.elements[2].color = (1.0, 1.0, 1.0, 1.0)
            if hasattr(colorramp_1.color_ramp.elements[2], 'position'):
                colorramp_1.color_ramp.elements[2].position = 0.9900000095367432
            if 3 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(1.0)
            if hasattr(colorramp_1.color_ramp.elements[3], 'alpha'):
                colorramp_1.color_ramp.elements[3].alpha = 1.0
            if hasattr(colorramp_1.color_ramp.elements[3], 'color'):
                colorramp_1.color_ramp.elements[3].color = (1.0, 0.0, 0.0, 1.0)
            if hasattr(colorramp_1.color_ramp.elements[3], 'position'):
                colorramp_1.color_ramp.elements[3].position = 1.0
        if hasattr(colorramp_1.color_ramp, 'hue_interpolation'):
            colorramp_1.color_ramp.hue_interpolation = 'NEAR'
        if hasattr(colorramp_1.color_ramp, 'interpolation'):
            colorramp_1.color_ramp.interpolation = 'LINEAR'
    if hasattr(colorramp_1, 'hide'):
        colorramp_1.hide = False
    if hasattr(colorramp_1, 'location'):
        colorramp_1.location = (320.0, 10.0)
    if hasattr(colorramp_1, 'mute'):
        colorramp_1.mute = False
    if hasattr(colorramp_1, 'name'):
        colorramp_1.name = 'ColorRamp'
    if hasattr(colorramp_1, 'use_custom_color'):
        colorramp_1.use_custom_color = False
    if hasattr(colorramp_1, 'width'):
        colorramp_1.width = 240.0
    colorramp_1.inputs[0].default_value = 0.5
    colorramp_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    colorramp_1.outputs[1].default_value = 0.0

    geometry_1 = node_tree1.nodes.new('ShaderNodeNewGeometry')
    if hasattr(geometry_1, 'active_preview'):
        geometry_1.active_preview = False
    if hasattr(geometry_1, 'color'):
        geometry_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(geometry_1, 'hide'):
        geometry_1.hide = False
    if hasattr(geometry_1, 'location'):
        geometry_1.location = (600.0, 250.0)
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

    emission_1 = node_tree1.nodes.new('ShaderNodeEmission')
    if hasattr(emission_1, 'active_preview'):
        emission_1.active_preview = False
    if hasattr(emission_1, 'color'):
        emission_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(emission_1, 'hide'):
        emission_1.hide = False
    if hasattr(emission_1, 'location'):
        emission_1.location = (600.0, 10.0)
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
        emission_001_1.location = (600.0, -110.0)
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

    mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
    if hasattr(mix_shader_1, 'active_preview'):
        mix_shader_1.active_preview = False
    if hasattr(mix_shader_1, 'color'):
        mix_shader_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(mix_shader_1, 'hide'):
        mix_shader_1.hide = False
    if hasattr(mix_shader_1, 'location'):
        mix_shader_1.location = (780.0, 50.0)
    if hasattr(mix_shader_1, 'mute'):
        mix_shader_1.mute = False
    if hasattr(mix_shader_1, 'name'):
        mix_shader_1.name = 'Mix Shader'
    if hasattr(mix_shader_1, 'use_custom_color'):
        mix_shader_1.use_custom_color = False
    if hasattr(mix_shader_1, 'width'):
        mix_shader_1.width = 140.0
    mix_shader_1.inputs[0].default_value = 0.5

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
        group_output_1.location = (970.0, -0.0)
    if hasattr(group_output_1, 'mute'):
        group_output_1.mute = False
    if hasattr(group_output_1, 'name'):
        group_output_1.name = 'Group Output'
    if hasattr(group_output_1, 'use_custom_color'):
        group_output_1.use_custom_color = False
    if hasattr(group_output_1, 'width'):
        group_output_1.width = 140.0

    # LINKS
    node_tree1.links.new(group_input_1.outputs[0], separate_rgb_1.inputs[0])
    node_tree1.links.new(mix_shader_1.outputs[0], group_output_1.inputs[0])
    node_tree1.links.new(group_input_1.outputs[1], math_006_1.inputs[0])
    node_tree1.links.new(emission_001_1.outputs[0], mix_shader_1.inputs[2])
    node_tree1.links.new(geometry_1.outputs[6], mix_shader_1.inputs[0])
    node_tree1.links.new(math_1.outputs[0], math_001_1.inputs[0])
    node_tree1.links.new(math_001_1.outputs[0], math_002_1.inputs[0])
    node_tree1.links.new(math_002_1.outputs[0], math_003_1.inputs[0])
    node_tree1.links.new(math_003_1.outputs[0], map_range_1.inputs[0])
    node_tree1.links.new(emission_1.outputs[0], mix_shader_1.inputs[1])
    node_tree1.links.new(separate_rgb_1.outputs[0], math_1.inputs[1])
    node_tree1.links.new(separate_rgb_1.outputs[1], math_001_1.inputs[1])
    node_tree1.links.new(map_range_1.outputs[0], colorramp_1.inputs[0])
    node_tree1.links.new(math_006_1.outputs[0], math_005_1.inputs[1])
    node_tree1.links.new(math_006_1.outputs[0], math_004_1.inputs[1])
    node_tree1.links.new(math_004_1.outputs[0], map_range_1.inputs[2])
    node_tree1.links.new(math_005_1.outputs[0], map_range_1.inputs[1])
    node_tree1.links.new(colorramp_1.outputs[0], emission_1.inputs[0])

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
    group_0.location = (0.0, 0.0)
if hasattr(group_0, 'mute'):
    group_0.mute = False
if hasattr(group_0, 'name'):
    group_0.name = 'Group'
if hasattr(group_0, 'use_custom_color'):
    group_0.use_custom_color = False
if hasattr(group_0, 'width'):
    group_0.width = 140.0
group_0.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
group_0.inputs[1].default_value = 0.5

# LINKS
node_tree0.links.new(vertex_color_0.outputs[0], group_0.inputs[0])
node_tree0.links.new(group_0.outputs[0], material_output_0.inputs[0])
node_tree0.links.new(value_0.outputs[0], group_0.inputs[1])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = r3_deviation_map

# FAKE USER
bpy.data.materials['r3_deviation_map'].use_fake_user = True