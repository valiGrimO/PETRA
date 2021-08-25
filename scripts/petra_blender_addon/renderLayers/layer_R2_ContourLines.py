import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
    # For selected objects:
        # Apply `R2_ContourLines` material

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[5]`

# CONTOUR LINES 1
## Configure Material
    # Unmute `Math`
    # Mute `Math.001`
    # Mute `Math.002`

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# CONTOUR LINES 2
## Configure Material
    # Unmute `Math.001`

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# CONTOUR LINES 3
## Configure Material
    # Unmute `Math.002`

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Disconnect `Render Layers/[0]` from `Hub/[5]`
