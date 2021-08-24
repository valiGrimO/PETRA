import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
    # For selected objects:
        # Apply `H2_OBN` material

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[2]`

# Lock interface while rendering
    # Render Display Type: Keep User Interface
    # bpy.context.scene.render.use_lock_interface = True

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Disconnect `Render Layers/[0]` to `Hub/[2]`
