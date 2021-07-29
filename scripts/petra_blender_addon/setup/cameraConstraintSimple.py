import bpy


print("[PETRA] Setup: Initial")

C = bpy.context
D = bpy.data

# ----------------------------------
# FRAME
# ----------------------------------

# Create a plane
bpy.ops.mesh.primitive_plane_add(
    enter_editmode=False, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
)
so = C.selected_objects[0]
so.name = "Frame"

## Skin modifyer
bpy.ops.object.modifier_add(type="SKIN")

## Skin resize
bpy.ops.object.editmode_toggle()
bpy.ops.transform.skin_resize(value=(0.1, 0.1, 0.1))
bpy.ops.object.editmode_toggle()

## Apply modifyer
bpy.ops.object.modifier_apply(modifier="Skin", report=True)

## Scale the frame
C.object.scale = 0.487805, 0.487805, 0.487805
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

# ----------------------------------
# Camera
# ----------------------------------

## Cam-01
bpy.ops.object.camera_add(location=(0, 0, 1), rotation=(0, 0, 0))
so = C.selected_objects[0]
so.name = "Cam-01"

## Set Camera Ortho
for obj in C.scene.objects:
    if obj.type == "CAMERA":
        print(obj.data.type)
        obj.data.type = "ORTHO"

# ----------------------------------
# Drivers
# ----------------------------------

def addDrivers("Frame", "Cam-01", 
#             (source, target, prop, dataPath, index = -1, negative = False, func = '')    

#    data_path = "key_blocks[\"Key1\"].value"
#    dr = mesh.shape_keys.driver_add(data_path)
    dr.driver.type='MAX'

    var = dr.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = oScaleX
    var.targets[0].bone_target = "oScaleX"
    var.targets[0].transform_type = 'scale[0]'
    
    var = dr.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = oScaleY
    var.targets[0].bone_target = "oScaleY"
    var.targets[0].transform_type = 'scale[1]'



# ---------------------------------- # ---------------------------------- # ---------------------------------- 

## Define orthographic scale:
### Cam-01
    # Choose the highest value between
        # bpy.data.objects["Framing Box"].scale[0]
        # bpy.data.objects["Framing Box"].scale[2]
    # Copy this value as a new driver
        # bpy.ops.ui.copy_as_driver_button()

    # Set this value as the orthographic scale of the camera
        # bpy.ops.anim.paste_driver_button()
        
# ---------------------------------- # ---------------------------------- # ---------------------------------- 

# Below, inspiration from
# http://web.purplefrog.com/~thoth/blender/python-cookbook/driver-multi-chain.html
# line 145

def addDrivers(obj, oa, zArray5):

    mesh = obj.data

    z0,z1,z2,z3,z4 = zArray5

    za = z1 + z3-z2
    zb = z3
    zc = z4

    data_path = "key_blocks[\"Key1\"].value"
    dr = mesh.shape_keys.driver_add(data_path)
    dr.driver.type='MAX'

    var = dr.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = oa
    var.targets[0].bone_target = "bone.L"
    var.targets[0].transform_type = 'LOC_Z'
    dr.modifiers[0].coefficients = ABFor(za, zb)


    var = dr.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = oa
    var.targets[0].bone_target = "bone.R"
    var.targets[0].transform_type = 'LOC_Z'
    dr.modifiers[0].coefficients = ABFor(za, zb)

    #

    data_path = "key_blocks[\"Key2A\"].value"
    dr = mesh.shape_keys.driver_add(data_path)
    dr.driver.type='MAX'

    var = dr.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = oa
    var.targets[0].bone_target = "bone.L"
    var.targets[0].transform_type = 'LOC_Z'
    dr.modifiers[0].coefficients = ABFor(zb, zc)

    #

    data_path = "key_blocks[\"Key2B\"].value"
    dr = mesh.shape_keys.driver_add(data_path)
    dr.driver.type='MAX'

    var = dr.driver.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = oa
    var.targets[0].bone_target = "bone.R"
    var.targets[0].transform_type = 'LOC_Z'
    dr.modifiers[0].coefficients = ABFor(zb, zc)


xArray6 = [0, 0.2, 0.8, 1.2, 1.8, 2]
yArray4 = [0, 0.2, 0.8, 1 ]
zArray5 = [ 0, 0.2, 1, 1.2, 2]
name = "stacks"

mesh = createMesh(name, xArray6, yArray4 ,zArray5)

obj = bpy.data.objects.new(name, mesh)

bpy.context.scene.objects.link(obj)

bpy.context.scene.objects.active =obj
obj.select = True

addShapeKeys(obj, xArray6, yArray4 ,zArray5)

oa = fabArmature(name)

addDrivers(obj, oa, zArray5)