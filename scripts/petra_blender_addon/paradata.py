"""
Tools to extract parameter data from Blender and save it.
"""

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

    ########################################################
    #    VALENTIN TODO: COMPLETE CODE BETWEEN THE LINES    #
    ########################################################

    # Note: if `blenderdata` misses a value,
    # then edit the BlenderData class above.
    blenderdata = BlenderData(context)

    result["documentedObject"] = "_" # insert the name of selected meshes

    fB = result["framingBox"]
    locations = blenderdata.framing_box.location
    fB["locationX"] = f"{locations[0]} m"
    fB["locationY"] = f"{locations[1]} m"
    fB["locationZ"] = f"{locations[2]} m"

    rotations_fB = blenderdata.framing_box.rotation_euler
    fB["rotationX"] = f"{rotations_fB[0]}°"
    fB["rotationY"] = f"{rotations_fB[1]}°"
    fB["rotationZ"] = f"{rotations_fB[2]}°"

    dimensions = blenderdata.framing_box.scale
    fB["dimensionX"] = f"{dimensions[0]} m"
    fB["dimensionY"] = f"{dimensions[1]} m"
    fB["dimensionZ"] = f"{dimensions[2]} m"

    sS = result["sceneSettings"]
    sS["documentationScale"] = varA = blenderdata.documentation_scale_fraction
    sS["spatialResolution"] = varB = f"1 pixel covers {blenderdata.spatial_resolution} mm"
    varC = round(varA/(varB/25.4))
    sS["imageResolution"] = f"{varC} ppi"

# If we can create a loop for every camera in the scene (except for location and rotation), it would be awesome!

    # select cam_01
    cam = result["cameras"]
    cam[0]["name"] = blenderdata.cam_01.name
    cam[0]["imageSettings"]["orthographicScale"] = f"{blenderdata.orthoscale} m" # where can I get orthographic scale?
    cam[0]["imageSettings"]["printedSize_cm"] = "_ x _ cm" # where can I get the printed size?
    # cam[0]["imageSettings"]["printedSize_px"] = f"{blenderdata.render.resolution_x} x {blenderdata.render.resolution_y} pixels"
    # AttributeError: 'BlenderData' object has no attribute 'render'

    # cam[0]["cameraSettings"]["clippingStart"] = blenderdata.cameras.clip_start
    # cam[0]["cameraSettings"]["clippingEnd"] = blenderdata.cameras.clip_end
    # cam[0]["cameraSettings"]["shiftX"] = blenderdata.cameras.shift_x
    # cam[0]["cameraSettings"]["shiftY"] = blenderdata.cameras.shift_y

    # bpy.ops.view3d.snap_cursor_to_selected()      or: snap_cursor_to["cam_01"]
    # cam[0]["cameraSettings"]["locationX"] = blenderdata.cursor.location[0] # bpy.data.scenes["Scene"].cursor.location[0]
    # cam[0]["cameraSettings"]["locationY"] = blenderdata.cursor.location[1]
    # cam[0]["cameraSettings"]["locationZ"] = blenderdata.cursor.location[2]
    rotations_cam01 = blenderdata.cam_01.rotation_euler
    cam[0]["cameraSettings"]["rotationX"] = f"{rotations_fB[0]+rotations_cam01[0]+90}°"
    cam[0]["cameraSettings"]["rotationY"] = f"{rotations_fB[1]+rotations_cam01[2]}°"
    cam[0]["cameraSettings"]["rotationZ"] = f"{rotations_fB[2]+rotations_cam01[2]}°"

    ########################################################

    save_yaml(result, filepath)
