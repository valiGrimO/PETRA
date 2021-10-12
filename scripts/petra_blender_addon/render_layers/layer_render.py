import bpy

for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
    	bpy.ops.petra.activate_and_preview_scene_camera()
    	bpy.ops.render.render(use_viewport=True)
