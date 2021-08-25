import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Activate Ambient Occlusion
bpy.context.scene.eevee.use_gtao = True

# Ambient Occlusion Distance
bpy.context.scene.eevee.gtao_distance = 5

# Ambient Occlusion Quality
bpy.context.scene.eevee.gtao_quality = 1

# Apply material to selected objects
    # For selected objects:
        # Apply `l1_occlusionambiante`

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[3]`

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Deactivate Ambient Occlusion
bpy.context.scene.eevee.use_gtao = False

# Set Compositor in its initial state
    # Deconnect `Render Layers/[0]` to `Hub/[3]`
