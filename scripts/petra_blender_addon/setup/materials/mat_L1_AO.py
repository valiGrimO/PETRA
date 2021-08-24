import bpy

# MATERIAL
l1_ao = bpy.data.materials.new(name='l1_ao')
l1_ao.use_nodes = True
node_tree0 = l1_ao.node_tree
for node in node_tree0.nodes:
    node_tree0.nodes.remove(node)

# NODES
principled_bsdf_0 = node_tree0.nodes.new('ShaderNodeBsdfPrincipled')
if hasattr(principled_bsdf_0, 'active_preview'):
    principled_bsdf_0.active_preview = False
if hasattr(principled_bsdf_0, 'color'):
    principled_bsdf_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(principled_bsdf_0, 'distribution'):
    principled_bsdf_0.distribution = 'GGX'
if hasattr(principled_bsdf_0, 'hide'):
    principled_bsdf_0.hide = False
if hasattr(principled_bsdf_0, 'location'):
    principled_bsdf_0.location = (460.0, 0.0)
if hasattr(principled_bsdf_0, 'mute'):
    principled_bsdf_0.mute = False
if hasattr(principled_bsdf_0, 'name'):
    principled_bsdf_0.name = 'Principled BSDF'
if hasattr(principled_bsdf_0, 'subsurface_method'):
    principled_bsdf_0.subsurface_method = 'BURLEY'
if hasattr(principled_bsdf_0, 'use_custom_color'):
    principled_bsdf_0.use_custom_color = False
if hasattr(principled_bsdf_0, 'width'):
    principled_bsdf_0.width = 240.0
principled_bsdf_0.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
principled_bsdf_0.inputs[1].default_value = 0.0
principled_bsdf_0.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
principled_bsdf_0.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
principled_bsdf_0.inputs[4].default_value = 0.0
principled_bsdf_0.inputs[5].default_value = 0.5
principled_bsdf_0.inputs[6].default_value = 0.0
principled_bsdf_0.inputs[7].default_value = 0.5
principled_bsdf_0.inputs[8].default_value = 0.0
principled_bsdf_0.inputs[9].default_value = 0.0
principled_bsdf_0.inputs[10].default_value = 0.0
principled_bsdf_0.inputs[11].default_value = 0.5
principled_bsdf_0.inputs[12].default_value = 0.0
principled_bsdf_0.inputs[13].default_value = 0.029999999329447746
principled_bsdf_0.inputs[14].default_value = 1.4500000476837158
principled_bsdf_0.inputs[15].default_value = 0.0
principled_bsdf_0.inputs[16].default_value = 0.0
principled_bsdf_0.inputs[17].default_value = (0.0, 0.0, 0.0, 1.0)
principled_bsdf_0.inputs[18].default_value = 1.0
principled_bsdf_0.inputs[19].default_value = 1.0
principled_bsdf_0.inputs[20].default_value = (0.0, 0.0, 0.0)
principled_bsdf_0.inputs[21].default_value = (0.0, 0.0, 0.0)
principled_bsdf_0.inputs[22].default_value = (0.0, 0.0, 0.0)

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
            colorramp_0.color_ramp.elements.new(0.30000001192092896)
        if hasattr(colorramp_0.color_ramp.elements[0], 'alpha'):
            colorramp_0.color_ramp.elements[0].alpha = 1.0
        if hasattr(colorramp_0.color_ramp.elements[0], 'color'):
            colorramp_0.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
        if hasattr(colorramp_0.color_ramp.elements[0], 'position'):
            colorramp_0.color_ramp.elements[0].position = 0.30000001192092896
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
        colorramp_0.color_ramp.interpolation = 'B_SPLINE'
if hasattr(colorramp_0, 'hide'):
    colorramp_0.hide = False
if hasattr(colorramp_0, 'location'):
    colorramp_0.location = (180.0, 0.0)
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

ambient_occlusion_001_0 = node_tree0.nodes.new('ShaderNodeAmbientOcclusion')
if hasattr(ambient_occlusion_001_0, 'active_preview'):
    ambient_occlusion_001_0.active_preview = False
if hasattr(ambient_occlusion_001_0, 'color'):
    ambient_occlusion_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(ambient_occlusion_001_0, 'hide'):
    ambient_occlusion_001_0.hide = False
if hasattr(ambient_occlusion_001_0, 'inside'):
    ambient_occlusion_001_0.inside = False
if hasattr(ambient_occlusion_001_0, 'location'):
    ambient_occlusion_001_0.location = (0.0, 0.0)
if hasattr(ambient_occlusion_001_0, 'mute'):
    ambient_occlusion_001_0.mute = False
if hasattr(ambient_occlusion_001_0, 'name'):
    ambient_occlusion_001_0.name = 'Ambient Occlusion.001'
if hasattr(ambient_occlusion_001_0, 'only_local'):
    ambient_occlusion_001_0.only_local = False
if hasattr(ambient_occlusion_001_0, 'samples'):
    ambient_occlusion_001_0.samples = 16
if hasattr(ambient_occlusion_001_0, 'use_custom_color'):
    ambient_occlusion_001_0.use_custom_color = False
if hasattr(ambient_occlusion_001_0, 'width'):
    ambient_occlusion_001_0.width = 140.0
ambient_occlusion_001_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
ambient_occlusion_001_0.inputs[1].default_value = 1.0
ambient_occlusion_001_0.inputs[2].default_value = (0.0, 0.0, 0.0)
ambient_occlusion_001_0.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
ambient_occlusion_001_0.outputs[1].default_value = 0.0

emission_002_0 = node_tree0.nodes.new('ShaderNodeEmission')
if hasattr(emission_002_0, 'active_preview'):
    emission_002_0.active_preview = False
if hasattr(emission_002_0, 'color'):
    emission_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(emission_002_0, 'hide'):
    emission_002_0.hide = False
if hasattr(emission_002_0, 'location'):
    emission_002_0.location = (720.0, -60.0)
if hasattr(emission_002_0, 'mute'):
    emission_002_0.mute = False
if hasattr(emission_002_0, 'name'):
    emission_002_0.name = 'Emission.002'
if hasattr(emission_002_0, 'use_custom_color'):
    emission_002_0.use_custom_color = False
if hasattr(emission_002_0, 'width'):
    emission_002_0.width = 140.0
emission_002_0.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
emission_002_0.inputs[1].default_value = 1.0

mix_shader_001_0 = node_tree0.nodes.new('ShaderNodeMixShader')
if hasattr(mix_shader_001_0, 'active_preview'):
    mix_shader_001_0.active_preview = False
if hasattr(mix_shader_001_0, 'color'):
    mix_shader_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
if hasattr(mix_shader_001_0, 'hide'):
    mix_shader_001_0.hide = False
if hasattr(mix_shader_001_0, 'location'):
    mix_shader_001_0.location = (900.0, 40.0)
if hasattr(mix_shader_001_0, 'mute'):
    mix_shader_001_0.mute = False
if hasattr(mix_shader_001_0, 'name'):
    mix_shader_001_0.name = 'Mix Shader.001'
if hasattr(mix_shader_001_0, 'use_custom_color'):
    mix_shader_001_0.use_custom_color = False
if hasattr(mix_shader_001_0, 'width'):
    mix_shader_001_0.width = 140.0
mix_shader_001_0.inputs[0].default_value = 0.5

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
    material_output_0.location = (1080.0, 40.0)
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
    geometry_001_0.location = (720.0, 220.0)
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

# LINKS
node_tree0.links.new(ambient_occlusion_001_0.outputs[1], colorramp_0.inputs[0])
node_tree0.links.new(colorramp_0.outputs[0], principled_bsdf_0.inputs[0])
node_tree0.links.new(principled_bsdf_0.outputs[0], mix_shader_001_0.inputs[1])
node_tree0.links.new(emission_002_0.outputs[0], mix_shader_001_0.inputs[2])
node_tree0.links.new(geometry_001_0.outputs[6], mix_shader_001_0.inputs[0])
node_tree0.links.new(mix_shader_001_0.outputs[0], material_output_0.inputs[0])

# TO ACTIVE
selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
for obj in selected_objects:
    obj.active_material = l1_ao
