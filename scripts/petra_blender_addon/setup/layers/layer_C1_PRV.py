import bpy

MATERIALS:
    to selected object, apply material c1_prv
# how to differenciate prt to prv?
# bpy.data.objects['objectName'].data.materials.append(bpy.data.materials.get('materialName'))


COMPOSITING:
    connect Render Layers with C1
    disconnect Render Layers from H1
    disconnect Render Layers from H2
    disconnect Render Layers from L1
    disconnect Render Layers from R1
    disconnect Render Layers from R2
    disconnect Render Layers from R3
    disconnect Render Layers from R4
    disconnect Render Layers from R5
    disconnect Render Layers from R6
    

# Reference Sphere
bpy.data.objects["Reference Sphere"].hide_render = False
