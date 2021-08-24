import bpy

# Select render Engine
bpy.context.scene.render.engine = 'CYCLES'

# Apply material to selected objects
    # For selected objects:
        # Apply `R4_Pointiness` material

# Lock interface while rendering
    # Render Display Type: Keep User Interface
    # bpy.context.scene.render.use_lock_interface = True

# 100%
## Configure Compositor
    # Connect `Render Layers/[0]` to `Hub/[7]`
    # Connect `Hub/[4]` to `R4:Pointiness/[0]`

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# 25%
# Decimate Selected mesh
    # bpy.ops.object.modifier_add(type='DECIMATE')
    # bpy.context.object.modifiers["Decimate"].ratio = 0.25

## Configure Compositor
    # Connect `Hub/[4]` to `R4:Pointiness/[1]`

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# 10%
# Decimate Selected mesh
    # bpy.ops.object.modifier_add(type='DECIMATE')
    # bpy.context.object.modifiers["Decimate"].ratio = 0.1

## Configure Compositor
    # Connect `Hub/[4]` to `R4:Pointiness/[2]`

## Produce Documentation
    # hit "produce documentation" in the PETrA Pannel (Rendering)

# Set Compositor in its initial state
    # Disconnect `Render Layers/[0]` from `Hub/[7]`
    # Connect `Hub/[4]` to `R4:Pointiness/[0]`

# Delete DECIMATE modifyer on selected object
    # bpy.ops.object.modifier_remove(modifier="Decimate")
