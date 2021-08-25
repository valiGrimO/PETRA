import bpy

# Select render Engine
bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'

# Activate Flat Shading
    # bpy.context.scene.shading.light = 'FLAT'	MESSAGE: AttributeError: 'Scene' object has no attribute 'shading'

# Render Vertex Color
    # bpy.context.scene.shading.color_type = 'VERTEX'	MESSAGE: Should be the same here...

# Backface culling
bpy.context.scene.shading.show_backface_culling = True

# Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[0]`
    # Connect `Hub/C1:[0]` to `C1:Color/[1]`

# Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Disconnect `Render Layers/[0]` to `Hub/[0]`
    # Disconnect `Hub/C1:[0]` to `C1:Color/[1]`

