bl_info = {
    "name": "Deviation Map",
    "author": "Niels Klop"
    "version": (1, 17),
    "blender": (2, 90, 0),
    "location": "View3D > Sidebar > Distance Map",
    "description": "Calculate and visualize the distance between two objects",
    "category": "Object",
}

import bpy
import numpy as np
import mathutils as mu
import blf
import bpy_extras
import copy
import random
import os
from bpy_extras import view3d_utils

#future release: use empty [] for unselected vertex (convert to -10**9 for custom property)

#callback function for plotting text map
def drawTextCallback(context, dummy):
    for object in bpy.context.selected_objects:
        if len(object.data.vertex_colors) > 0: #if there is at least one vertex color map
            if object.data.vertex_colors.active.name in object.keys(): #check if color map name corresponds to one of the object's custom properties
                mapID = object.data.vertex_colors.active.name #retrieve active color map name
                lookupTable = [item for item in object[mapID]] #retrieve lookup table from custom properties
                verts = [object.matrix_world @ v.co for v in object.data.vertices] #retrieve object's vertex locations
                for count, item in enumerate(lookupTable):
                    if item != 10**9 and item != -10**9: #10**9 = None (no hit), -10**9 = [] (not selected)
                        vertLocOnScreen = view3d_utils.location_3d_to_region_2d(context.region, context.space_data.region_3d, verts[count]) #3d vertex location to 2d region location
                        blf.position(0, vertLocOnScreen[0], vertLocOnScreen[1], 0) #set text location
                        blf.size(0, bpy.context.scene.fontSize, 72) #set text size
                        fontColor = bpy.context.scene.fontColor
                        blf.color(0, fontColor[0], fontColor[1], fontColor[2], 1) #set text color
                        if bpy.context.scene.decimals == 0:
                            txt = str(int(round(item, bpy.context.scene.decimals))) #round to integer if decimals is zero
                        else:
                            txt = str(round(item, bpy.context.scene.decimals))
                        blf.draw(0, txt) #draw text
    return

class OBJECT_OT_distanceMapReadme_operator(bpy.types.Operator):
    """Export read me"""
    bl_idname = "object.distancemapreadme"
    bl_label = "Export read me"
    filepath: bpy.props.StringProperty(subtype = "FILE_PATH")

    def execute(self, context):
        #readme
        readme = '*** DISTANCE MAP READ ME ***' + '\n\n' 'The Distance Map addon is visible in the Sidebar (hotkey N) > Distance Map. To be able to generate a distance map, select two objects with mesh data. The distance map is built onto the last selected (active) object. The first selected (inactive) object serves as the target object, i.e. the object to which the distance is calculated. NOTE: Modifiers are not applied before calculating the distance map. NOTE: Color and text maps are not updated when an object is transformed after calculating the distance map.' + '\n\n' '* Generate Distance Map' + '\n' 'Generate a distance map of two selected mesh objects. Distance maps are saved under Properties > Object Data Properties > Vertex Colors. In the distance map name, the name of the target object, the raycast method ("Normals" or "Nearest") and maximum distance are included. Select a vertex color map name (not the camera icon) to make it active. Switch to viewport shading "Solid" and shading color "Vertex" to view the active color map in the viewport.' + '\n\n' '* Raycast Mode' + '\n' 'There are two methods to calculate a distance map. The "Normals" mode searches for the shortest distance from the base object to the target object along the vertex normals. Whether a hit was found along the positive or negative normal direction determines the color. If no hit was found, the out of range color is used. The "Nearest" mode searches for the shortest distance to the target object in any direction. The terms "positive" and "negative" are ill-defined in this context, this method therefore only uses the positive color. In contrary to the "Normals" mode, this method yields results for every vertex, as it searches in any direction.' + '\n\n' '* Normalization Value' + '\n' 'The normalization value determines how the colors of the color map are scaled. The distance map colors are normalized according to this value. If set to zero, the color map is normalized using the largest distance that was found and the colors are spaced evenly over the distance map. A small value will produce a color map with concentrated colors, while a larger value will stretch the colors in the color map.' + '\n\n' '* Positive Color' + '\n' 'Color that is used for positive distances.' + '\n\n' '* Negative Color' + '\n' 'Color that is used for negative distances (disabled in "Nearest" mode).' + '\n\n' '* Out Of Range Color' + '\n' 'Color that is used when no raycast hit was found (disabled in "Nearest" mode).' + '\n\n' '* Show Distances' '\n' 'Display the distances of the active distance map in the viewport. Select the desired object and distance map (Properties > Object Data Properties > Vertex Colors) to view the distance per vertex.' + '\n\n' '* Font Size' '\n' 'The font size of the distances in the viewport.' + '\n\n' '* Decimals' '\n' 'The number of decimals of the distances in the viewport.' + '\n\n' '* Font Color' + '\n' 'The font color of the distances in the viewport.' + '\n\n' '* Export Distances' + '\n' 'Export the distances of a distance map to a text file. Select one object and the desired distance map (Properties > Object Data Properties > Vertex Colors). The values can be copied to other software for further analysis. In the text file, row index corresponds to vertex index (both starting at 0). A "nan" value indicates that there was no raycast hit for this vertex.'

        #write readme
        file = open(self.filepath, 'w')
        file.write(readme)
        return {'FINISHED'}

    def invoke(self, context, event):
        #open explorer
        context.window_manager.fileselect_add(self)

        #set path and file name
        defaultFileName = 'readme.txt'
        if os.path.split(self.filepath)[1] != 'readme.txt':
            self.filepath = self.filepath + defaultFileName
        return {'RUNNING_MODAL'}

class OBJECT_OT_distanceMap_operator(bpy.types.Operator):
    """Generate distance map of two selected mesh objects (saved under Properties > Object Data Properties > Vertex Colors)"""
    bl_idname = "object.generatedistancemap"
    bl_label = "Generate Distance Map"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) == 2 and bpy.context.selected_objects[0].type == 'MESH' and bpy.context.selected_objects[1].type == 'MESH'

    def execute(self, context):
        #assign base object
        baseObject = bpy.context.active_object
        baseWorldMatrix = np.array(baseObject.matrix_world)

        baseVerts = []
        baseVertIndices = []
        baseNormals = []
        for v in baseObject.data.vertices:
            baseVerts.append(baseObject.matrix_world @ v.co)
            baseVertIndices.append(v.index)
            baseNormals.append(baseWorldMatrix[0:3,0:3] @ v.normal)

        #assign target object
        targetObject = bpy.context.selected_objects
        targetObject.remove(baseObject)
        targetObject = targetObject[0]

        targetPolygons = []
        targetVerts = []
        for f in targetObject.data.polygons:
            currentPolygon = []
            for loopIndex in f.loop_indices:
                currentPolygon.append(targetObject.data.loops[loopIndex].vertex_index)
            targetPolygons.append(currentPolygon)

        for v in targetObject.data.vertices:
            targetVerts.append(targetObject.matrix_world @ v.co)

        #build target tree
        targetTree = mu.bvhtree.BVHTree.FromPolygons(targetVerts, targetPolygons, all_triangles = False, epsilon = 0.0)

        #raycast procedure
        lookupTable = []
        for v in range(len(baseObject.data.vertices)):
                lookupTable.append([])
        maxDistance = 0

        #normals raycast mode
        if bpy.context.scene.raycastMode == 'normals':
            for i, vertCo in enumerate(baseVerts):
                vertIndex = baseVertIndices[i]
                raycastPositive = targetTree.ray_cast(vertCo, baseNormals[i], 10**10)[3]
                raycastNegative = targetTree.ray_cast(vertCo, -baseNormals[i], 10**10)[3]

                #build lookup table
                if raycastNegative == None and raycastPositive == None:
                    lookupTable[vertIndex] = None #no raycast hit
                elif raycastNegative == None:
                    lookupTable[vertIndex] = -raycastPositive #only positive raycast hit
                elif raycastPositive == None:
                    lookupTable[vertIndex] = raycastNegative #only negative raycast hit
                elif np.abs(raycastNegative) < np.abs(raycastPositive):
                    lookupTable[vertIndex] = raycastNegative #negative raycast hit is smaller than positive
                elif np.abs(raycastNegative) >= np.abs(raycastPositive):
                    lookupTable[vertIndex] = -raycastPositive #positive raycast hit is smaller than or equal to negative

                #iteratively determine maximum distance (ignore [] and None)
                if lookupTable[vertIndex] is not None:
                    if np.abs(lookupTable[vertIndex]) > maxDistance:
                        maxDistance = np.abs(lookupTable[vertIndex])

        #nearest raycast mode
        elif bpy.context.scene.raycastMode == 'nearest':
            for i, vertCo in enumerate(baseVerts):
                vertIndex = baseVertIndices[i]
                raycast = targetTree.find_nearest(vertCo, 10**10)

                #build lookup table
                lookupTable[vertIndex] = raycast[3]

                #iteratively determine maximum distance (ignore [])
                if np.abs(lookupTable[vertIndex]) > maxDistance:
                     maxDistance = np.abs(lookupTable[vertIndex])

        #random seed for map ID
        seed = random.randint(0,100000)

        #include target object, raycast mode and maximum value in map name
        mapID = 'DM' #+ targetObject.name + '_' + bpy.context.scene.raycastMode + '_max:' + str(round(maxDistance,2)) + '_ID=' + str(seed)

        #add lookup table to custom properties of object
        lookupTableCustomProp = copy.deepcopy(lookupTable)
        for count, item in enumerate(lookupTableCustomProp):
            if item is None:
                lookupTableCustomProp[count] = 10**9 #replace None with 10**9; only float, int or dict allowed in custom properties, but dict is very slow, float and int do not allow None
            #future release: elif item is []: lookupTableCustomProp[count] = -10**9
        baseObject[mapID] = lookupTableCustomProp

        #lookup table normalization
        if bpy.context.scene.normValue == 0:
            normValue = maxDistance
        else:
            normValue = bpy.context.scene.normValue

        lookupTableNorm = copy.deepcopy(lookupTable)
        for count, item in enumerate(lookupTableNorm):
            if item is not None and item != [] and normValue != 0: #None for no raycast hit, [] for unselected (future release)
                lookupTableNorm[count] = item / normValue
                if lookupTableNorm[count] > 1.0: #clip values above 1.0
                    lookupTableNorm[count] = 1.0
                elif lookupTableNorm[count] < -1.0: #clip values below -1.0
                    lookupTableNorm[count] = -1.0

        #color assignment, sRGB to RGB (gamma correction of 2.2)
        positiveColorRGB = np.power(bpy.context.scene.positiveColor, 1 / 2.2)
        negativeColorRGB = np.power(bpy.context.scene.negativeColor, 1 / 2.2)
        outOfRangeColorRGB = np.power(bpy.context.scene.outOfRangeColor, 1 / 2.2)

        #blender only allows 8 vertex color maps
        if len(baseObject.data.vertex_colors) < 8:
            colorLayer = baseObject.data.vertex_colors.new(name = mapID)
            baseObject.data.vertex_colors.active = colorLayer

            #color assignment works by iterating over every corner of every polygon
            for f in baseObject.data.polygons:
                for loopIndex in f.loop_indices:
                    vertIndex = baseObject.data.loops[loopIndex].vertex_index
                    if lookupTableNorm[vertIndex] == None:
                        colorLayer.data[loopIndex].color = [outOfRangeColorRGB[0], outOfRangeColorRGB[1], outOfRangeColorRGB[2], 1] #no raycast hit
                    elif lookupTableNorm[vertIndex] >= 0:
                        vertColor = [1 - (1 - i) * np.abs(lookupTableNorm[vertIndex]) for i in positiveColorRGB] #gradient to white for smaller distances
                        colorLayer.data[loopIndex].color = [vertColor[0], vertColor[1], vertColor[2], 1] #positive raycast hit
                    elif lookupTableNorm[vertIndex] < 0:
                        vertColor = [1 - (1 - i) * np.abs(lookupTableNorm[vertIndex]) for i in negativeColorRGB] #gradient to white for smaller distances
                        colorLayer.data[loopIndex].color = [vertColor[0], vertColor[1], vertColor[2], 1] #negative raycast hit

        #error message if maximum of vertex color maps is reached
        else:
            self.report({'ERROR'}, "Maximum number of vertex color maps reached (8).")

        #set shading to solid and color to vertex for every 3d viewport
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'
        return {'FINISHED'}

class OBJECT_OT_showDistances_operator(bpy.types.Operator):
    """Show true distances of active distance map when object is selected"""
    bl_idname = "object.showdistances"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        if globalVars.DM:
            #switch show/hide status
            globalVars.DM = 0

            #add handler (text is drawn every frame)
            bpy.types.SpaceView3D.draw_handler_remove(globalVars.drawHandle, 'WINDOW')

            #redraw scene
            bpy.ops.wm.redraw_timer(type = 'DRAW_WIN_SWAP', iterations = 1)
            return {'FINISHED'}
        else:
            #switch show/hide status
            globalVars.DM = 1

            #remove handler (text is drawn every frame)
            globalVars.drawHandle = bpy.types.SpaceView3D.draw_handler_add(drawTextCallback, (bpy.context, None), 'WINDOW', 'POST_PIXEL')

            #redraw scene
            bpy.ops.wm.redraw_timer(type = 'DRAW_WIN_SWAP', iterations = 1)
            return {'RUNNING_MODAL'}

class OBJECT_OT_exportDistances_operator(bpy.types.Operator):
    """Export distances of active distance map of active object to file"""
    bl_idname = "object.exportdistances"
    bl_label = "Export Distances"
    filepath: bpy.props.StringProperty(subtype = "FILE_PATH")

    @classmethod
    def poll(cls, context):
        object = bpy.context.active_object
        if object != None:
            return len(context.selected_objects) == 1 and len(object.data.vertex_colors) > 0 and object.data.vertex_colors.active.name in object.keys()

    def execute(self, context):
        object =  bpy.context.active_object
        if len(object.data.vertex_colors) > 0: #if there is at least one vertex color map
            if object.data.vertex_colors.active.name in object.keys(): #check if color map name corresponds to one of the object's custom properties
                mapID = object.data.vertex_colors.active.name #retrieve active color map name
                #lookupTable = np.array([item for item in object[mapID].values()], dtype = np.float) #retrieve lookup table from custom properties
                lookupTable = object[mapID].to_list()
                for count, item in enumerate(lookupTable):
                    if item == 10**9:
                        lookupTable[count] = np.nan

        #write distances
        np.savetxt(self.filepath, np.array(lookupTable), fmt = "%.3f")
        return {'FINISHED'}

    def invoke(self, context, event):
        #open explorer
        context.window_manager.fileselect_add(self)

        #set path and file name
        defaultFileName = 'distances.txt'
        if os.path.split(self.filepath)[1] != 'distances.txt':
            self.filepath = self.filepath + defaultFileName
        return {'RUNNING_MODAL'}

class OBJECT_PT_distanceMap_panel(bpy.types.Panel):
    bl_category = "Distance Map"
    bl_label = "Distance Map"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"

    def draw(self, context):
        #readme panel
        layout = self.layout
        row = layout.row()
        row.alignment = "RIGHT"
        row.scale_x = 2
        row.operator("object.distancemapreadme", text = "", icon = "QUESTION")
        layout.separator()

        #color map panel
        layout.label(text = "Color Map Settings")
        layout.operator("object.generatedistancemap")
        row = layout.row()
        row.label(text = "Raycast Mode")
        row.prop(context.scene, "raycastMode", text = "")
        layout.prop(context.scene, "normValue", text = "Normalization Value")
        layout.prop(context.scene, "positiveColor", text = "Positive Color")
        row = layout.row()
        row.prop(context.scene, "negativeColor", text = "Negative Color")
        if bpy.context.scene.raycastMode == 'nearest':
            row.enabled = False
        row = layout.row()
        row.prop(context.scene, "outOfRangeColor", text = "Out Of Range Color")
        if bpy.context.scene.raycastMode == 'nearest':
            row.enabled = False
        layout.separator()

        #text map panel
        layout.label(text = "Text Map Settings")
        if globalVars.DM:
            txt = "Hide Distances"
        else:
            txt = "Show Distances"
        layout.operator("object.showdistances", text = txt)
        layout.prop(context.scene, "fontSize", text = "Font Size")
        layout.prop(context.scene, "decimals", text = "Decimals")
        layout.prop(context.scene, "fontColor", text = "Font Color")
        layout.operator("object.exportdistances")

class globalVars():
    pass

classes = (
    OBJECT_OT_distanceMapReadme_operator,
    OBJECT_OT_distanceMap_operator,
    OBJECT_OT_showDistances_operator,
    OBJECT_OT_exportDistances_operator,
    OBJECT_PT_distanceMap_panel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    globalVars.DM = 0

    bpy.types.Scene.raycastMode = bpy.props.EnumProperty(
        items = [("normals", "Normals", "Shortest distance to target object along positive or negative direction of vertex normals"),
        ("nearest", "Nearest", "Shortest distance to target object in any direction (only positive colors).")])
    bpy.types.Scene.normValue = bpy.props.FloatProperty(
        description = "Normalization value for color map scaling. If set to 0, colors are normalized using the largest distance that was found",
        default = 0, min = 0)
    bpy.types.Scene.positiveColor = bpy.props.FloatVectorProperty(
        name = "Positive color",
        subtype = 'COLOR', min = 0, max = 1,
        default = (1.0, 0.0, 0.0)) # gamma corrected Red
    bpy.types.Scene.negativeColor = bpy.props.FloatVectorProperty(
        name = "Negative color",
        subtype = 'COLOR', min = 0, max = 1,
        default = (0.0, 1.0, 0.0)) #gamma corrected Green
    bpy.types.Scene.outOfRangeColor = bpy.props.FloatVectorProperty(
        name = "Out of range color",
        subtype = 'COLOR', min = 0, max = 1,
        default = (0.0, 0.0, 1.0)) #gamma corrected Blue
    bpy.types.Scene.fontSize = bpy.props.IntProperty(
        description = "Font size",
        default = 15, min = 1)
    bpy.types.Scene.decimals = bpy.props.IntProperty(
        description = "Number of decimals",
        default = 1, min = 0, max = 10)
    bpy.types.Scene.fontColor = bpy.props.FloatVectorProperty(
        name = "Font color",
        subtype = 'COLOR', min = 0, max = 1,
        default = (1.0, 1.0, 1.0)) #white

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
