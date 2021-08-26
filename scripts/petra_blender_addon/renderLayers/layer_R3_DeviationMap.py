import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Apply material to selected objects
    # For selected objects:
        # Apply `r3_deviation_map`

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[6]`

#################################################
*This part is written in MarkDown:*

We have to configure some options through the interface of the plugin. We need to match:
1. the vertex group available (`col`, `DM1`, `DM2`)
2. with extreme values

Those options are to be configured in the `r3_deviation_map` material.

*End of the MarkDown passage.*
#################################################

# DM1
    # set the DM1 configuration 

    # unmute `File Output`
    # mute `File Output.001`
    # unmute `File Output.002`
    # mute `File Output.003`

    # hit "produce documentation" in the PETrA Pannel (Rendering)

# DM2
    # set the DM1 configuration 

    # mute `File Output`
    # unmute `File Output.001`
    # mute `File Output.002`
    # unmute `File Output.003`

    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Deconnect `Render Layers/[0]` to `Hub/[6]`
