import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
    # For selected objects:
        # Apply `C1_PRV` material

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[0]`
    # Connect `Hub/C1:[0]` to `C1:Color/[1]`

# Lock interface while rendering
    # Render Display Type: Keep User Interface
    # bpy.context.scene.render.use_lock_interface = True

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Disconnect `Render Layers/[0]` to `Hub/[0]`
    # Disconnect `Hub/C1:[0]` to `C1:Color/[1]`
