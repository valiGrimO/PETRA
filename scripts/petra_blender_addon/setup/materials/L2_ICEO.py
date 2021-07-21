import bpy

# MATERIAL
iceo = bpy.data.materials.new(name='iceo')
iceo.use_nodes = True
node_tree0 = iceo.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
image_texture_001_0 = node_tree0.nodes.new('ShaderNodeTexImage')
if hasattr(image_texture_001_0, 'color'):
    image_texture_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(image_texture_001_0, 'extension'):
    image_texture_001_0.extension = 'REPEAT'
if hasattr(image_texture_001_0, 'hide'):
    image_texture_001_0.hide = False
if hasattr(image_texture_001_0, 'interpolation'):
    image_texture_001_0.interpolation = 'Linear'
if hasattr(image_texture_001_0, 'label'):
    image_texture_001_0.label = 'Cam-##_R3_EC2'
if hasattr(image_texture_001_0, 'location'):
    image_texture_001_0.location = (-420.0, -20.0)
if hasattr(image_texture_001_0, 'mute'):
    image_texture_001_0.mute = False
if hasattr(image_texture_001_0, 'name'):
    image_texture_001_0.name = 'Image Texture.001'
if hasattr(image_texture_001_0, 'projection'):
    image_texture_001_0.projection = 'FLAT'
if hasattr(image_texture_001_0, 'projection_blend'):
    image_texture_001_0.projection_blend = 0.0
if hasattr(image_texture_001_0, 'use_custom_color'):
    image_texture_001_0.use_custom_color = False
if hasattr(image_texture_001_0, 'width'):
    image_texture_001_0.width = 240.0
image_texture_001_0.inputs[0].default_value = (0.0, 0.0, 0.0)
image_texture_001_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
image_texture_001_0.outputs[1].default_value = 0.0

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
            colorramp_0.color_ramp.elements.new(0.20000000298023224)
        if hasattr(colorramp_0.color_ramp.elements[1], 'alpha'):
            colorramp_0.color_ramp.elements[1].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[1], 'color'):
            colorramp_0.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[1], 'position'):
            colorramp_0.color_ramp.elements[1].position = 0.20000000298023224
        if 2 >= len(colorramp_0.color_ramp.elements):
            colorramp_0.color_ramp.elements.new(0.7450000047683716)
        if hasattr(colorramp_0.color_ramp.elements[2], 'alpha'):
            colorramp_0.color_ramp.elements[2].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[2], 'color'):
            colorramp_0.color_ramp.elements[2].color = (0.0, 0.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[2], 'position'):
            colorramp_0.color_ramp.elements[2].position = 0.7450000047683716
    if hasattr(colorramp_0.color_ramp, 'hue_interpolation'):
        colorramp_0.color_ramp.hue_interpolation = 'NEAR'
    if hasattr(colorramp_0.color_ramp, 'interpolation'):
        colorramp_0.color_ramp.interpolation = 'CONSTANT'
if hasattr(colorramp_0, 'hide'):
    colorramp_0.hide = False
if hasattr(colorramp_0, 'location'):
    colorramp_0.location = (-920.0, -1400.0)
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

image_texture_0 = node_tree0.nodes.new('ShaderNodeTexImage')
if hasattr(image_texture_0, 'color'):
    image_texture_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(image_texture_0, 'extension'):
    image_texture_0.extension = 'REPEAT'
if hasattr(image_texture_0, 'hide'):
    image_texture_0.hide = False
if hasattr(image_texture_0, 'interpolation'):
    image_texture_0.interpolation = 'Linear'
if hasattr(image_texture_0, 'label'):
    image_texture_0.label = 'Cam-##_R1_NMC'
if hasattr(image_texture_0, 'location'):
    image_texture_0.location = (-420.0, 200.0)
if hasattr(image_texture_0, 'mute'):
    image_texture_0.mute = False
if hasattr(image_texture_0, 'name'):
    image_texture_0.name = 'Image Texture'
if hasattr(image_texture_0, 'projection'):
    image_texture_0.projection = 'FLAT'
if hasattr(image_texture_0, 'projection_blend'):
    image_texture_0.projection_blend = 0.0
if hasattr(image_texture_0, 'use_custom_color'):
    image_texture_0.use_custom_color = False
if hasattr(image_texture_0, 'width'):
    image_texture_0.width = 240.0
image_texture_0.inputs[0].default_value = (0.0, 0.0, 0.0)
image_texture_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
image_texture_0.outputs[1].default_value = 0.0

material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
if hasattr(material_output_0, 'color'):
    material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(material_output_0, 'hide'):
    material_output_0.hide = True
if hasattr(material_output_0, 'is_active_output'):
    material_output_0.is_active_output = False
if hasattr(material_output_0, 'label'):
    material_output_0.label = 'R3_EC2_EV'
if hasattr(material_output_0, 'location'):
    material_output_0.location = (120.0, 0.0)
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

material_output_001_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
if hasattr(material_output_001_0, 'color'):
    material_output_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(material_output_001_0, 'hide'):
    material_output_001_0.hide = True
if hasattr(material_output_001_0, 'is_active_output'):
    material_output_001_0.is_active_output = True
if hasattr(material_output_001_0, 'label'):
    material_output_001_0.label = 'R1_NMC_EV'
if hasattr(material_output_001_0, 'location'):
    material_output_001_0.location = (120.0, 40.0)
if hasattr(material_output_001_0, 'mute'):
    material_output_001_0.mute = False
if hasattr(material_output_001_0, 'name'):
    material_output_001_0.name = 'Material Output.001'
if hasattr(material_output_001_0, 'target'):
    material_output_001_0.target = 'ALL'
if hasattr(material_output_001_0, 'use_custom_color'):
    material_output_001_0.use_custom_color = False
if hasattr(material_output_001_0, 'width'):
    material_output_001_0.width = 140.0
material_output_001_0.inputs[2].default_value = (0.0, 0.0, 0.0)

image_texture_002_0 = node_tree0.nodes.new('ShaderNodeTexImage')
if hasattr(image_texture_002_0, 'color'):
    image_texture_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(image_texture_002_0, 'extension'):
    image_texture_002_0.extension = 'REPEAT'
if hasattr(image_texture_002_0, 'hide'):
    image_texture_002_0.hide = False
if hasattr(image_texture_002_0, 'interpolation'):
    image_texture_002_0.interpolation = 'Linear'
if hasattr(image_texture_002_0, 'label'):
    image_texture_002_0.label = 'Cam-##_H_Masks'
if hasattr(image_texture_002_0, 'location'):
    image_texture_002_0.location = (-420.0, -240.0)
if hasattr(image_texture_002_0, 'mute'):
    image_texture_002_0.mute = False
if hasattr(image_texture_002_0, 'name'):
    image_texture_002_0.name = 'Image Texture.002'
if hasattr(image_texture_002_0, 'projection'):
    image_texture_002_0.projection = 'FLAT'
if hasattr(image_texture_002_0, 'projection_blend'):
    image_texture_002_0.projection_blend = 0.0
if hasattr(image_texture_002_0, 'use_custom_color'):
    image_texture_002_0.use_custom_color = False
if hasattr(image_texture_002_0, 'width'):
    image_texture_002_0.width = 240.0
image_texture_002_0.inputs[0].default_value = (0.0, 0.0, 0.0)
image_texture_002_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
image_texture_002_0.outputs[1].default_value = 0.0

node_tree1 = bpy.data.node_groups.get('ICEO_compositor')
if not node_tree1:
    node_tree1 = bpy.data.node_groups.new('ICEO_compositor', 'ShaderNodeTree')
    # INPUTS
    node_tree1.inputs.new('NodeSocketColor', 'R1_NMC')
    node_tree1.inputs.new('NodeSocketFloat', 'R3_EC2')
    node_tree1.inputs.new('NodeSocketFloatFactor', 'H_Masks')
    # OUTPUTS
    node_tree1.outputs.new('NodeSocketShader', 'L2_ICEO')
    node_tree1.outputs.new('NodeSocketShader', 'L3_ICEO')
    # NODES
    bump_1 = node_tree1.nodes.new('ShaderNodeBump')
    if hasattr(bump_1, 'color'):
        bump_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(bump_1, 'hide'):
        bump_1.hide = False
    if hasattr(bump_1, 'invert'):
        bump_1.invert = False
    if hasattr(bump_1, 'location'):
        bump_1.location = (-240.0, -10.0)
    if hasattr(bump_1, 'mute'):
        bump_1.mute = False
    if hasattr(bump_1, 'name'):
        bump_1.name = 'Bump'
    if hasattr(bump_1, 'use_custom_color'):
        bump_1.use_custom_color = False
    if hasattr(bump_1, 'width'):
        bump_1.width = 140.0
    bump_1.inputs[0].default_value = 1.0
    bump_1.inputs[1].default_value = 1.0
    bump_1.inputs[2].default_value = 1.0
    bump_1.inputs[3].default_value = 1.0
    bump_1.inputs[4].default_value = 1.0
    bump_1.inputs[5].default_value = (0.0, 0.0, 0.0)
    bump_1.outputs[0].default_value = (0.0, 0.0, 0.0)

    colorramp_001_1 = node_tree1.nodes.new('ShaderNodeValToRGB')
    if hasattr(colorramp_001_1, 'color'):
        colorramp_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(colorramp_001_1, 'color_ramp'):
        if hasattr(colorramp_001_1.color_ramp, 'color_mode'):
            colorramp_001_1.color_ramp.color_mode = 'RGB'
        if hasattr(colorramp_001_1.color_ramp, 'elements'):
            if 0 >= len(colorramp_001_1.color_ramp.elements):
                colorramp_001_1.color_ramp.elements.new(0.0)
            if hasattr(colorramp_001_1.color_ramp.elements[0], 'alpha'):
                colorramp_001_1.color_ramp.elements[0].alpha = 1.0
            if hasattr(colorramp_001_1.color_ramp.elements[0], 'color'):
                colorramp_001_1.color_ramp.elements[0].color = (1.0, 1.0, 1.0, 1.0)
            if hasattr(colorramp_001_1.color_ramp.elements[0], 'position'):
                colorramp_001_1.color_ramp.elements[0].position = 0.0
            if 1 >= len(colorramp_001_1.color_ramp.elements):
                colorramp_001_1.color_ramp.elements.new(0.20000000298023224)
            if hasattr(colorramp_001_1.color_ramp.elements[1], 'alpha'):
                colorramp_001_1.color_ramp.elements[1].alpha = 1.0
            if hasattr(colorramp_001_1.color_ramp.elements[1], 'color'):
                colorramp_001_1.color_ramp.elements[1].color = (0.0, 0.0, 0.0, 1.0)
            if hasattr(colorramp_001_1.color_ramp.elements[1], 'position'):
                colorramp_001_1.color_ramp.elements[1].position = 0.20000000298023224
            if 2 >= len(colorramp_001_1.color_ramp.elements):
                colorramp_001_1.color_ramp.elements.new(0.7450000047683716)
            if hasattr(colorramp_001_1.color_ramp.elements[2], 'alpha'):
                colorramp_001_1.color_ramp.elements[2].alpha = 1.0
            if hasattr(colorramp_001_1.color_ramp.elements[2], 'color'):
                colorramp_001_1.color_ramp.elements[2].color = (1.0, 1.0, 1.0, 1.0)
            if hasattr(colorramp_001_1.color_ramp.elements[2], 'position'):
                colorramp_001_1.color_ramp.elements[2].position = 0.7450000047683716
        if hasattr(colorramp_001_1.color_ramp, 'hue_interpolation'):
            colorramp_001_1.color_ramp.hue_interpolation = 'NEAR'
        if hasattr(colorramp_001_1.color_ramp, 'interpolation'):
            colorramp_001_1.color_ramp.interpolation = 'CONSTANT'
    if hasattr(colorramp_001_1, 'hide'):
        colorramp_001_1.hide = False
    if hasattr(colorramp_001_1, 'location'):
        colorramp_001_1.location = (-240.0, -250.0)
    if hasattr(colorramp_001_1, 'mute'):
        colorramp_001_1.mute = False
    if hasattr(colorramp_001_1, 'name'):
        colorramp_001_1.name = 'ColorRamp.001'
    if hasattr(colorramp_001_1, 'use_custom_color'):
        colorramp_001_1.use_custom_color = False
    if hasattr(colorramp_001_1, 'width'):
        colorramp_001_1.width = 240.0
    colorramp_001_1.inputs[0].default_value = 0.5
    colorramp_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
    colorramp_001_1.outputs[1].default_value = 0.0

    principled_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfPrincipled')
    if hasattr(principled_bsdf_1, 'color'):
        principled_bsdf_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(principled_bsdf_1, 'distribution'):
        principled_bsdf_1.distribution = 'GGX'
    if hasattr(principled_bsdf_1, 'hide'):
        principled_bsdf_1.hide = False
    if hasattr(principled_bsdf_1, 'location'):
        principled_bsdf_1.location = (-60.0, -10.0)
    if hasattr(principled_bsdf_1, 'mute'):
        principled_bsdf_1.mute = False
    if hasattr(principled_bsdf_1, 'name'):
        principled_bsdf_1.name = 'Principled BSDF'
    if hasattr(principled_bsdf_1, 'subsurface_method'):
        principled_bsdf_1.subsurface_method = 'BURLEY'
    if hasattr(principled_bsdf_1, 'use_custom_color'):
        principled_bsdf_1.use_custom_color = False
    if hasattr(principled_bsdf_1, 'width'):
        principled_bsdf_1.width = 240.0
    principled_bsdf_1.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    principled_bsdf_1.inputs[1].default_value = 0.0
    principled_bsdf_1.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_1.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    principled_bsdf_1.inputs[4].default_value = 0.0
    principled_bsdf_1.inputs[5].default_value = 0.5
    principled_bsdf_1.inputs[6].default_value = 0.0
    principled_bsdf_1.inputs[7].default_value = 0.5
    principled_bsdf_1.inputs[8].default_value = 0.0
    principled_bsdf_1.inputs[9].default_value = 0.0
    principled_bsdf_1.inputs[10].default_value = 0.0
    principled_bsdf_1.inputs[11].default_value = 0.5
    principled_bsdf_1.inputs[12].default_value = 0.0
    principled_bsdf_1.inputs[13].default_value = 0.029999999329447746
    principled_bsdf_1.inputs[14].default_value = 1.4500000476837158
    principled_bsdf_1.inputs[15].default_value = 0.0
    principled_bsdf_1.inputs[16].default_value = 0.0
    principled_bsdf_1.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
    principled_bsdf_1.inputs[18].default_value = 1.0
    principled_bsdf_1.inputs[19].default_value = 1.0
    principled_bsdf_1.inputs[20].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_1.inputs[21].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_1.inputs[22].default_value = (0.0, 0.0, 0.0)

    emission_1 = node_tree1.nodes.new('ShaderNodeEmission')
    if hasattr(emission_1, 'color'):
        emission_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(emission_1, 'hide'):
        emission_1.hide = False
    if hasattr(emission_1, 'location'):
        emission_1.location = (40.0, -150.0)
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

    mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
    if hasattr(mix_shader_1, 'color'):
        mix_shader_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(mix_shader_1, 'hide'):
        mix_shader_1.hide = False
    if hasattr(mix_shader_1, 'location'):
        mix_shader_1.location = (240.0, -10.0)
    if hasattr(mix_shader_1, 'mute'):
        mix_shader_1.mute = False
    if hasattr(mix_shader_1, 'name'):
        mix_shader_1.name = 'Mix Shader'
    if hasattr(mix_shader_1, 'use_custom_color'):
        mix_shader_1.use_custom_color = False
    if hasattr(mix_shader_1, 'width'):
        mix_shader_1.width = 140.0
    mix_shader_1.inputs[0].default_value = 0.5

    principled_bsdf_001_1 = node_tree1.nodes.new('ShaderNodeBsdfPrincipled')
    if hasattr(principled_bsdf_001_1, 'color'):
        principled_bsdf_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(principled_bsdf_001_1, 'distribution'):
        principled_bsdf_001_1.distribution = 'GGX'
    if hasattr(principled_bsdf_001_1, 'hide'):
        principled_bsdf_001_1.hide = False
    if hasattr(principled_bsdf_001_1, 'location'):
        principled_bsdf_001_1.location = (-60.0, 250.0)
    if hasattr(principled_bsdf_001_1, 'mute'):
        principled_bsdf_001_1.mute = False
    if hasattr(principled_bsdf_001_1, 'name'):
        principled_bsdf_001_1.name = 'Principled BSDF.001'
    if hasattr(principled_bsdf_001_1, 'subsurface_method'):
        principled_bsdf_001_1.subsurface_method = 'BURLEY'
    if hasattr(principled_bsdf_001_1, 'use_custom_color'):
        principled_bsdf_001_1.use_custom_color = False
    if hasattr(principled_bsdf_001_1, 'width'):
        principled_bsdf_001_1.width = 240.0
    principled_bsdf_001_1.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    principled_bsdf_001_1.inputs[1].default_value = 0.0
    principled_bsdf_001_1.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_001_1.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    principled_bsdf_001_1.inputs[4].default_value = 0.0
    principled_bsdf_001_1.inputs[5].default_value = 0.5
    principled_bsdf_001_1.inputs[6].default_value = 0.0
    principled_bsdf_001_1.inputs[7].default_value = 0.5
    principled_bsdf_001_1.inputs[8].default_value = 0.0
    principled_bsdf_001_1.inputs[9].default_value = 0.0
    principled_bsdf_001_1.inputs[10].default_value = 0.0
    principled_bsdf_001_1.inputs[11].default_value = 0.5
    principled_bsdf_001_1.inputs[12].default_value = 0.0
    principled_bsdf_001_1.inputs[13].default_value = 0.029999999329447746
    principled_bsdf_001_1.inputs[14].default_value = 1.4500000476837158
    principled_bsdf_001_1.inputs[15].default_value = 0.0
    principled_bsdf_001_1.inputs[16].default_value = 0.0
    principled_bsdf_001_1.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
    principled_bsdf_001_1.inputs[18].default_value = 1.0
    principled_bsdf_001_1.inputs[19].default_value = 1.0
    principled_bsdf_001_1.inputs[20].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_001_1.inputs[21].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_001_1.inputs[22].default_value = (0.0, 0.0, 0.0)

    emission_001_1 = node_tree1.nodes.new('ShaderNodeEmission')
    if hasattr(emission_001_1, 'color'):
        emission_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(emission_001_1, 'hide'):
        emission_001_1.hide = False
    if hasattr(emission_001_1, 'location'):
        emission_001_1.location = (40.0, 110.0)
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

    mix_shader_001_1 = node_tree1.nodes.new('ShaderNodeMixShader')
    if hasattr(mix_shader_001_1, 'color'):
        mix_shader_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(mix_shader_001_1, 'hide'):
        mix_shader_001_1.hide = False
    if hasattr(mix_shader_001_1, 'location'):
        mix_shader_001_1.location = (240.0, 250.0)
    if hasattr(mix_shader_001_1, 'mute'):
        mix_shader_001_1.mute = False
    if hasattr(mix_shader_001_1, 'name'):
        mix_shader_001_1.name = 'Mix Shader.001'
    if hasattr(mix_shader_001_1, 'use_custom_color'):
        mix_shader_001_1.use_custom_color = False
    if hasattr(mix_shader_001_1, 'width'):
        mix_shader_001_1.width = 140.0
    mix_shader_001_1.inputs[0].default_value = 0.5

    normal_map_1 = node_tree1.nodes.new('ShaderNodeNormalMap')
    if hasattr(normal_map_1, 'color'):
        normal_map_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(normal_map_1, 'hide'):
        normal_map_1.hide = False
    if hasattr(normal_map_1, 'location'):
        normal_map_1.location = (-240.0, 250.0)
    if hasattr(normal_map_1, 'mute'):
        normal_map_1.mute = False
    if hasattr(normal_map_1, 'name'):
        normal_map_1.name = 'Normal Map'
    if hasattr(normal_map_1, 'space'):
        normal_map_1.space = 'TANGENT'
    if hasattr(normal_map_1, 'use_custom_color'):
        normal_map_1.use_custom_color = False
    if hasattr(normal_map_1, 'width'):
        normal_map_1.width = 150.0
    normal_map_1.inputs[0].default_value = 1.0
    normal_map_1.inputs[1].default_value = (0.5, 0.5, 1.0, 1.0)
    normal_map_1.outputs[0].default_value = (0.0, 0.0, 0.0)

    group_input_1 = node_tree1.nodes.new('NodeGroupInput')
    if hasattr(group_input_1, 'color'):
        group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(group_input_1, 'hide'):
        group_input_1.hide = False
    if hasattr(group_input_1, 'location'):
        group_input_1.location = (-520.0, -20.0)
    if hasattr(group_input_1, 'mute'):
        group_input_1.mute = False
    if hasattr(group_input_1, 'name'):
        group_input_1.name = 'Group Input'
    if hasattr(group_input_1, 'use_custom_color'):
        group_input_1.use_custom_color = False
    if hasattr(group_input_1, 'width'):
        group_input_1.width = 140.0
    group_input_1.outputs[0].default_value = (0.5, 0.5, 1.0, 1.0)
    group_input_1.outputs[1].default_value = 1.0
    group_input_1.outputs[2].default_value = 0.5

    group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
    if hasattr(group_output_1, 'color'):
        group_output_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
    if hasattr(group_output_1, 'hide'):
        group_output_1.hide = False
    if hasattr(group_output_1, 'is_active_output'):
        group_output_1.is_active_output = True
    if hasattr(group_output_1, 'location'):
        group_output_1.location = (440.0, -20.0)
    if hasattr(group_output_1, 'mute'):
        group_output_1.mute = False
    if hasattr(group_output_1, 'name'):
        group_output_1.name = 'Group Output'
    if hasattr(group_output_1, 'use_custom_color'):
        group_output_1.use_custom_color = False
    if hasattr(group_output_1, 'width'):
        group_output_1.width = 140.0

    # LINKS
    node_tree1.links.new(group_input_1.outputs[2], colorramp_001_1.inputs[0])
    node_tree1.links.new(group_input_1.outputs[1], bump_1.inputs[2])
    node_tree1.links.new(mix_shader_1.outputs[0], group_output_1.inputs[1])
    node_tree1.links.new(group_input_1.outputs[0], normal_map_1.inputs[1])
    node_tree1.links.new(mix_shader_001_1.outputs[0], group_output_1.inputs[0])
    node_tree1.links.new(bump_1.outputs[0], principled_bsdf_1.inputs[20])
    node_tree1.links.new(principled_bsdf_1.outputs[0], mix_shader_1.inputs[1])
    node_tree1.links.new(emission_1.outputs[0], mix_shader_1.inputs[2])
    node_tree1.links.new(colorramp_001_1.outputs[0], mix_shader_1.inputs[0])
    node_tree1.links.new(principled_bsdf_001_1.outputs[0], mix_shader_001_1.inputs[1])
    node_tree1.links.new(emission_001_1.outputs[0], mix_shader_001_1.inputs[2])
    node_tree1.links.new(colorramp_001_1.outputs[0], mix_shader_001_1.inputs[0])
    node_tree1.links.new(normal_map_1.outputs[0], principled_bsdf_001_1.inputs[20])

group_0 = node_tree0.nodes.new('ShaderNodeGroup')
if hasattr(group_0, 'node_tree'):
    group_0.node_tree = bpy.data.node_groups.get('ICEO_compositor')
if hasattr(group_0, 'color'):
    group_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(group_0, 'hide'):
    group_0.hide = False
if hasattr(group_0, 'location'):
    group_0.location = (-60.0, 60.0)
if hasattr(group_0, 'mute'):
    group_0.mute = False
if hasattr(group_0, 'name'):
    group_0.name = 'Group'
if hasattr(group_0, 'use_custom_color'):
    group_0.use_custom_color = False
if hasattr(group_0, 'width'):
    group_0.width = 140.0
group_0.inputs[0].default_value = (0.5, 0.5, 1.0, 1.0)
group_0.inputs[1].default_value = 1.0
group_0.inputs[2].default_value = 0.5

# LINKS
node_tree0.links.new(image_texture_002_0.outputs[0], group_0.inputs[2])
node_tree0.links.new(image_texture_001_0.outputs[0], group_0.inputs[1])
node_tree0.links.new(group_0.outputs[1], material_output_0.inputs[0])
node_tree0.links.new(image_texture_0.outputs[0], group_0.inputs[0])
node_tree0.links.new(group_0.outputs[0], material_output_001_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = iceo

