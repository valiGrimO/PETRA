"""
Tools to extract parameter data from Blender and save it.
"""

import bpy # il faudrait trouver un moyen pour ne pas l'utiliser...
import math
import addon_utils
import datetime

from fractions import Fraction
from pathlib import Path

from .filetools import read_yaml, save_yaml


YAML_TEMPLATE_FILEPATH = Path(__file__).parent / "templates" / "paradata.yaml"


class BlenderData:
    """Class for data we extracted from Blender."""

    def __init__(self, context):
        """
        Extract data from Blender for use in various places.

        Parameters
        ----------
        context: bpy.types.Context
            Current windowmanager and data context. Akin to `bpy.context`.

        Examples
        --------
        >>> from petra_blender_addon.paradata import BlenderData
        >>> b = BlenderData(bpy.context)
        >>> b.documentation_scale_fraction
        '1/20'
        >>> vars(b)
        ...
        """
        # Collect objects from Blender
        # --------------------------------------------------
        collection = context.scene.collection.children["PETRA"]
        objects = collection.objects
        params = context.scene.petra

        # Assign to local names
        # --------------------------------------------------
        self.framing_box = objects["Framing Box"]        
        
        self.cam_01 = objects["Cam-01"]
        self.cam_02 = objects["Cam-02"]
        self.cam_03 = objects["Cam-03"]
        self.cam_04 = objects["Cam-04"]
        self.cam_05 = objects["Cam-05"]
        self.cam_06 = objects["Cam-06"]

        self.documentation_scale = params.documentation_scale  # float
        # Experimental. Works well for 1/10 and 1/20.
        # Does not work well for 1/30,
        self.documentation_scale_fraction = str(
            round(Fraction(params.documentation_scale), 7)
        )

        # Note: this is unscaled and in millimetres per pixel.
        self.spatial_resolution = params.spatial_resolution

        # Note: this is scaled and in pixels per inch.
        self.resolution_of_image = round(
            25.4 / (self.documentation_scale * self.spatial_resolution)
        )
        
        
        '''
        Experimentation...
        '''
        
        # Contour lines
        CL = bpy.data.materials["R2_CL"].node_tree.nodes["value"].outputs[0].default_value
        self.CL1 = CL
        self.CL2 = CL * 5
        self.CL3 = CL * 10
        
        '''
        # Scale bar
        self.sca1 = round(blenderdata.documentation_scale*2000, 3)
        self.sca2 = round(blenderdata.documentation_scale*1000, 3)
        self.sca3 = round(blenderdata.documentation_scale*400, 3)
        self.sca4 = round(blenderdata.documentation_scale*200, 3)
        self.sca5 = round(blenderdata.documentation_scale*100, 3)
        '''
        
        '''
        End of experimentation!!!
        '''
        
        


def generate_yaml(context, filepath):
    """
    Extract information from Blender's data and save to a YAML file.

    Parameters
    ----------
    context : bpy.types.Context
        Current windowmanager and data context.

    filepath : str or Path
        Absolute path of YAML file to save to.

    Examples
    --------
    >>> generate_yaml(bpy.data, '/home/vgrimaud/test.yaml')

    """
    result = read_yaml(YAML_TEMPLATE_FILEPATH)

    #########################################
    #    COMPLETE CODE BETWEEN THE LINES    #
    #########################################

    # Note: if `blenderdata` misses a value,
    # then edit the BlenderData class above.
    blenderdata = BlenderData(context)
    C = bpy.context
    
    
    # Software version
    ## Blender
    blenderVersion = bpy.app.version_string
    
    ## PETRA
    for mod in addon_utils.modules():
    	if mod.bl_info['name'] == 'PETRA':
        	name = str(mod.bl_info.get('name'))
        	version = str(mod.bl_info.get('version'))
        	petraVersion = name + " " + version
    
    result["Blender_version"] = "Blender " + blenderVersion
    result["PETRA_version"] = petraVersion
    
    now = datetime.datetime.now()
    today = (now.strftime('%d-%m-%Y'))
    result["documentationDate"] = today
    
    
    # documentedObject.name
    documentedObject = C.selected_objects[0]
    docOb = result["documentedObject"]
    docOb["name"] = f"{documentedObject.name}"
    
    
    # documentedObject.location
    docOb_L = documentedObject.location
    docOb_LX = round(docOb_L[0], 6)
    docOb_LY = round(docOb_L[1], 6)
    docOb_LZ = round(docOb_L[2], 6)
    docOb["location"] = f"{docOb_LX} m, {docOb_LY} m, {docOb_LZ} m"
    
    
    # documentedObject.rotation
    docOb_R = documentedObject.rotation_euler #in radians

    docOb_RX = round(math.degrees(docOb_R[0]), 6)
    docOb_RY = round(math.degrees(docOb_R[1]), 6)
    docOb_RZ = round(math.degrees(docOb_R[2]), 6)
    
    docOb["rotation"] = f"{docOb_RX}°, {docOb_RY}°, {docOb_RZ}°"
    
    
    # documentedObject.scale
    docOb_S = documentedObject.scale

    docOb_SX = round(docOb_S[0], 6)
    docOb_SY = round(docOb_S[1], 6)
    docOb_SZ = round(docOb_S[2], 6)
    
    docOb["scale"] = f"{docOb_SX}, {docOb_SY}, {docOb_SZ}"
    
    
    # framingBox.location
    fB = result["framingBox"]
    
    fB_L = blenderdata.framing_box.location
    fB_LX = round(fB_L[0], 6)
    fB_LY = round(fB_L[1], 6)
    fB_LZ = round(fB_L[2], 6)
    
    fB["location"] = f"{fB_LX} m, {fB_LY} m, {fB_LZ} m"
    
    
    # framingBox.rotation
    fB_R = blenderdata.framing_box.rotation_euler #in radians
    
    fB_RX = round(math.degrees(fB_R[0]), 6)
    fB_RY = round(math.degrees(fB_R[1]), 6)
    fB_RZ = round(math.degrees(fB_R[2]), 6)
    
    fB["rotation"] = f"{fB_RX}°, {fB_RY}°, {fB_RZ}°"
    
    
    # framingBox.dimensions
    fB_S = blenderdata.framing_box.scale
    
    fB["dimension"] = f"{fB_S[0]} m, {fB_S[1]} m, {fB_S[2]} m"
    
    
    # documentationSettings
    dS = result["documentationSettings"]
    dS["documentationScale"] = blenderdata.documentation_scale_fraction
    dS["imageResolution"] = f"{blenderdata.resolution_of_image} ppi"
    dS["spatialResolution"] = f"1 pixel covers {blenderdata.spatial_resolution} mm"
    
    
    # Layer of information
    distance = bpy.data.materials["R2_CL"].node_tree.nodes["value"].outputs[0].default_value
    dist1 = str(distance)
    dist2 = str(distance*5)
    dist3 = str(distance*10)

    loi = result["layerOfInformation"]
    loi["R2_contourlines"]["R2_CL1"] = f"{dist1} mm"
    loi["R2_contourlines"]["R2_CL2"] = f"{dist2} mm"
    loi["R2_contourlines"]["R2_CL3"] = f"{dist3} mm"
    
    # cam.name
    cam = result["cameras"]
    cam[0]["name"] = blenderdata.cam_01.name
    cam[1]["name"] = blenderdata.cam_02.name
    cam[2]["name"] = blenderdata.cam_03.name
    cam[3]["name"] = blenderdata.cam_04.name
    cam[4]["name"] = blenderdata.cam_05.name
    cam[5]["name"] = blenderdata.cam_06.name
    
    
    # cam.absoluteLocation
    cam_01_aLocX = round(blenderdata.cam_01.matrix_world[0][3], 6)
    cam_01_aLocY = round(blenderdata.cam_01.matrix_world[1][3], 6)
    cam_01_aLocZ = round(blenderdata.cam_01.matrix_world[2][3], 6)
    
    cam_02_aLocX = round(blenderdata.cam_02.matrix_world[0][3], 6)
    cam_02_aLocY = round(blenderdata.cam_02.matrix_world[1][3], 6)
    cam_02_aLocZ = round(blenderdata.cam_02.matrix_world[2][3], 6)
    
    cam_03_aLocX = round(blenderdata.cam_03.matrix_world[0][3], 6)
    cam_03_aLocY = round(blenderdata.cam_03.matrix_world[1][3], 6)
    cam_03_aLocZ = round(blenderdata.cam_03.matrix_world[2][3], 6)
    
    cam_04_aLocX = round(blenderdata.cam_04.matrix_world[0][3], 6)
    cam_04_aLocY = round(blenderdata.cam_04.matrix_world[1][3], 6)
    cam_04_aLocZ = round(blenderdata.cam_04.matrix_world[2][3], 6)
    
    cam_05_aLocX = round(blenderdata.cam_05.matrix_world[0][3], 6)
    cam_05_aLocY = round(blenderdata.cam_05.matrix_world[1][3], 6)
    cam_05_aLocZ = round(blenderdata.cam_05.matrix_world[2][3], 6)
    
    cam_06_aLocX = round(blenderdata.cam_06.matrix_world[0][3], 6)
    cam_06_aLocY = round(blenderdata.cam_06.matrix_world[1][3], 6)
    cam_06_aLocZ = round(blenderdata.cam_06.matrix_world[2][3], 6)
    
    cam[0]["cameraSettings"]["absoluteLocation"] = f"{cam_01_aLocX} m, {cam_01_aLocY} m, {cam_01_aLocZ} m"
    cam[1]["cameraSettings"]["absoluteLocation"] = f"{cam_02_aLocX} m, {cam_02_aLocY} m, {cam_02_aLocZ} m"
    cam[2]["cameraSettings"]["absoluteLocation"] = f"{cam_03_aLocX} m, {cam_03_aLocY} m, {cam_03_aLocZ} m"
    cam[3]["cameraSettings"]["absoluteLocation"] = f"{cam_04_aLocX} m, {cam_04_aLocY} m, {cam_04_aLocZ} m"
    cam[4]["cameraSettings"]["absoluteLocation"] = f"{cam_05_aLocX} m, {cam_05_aLocY} m, {cam_05_aLocZ} m"
    cam[5]["cameraSettings"]["absoluteLocation"] = f"{cam_06_aLocX} m, {cam_06_aLocY} m, {cam_06_aLocZ} m"
    

    # cam.absoluteRotation
    cam_01_aRot = blenderdata.cam_01.matrix_world.to_euler()
    cam_01_aRotX = round(math.degrees(cam_01_aRot[0]), 6)
    cam_01_aRotY = round(math.degrees(cam_01_aRot[1]), 6)
    cam_01_aRotZ = round(math.degrees(cam_01_aRot[2]), 6)
    
    cam_02_aRot = blenderdata.cam_02.matrix_world.to_euler()
    cam_02_aRotX = round(math.degrees(cam_02_aRot[0]), 6)
    cam_02_aRotY = round(math.degrees(cam_02_aRot[1]), 6)
    cam_02_aRotZ = round(math.degrees(cam_02_aRot[2]), 6)
    
    cam_03_aRot = blenderdata.cam_03.matrix_world.to_euler()
    cam_03_aRotX = round(math.degrees(cam_03_aRot[0]), 6)
    cam_03_aRotY = round(math.degrees(cam_03_aRot[1]), 6)
    cam_03_aRotZ = round(math.degrees(cam_03_aRot[2]), 6)
    
    cam_04_aRot = blenderdata.cam_04.matrix_world.to_euler()
    cam_04_aRotX = round(math.degrees(cam_04_aRot[0]), 6)
    cam_04_aRotY = round(math.degrees(cam_04_aRot[1]), 6)
    cam_04_aRotZ = round(math.degrees(cam_04_aRot[2]), 6)
    
    cam_05_aRot = blenderdata.cam_05.matrix_world.to_euler()
    cam_05_aRotX = round(math.degrees(cam_05_aRot[0]), 6)
    cam_05_aRotY = round(math.degrees(cam_05_aRot[1]), 6)
    cam_05_aRotZ = round(math.degrees(cam_05_aRot[2]), 6)
    
    cam_06_aRot = blenderdata.cam_06.matrix_world.to_euler()
    cam_06_aRotX = round(math.degrees(cam_06_aRot[0]), 6)
    cam_06_aRotY = round(math.degrees(cam_06_aRot[1]), 6)
    cam_06_aRotZ = round(math.degrees(cam_06_aRot[2]), 6)
    
    cam[0]["cameraSettings"]["absoluteRotation"] = f"{cam_01_aRotX}°, {cam_01_aRotY}°, {cam_01_aRotZ}°"
    cam[1]["cameraSettings"]["absoluteRotation"] = f"{cam_02_aRotX}°, {cam_02_aRotY}°, {cam_02_aRotZ}°"
    cam[2]["cameraSettings"]["absoluteRotation"] = f"{cam_03_aRotX}°, {cam_03_aRotY}°, {cam_03_aRotZ}°"
    cam[3]["cameraSettings"]["absoluteRotation"] = f"{cam_04_aRotX}°, {cam_04_aRotY}°, {cam_04_aRotZ}°"
    cam[4]["cameraSettings"]["absoluteRotation"] = f"{cam_05_aRotX}°, {cam_05_aRotY}°, {cam_05_aRotZ}°"
    cam[5]["cameraSettings"]["absoluteRotation"] = f"{cam_06_aRotX}°, {cam_06_aRotY}°, {cam_06_aRotZ}°"
    
    
    # cam.relativeLocation
    cam[0]["cameraSettings"]["relativeLocation"] = f"{blenderdata.cam_01.location[0]} m, {blenderdata.cam_01.location[1]} m, {blenderdata.cam_01.location[2]} m"
    cam[1]["cameraSettings"]["relativeLocation"] = f"{blenderdata.cam_02.location[0]} m, {blenderdata.cam_02.location[1]} m, {blenderdata.cam_02.location[2]} m"
    cam[2]["cameraSettings"]["relativeLocation"] = f"{blenderdata.cam_03.location[0]} m, {blenderdata.cam_03.location[1]} m, {blenderdata.cam_03.location[2]} m"
    cam[3]["cameraSettings"]["relativeLocation"] = f"{blenderdata.cam_04.location[0]} m, {blenderdata.cam_04.location[1]} m, {blenderdata.cam_04.location[2]} m"
    cam[4]["cameraSettings"]["relativeLocation"] = f"{blenderdata.cam_05.location[0]} m, {blenderdata.cam_05.location[1]} m, {blenderdata.cam_05.location[2]} m"
    cam[5]["cameraSettings"]["relativeLocation"] = f"{blenderdata.cam_06.location[0]} m, {blenderdata.cam_06.location[1]} m, {blenderdata.cam_06.location[2]} m"
    
    
    # cam.relativeRotation
    cam_01_rRotX = round(math.degrees(blenderdata.cam_01.rotation_euler[0]), 3)
    cam_01_rRotY = round(math.degrees(blenderdata.cam_01.rotation_euler[1]), 3)
    cam_01_rRotZ = round(math.degrees(blenderdata.cam_01.rotation_euler[2]), 3)
    
    cam_02_rRotX = round(math.degrees(blenderdata.cam_02.rotation_euler[0]), 3)
    cam_02_rRotY = round(math.degrees(blenderdata.cam_02.rotation_euler[1]), 3)
    cam_02_rRotZ = round(math.degrees(blenderdata.cam_02.rotation_euler[2]), 3)
    
    cam_03_rRotX = round(math.degrees(blenderdata.cam_03.rotation_euler[0]), 3)
    cam_03_rRotY = round(math.degrees(blenderdata.cam_03.rotation_euler[1]), 3)
    cam_03_rRotZ = round(math.degrees(blenderdata.cam_03.rotation_euler[2]), 3)
    
    cam_04_rRotX = round(math.degrees(blenderdata.cam_04.rotation_euler[0]), 3)
    cam_04_rRotY = round(math.degrees(blenderdata.cam_04.rotation_euler[1]), 3)
    cam_04_rRotZ = round(math.degrees(blenderdata.cam_04.rotation_euler[2]), 3)
    
    cam_05_rRotX = round(math.degrees(blenderdata.cam_05.rotation_euler[0]), 3)
    cam_05_rRotY = round(math.degrees(blenderdata.cam_05.rotation_euler[1]), 3)
    cam_05_rRotZ = round(math.degrees(blenderdata.cam_05.rotation_euler[2]), 3)
    
    cam_06_rRotX = round(math.degrees(blenderdata.cam_06.rotation_euler[0]), 3)
    cam_06_rRotY = round(math.degrees(blenderdata.cam_06.rotation_euler[1]), 3)
    cam_06_rRotZ = round(math.degrees(blenderdata.cam_06.rotation_euler[2]), 3)
    
    cam[0]["cameraSettings"]["relativeRotation"] = f"{cam_01_rRotX}°, {cam_01_rRotY}°, {cam_01_rRotZ}°"
    cam[1]["cameraSettings"]["relativeRotation"] = f"{cam_02_rRotX}°, {cam_02_rRotY}°, {cam_02_rRotZ}°"
    cam[2]["cameraSettings"]["relativeRotation"] = f"{cam_03_rRotX}°, {cam_03_rRotY}°, {cam_03_rRotZ}°"
    cam[3]["cameraSettings"]["relativeRotation"] = f"{cam_04_rRotX}°, {cam_04_rRotY}°, {cam_04_rRotZ}°"
    cam[4]["cameraSettings"]["relativeRotation"] = f"{cam_05_rRotX}°, {cam_05_rRotY}°, {cam_05_rRotZ}°"
    cam[5]["cameraSettings"]["relativeRotation"] = f"{cam_06_rRotX}°, {cam_06_rRotY}°, {cam_06_rRotZ}°"
    
    
    # cam.clippingStart
    cam[0]["cameraSettings"]["clippingStart"] = f"{round(blenderdata.cam_01.data.clip_start, 8)} m"
    cam[1]["cameraSettings"]["clippingStart"] = f"{round(blenderdata.cam_02.data.clip_start, 8)} m"
    cam[2]["cameraSettings"]["clippingStart"] = f"{round(blenderdata.cam_03.data.clip_start, 8)} m"
    cam[3]["cameraSettings"]["clippingStart"] = f"{round(blenderdata.cam_04.data.clip_start, 8)} m"
    cam[4]["cameraSettings"]["clippingStart"] = f"{round(blenderdata.cam_05.data.clip_start, 8)} m"
    cam[5]["cameraSettings"]["clippingStart"] = f"{round(blenderdata.cam_06.data.clip_start, 8)} m"
    
    
    # cam.clippingEnd
    cam[0]["cameraSettings"]["clippingEnd"] = f"{blenderdata.cam_01.data.clip_end} m"
    cam[1]["cameraSettings"]["clippingEnd"] = f"{blenderdata.cam_02.data.clip_end} m"
    cam[2]["cameraSettings"]["clippingEnd"] = f"{blenderdata.cam_03.data.clip_end} m"
    cam[3]["cameraSettings"]["clippingEnd"] = f"{blenderdata.cam_04.data.clip_end} m"
    cam[4]["cameraSettings"]["clippingEnd"] = f"{blenderdata.cam_05.data.clip_end} m"
    cam[5]["cameraSettings"]["clippingEnd"] = f"{blenderdata.cam_06.data.clip_end} m"
    
    
    # cam.shift
    cam[0]["cameraSettings"]["shift"] = f"{blenderdata.cam_01.data.shift_x} m horizontally, {blenderdata.cam_01.data.shift_y} m vertically"
    cam[1]["cameraSettings"]["shift"] = f"{blenderdata.cam_02.data.shift_x} m horizontally, {blenderdata.cam_02.data.shift_y} m vertically"
    cam[2]["cameraSettings"]["shift"] = f"{blenderdata.cam_03.data.shift_x} m horizontally, {blenderdata.cam_03.data.shift_y} m vertically"
    cam[3]["cameraSettings"]["shift"] = f"{blenderdata.cam_04.data.shift_x} m horizontally, {blenderdata.cam_04.data.shift_y} m vertically"
    cam[4]["cameraSettings"]["shift"] = f"{blenderdata.cam_05.data.shift_x} m horizontally, {blenderdata.cam_05.data.shift_y} m vertically"
    cam[5]["cameraSettings"]["shift"] = f"{blenderdata.cam_06.data.shift_x} m horizontally, {blenderdata.cam_06.data.shift_y} m vertically"
    
    
    # IMAGE SETTINGS
    
    
    ## Orthographic Scale
    U, V, W = blenderdata.framing_box.dimensions
    U1 = round(U, 3)
    V1 = round(V, 3)
    W1 = round(W, 3)
    
    cam[0]["imageSettings"]["orthographicScale"] = f"{U1} x {W1} m"
    cam[1]["imageSettings"]["orthographicScale"] = f"{V1} x {W1} m"
    cam[2]["imageSettings"]["orthographicScale"] = f"{U1} x {W1} m"
    cam[3]["imageSettings"]["orthographicScale"] = f"{V1} x {W1} m"
    cam[4]["imageSettings"]["orthographicScale"] = f"{U1} x {V1} m"
    cam[5]["imageSettings"]["orthographicScale"] = f"{U1} x {V1} m"
    
    
    ## Printed Size
    DS = blenderdata.documentation_scale
    U2 = round(U1 * DS * 100, 2)
    V2 = round(V1 * DS * 100, 2)
    W2 = round(W1 * DS * 100, 2)
    
    cam[0]["imageSettings"]["printedSize"] = f"{U2} x {W2} cm"
    cam[1]["imageSettings"]["printedSize"] = f"{V2} x {W2} cm"
    cam[2]["imageSettings"]["printedSize"] = f"{U2} x {W2} cm"
    cam[3]["imageSettings"]["printedSize"] = f"{V2} x {W2} cm"
    cam[4]["imageSettings"]["printedSize"] = f"{U2} x {V2} cm"
    cam[5]["imageSettings"]["printedSize"] = f"{U2} x {V2} cm"
    
    
    ## Digital Size
    RI = blenderdata.resolution_of_image
    U3 = round(U2 / 2.54 * RI)
    V3 = round(V2 / 2.54 * RI)
    W3 = round(W2 / 2.54 * RI)
    
    cam[0]["imageSettings"]["digitalSize"] = f"{U3} x {W3} pixels"
    cam[1]["imageSettings"]["digitalSize"] = f"{V3} x {W3} pixels"
    cam[2]["imageSettings"]["digitalSize"] = f"{U3} x {W3} pixels"
    cam[3]["imageSettings"]["digitalSize"] = f"{V3} x {W3} pixels"
    cam[4]["imageSettings"]["digitalSize"] = f"{U3} x {V3} pixels"
    cam[5]["imageSettings"]["digitalSize"] = f"{U3} x {V3} pixels"
    
    
    ########################################################

    save_yaml(result, filepath)
