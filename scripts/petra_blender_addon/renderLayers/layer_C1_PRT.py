import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[0]`
    # Connect `Hub/C1:[0]` to `C1:Color/[0]`

# Lock interface while rendering
    # Render Display Type: Keep User Interface
    # bpy.context.scene.render.use_lock_interface = True

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Deconnect `Render Layers/[0]` to `Hub/[0]`
    # Deconnect `Hub/C1:[0]` to `C1:Color/[0]`
