import bpy

<<<<<<< HEAD
# get reference and list of nodes
nodetree = bpy.context.scene.node_tree

node1 = bpy.data.scenes["Scene"].node_tree.nodes["Render Layers"]
node2 = bpy.data.node_groups["Hub"]

# node2_in = node2_nodetree.nodes["NodeGroupInput"] -> how to recognize inputs and outputs?
# node2_out = node2_nodetree.nodes("NodeGroupOutput")

nodeC1 = bpy.data.node_groups["C1: Color"]
# will be used later in other scripts:
    # nodeR1 = bpy.data.node_groups["R1: Shading"]
    # nodeR2 = bpy.data.node_groups["R2: Contour Lines"]
    # nodeR3 = bpy.data.node_groups["R3: Distance Map"]
    # nodeR4 = bpy.data.node_groups["R4: Pointiness"]
    # nodeR5 = bpy.data.node_groups["R5: Aspect"]

# set render engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# assign material to selected objects
# for obj in bpy.context.selected_objects:
#    objectName.setMaterials([c1_prv])
#    data.materials.append(bpy.data.materials.get('c1_prv'))


# connect compositing nodes
## from 'render layer' to 'hub'
nodetree.links.new(node1.outputs[0], node2.inputs[0])
## from 'hub' to 'branch'
nodetree.links.new(node2.outputs[0], nodeC1.inputs[1])

# disconnect compositing nodes
## from 'render layer' to 'hub'
# nodetree.links.remove(node1.outputs[0], node2.inputs[0]) -> will be used later
nodetree.links.remove(node1.outputs[0], node2.inputs[1])
nodetree.links.remove(node1.outputs[0], node2.inputs[2])
nodetree.links.remove(node1.outputs[0], node2.inputs[3])
nodetree.links.remove(node1.outputs[0], node2.inputs[4])
nodetree.links.remove(node1.outputs[0], node2.inputs[5])
nodetree.links.remove(node1.outputs[0], node2.inputs[6])
nodetree.links.remove(node1.outputs[0], node2.inputs[7])
nodetree.links.remove(node1.outputs[0], node2.inputs[8])
nodetree.links.remove(node1.outputs[0], node2.inputs[9])

## from 'hub' to 'branch'
nodetree.links.remove(node2.outputs[0], nodeC1.inputs[0])

# Reference Sphere
bpy.data.objects["Reference Sphere"].hide_render = True

# ambient occlusion
bpy.context.scene.eevee.use_gtao = False
# bpy.context.scene.eevee.gtao_distance = 10
# bpy.context.scene.eevee.gtao_quality = 1

# hit render button
# bpy.ops.petra.produce_documentation()
=======
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
>>>>>>> main
