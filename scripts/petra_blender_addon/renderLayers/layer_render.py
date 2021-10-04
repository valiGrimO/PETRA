import bpy

bpy.ops.cameramanager.render_scene_animation()

# Delete DECIMATE modifier on selected object
# when R4 is applied
bpy.ops.object.modifier_remove(modifier="Decimate")
