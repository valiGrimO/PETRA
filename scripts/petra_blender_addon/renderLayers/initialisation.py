################################################################
# Setting everything properly to render any layer of information 
# (in case a user change something)
################################################################

import bpy

# Don't render `Reference Sphere`
bpy.data.objects["Reference Sphere"].hide_render = True

# Configure Compositor
    # Disconnect `Render Layers/[0]` to `Hub/[0]`
    # Disconnect `Render Layers/[0]` to `Hub/[1]`
    # Disconnect `Render Layers/[0]` to `Hub/[2]`
    # Disconnect `Render Layers/[0]` to `Hub/[3]`
    # Connect `Render Layers/[0]` to `Hub/[4]`
    # Disconnect `Render Layers/[0]` to `Hub/[5]`
    # Disconnect `Render Layers/[0]` to `Hub/[6]`
    # Disconnect `Render Layers/[0]` to `Hub/[7]`
    # Disconnect `Render Layers/[0]` to `Hub/[8]`
    # Disconnect `Render Layers/[0]` to `Hub/[9]`

# Lock interface while rendering
    # Render Display Type: Keep User Interface
    # bpy.context.scene.render.use_lock_interface = True
