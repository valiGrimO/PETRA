import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'

# Activate Matcap
    # bpy.context.scene.shading.light = 'MATCAP'    MESSAGE: AttributeError: 'Scene' object has no attribute 'shading'

# Select one of the matcaps
    # bpy.context.scene.shading.studio_light = 'check_normal+y.exr'     MESSAGE: Should be the same here...

# Render `Reference Sphere`
bpy.data.objects["Reference Sphere"].hide_render = False

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[4]`

# Lock interface while rendering
    # Render Display Type: Keep User Interface
    # bpy.context.scene.render.use_lock_interface = True

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set `Reference Sphere` in its initial state
bpy.data.objects["Reference Sphere"].hide_render = True

