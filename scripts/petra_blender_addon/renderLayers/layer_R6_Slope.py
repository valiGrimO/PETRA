import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Apply material
    # For selected objects:
        # Apply `R6_Slope` material
        # Apply `R6_Slope` material to Reference Sphere
        
# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[9]`

# Render `Reference Sphere`
bpy.data.objects["Reference Sphere"].hide_render = False

# Lock interface while rendering
    # Render Display Type: Keep User Interface
    # bpy.context.scene.render.use_lock_interface = True

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Disconnect `Render Layers/[0]` from `Hub/[9]`

# Set `Reference Sphere` in its initial state
bpy.data.objects["Reference Sphere"].hide_render = True
