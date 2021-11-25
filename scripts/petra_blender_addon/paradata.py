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

    rotations = blenderdata.framing_box.rotation_euler
    fB["rotationX"] = f"{rotations[0]}°"
    fB["rotationY"] = f"{rotations[1]}°"
    fB["rotationZ"] = f"{rotations[2]}°"

    dimensions = blenderdata.framing_box.scale
    fB["dimensionX"] = f"{dimensions[0]} m"
    fB["dimensionY"] = f"{dimensions[1]} m"
    fB["dimensionZ"] = f"{dimensions[2]} m"

    pS = result["projectSetup"]
    pS["echelleDocumentation"] = blenderdata.documentation_scale_fraction
    pS["imageResolution"] = "_ ppi" #blenderdata.image_resolution
    pS["spatialResolution"] = f"1 pixel covers {blenderdata.spatial_resolution} mm"

    cam = result["cameras"]
    cam[0]["name"] = blenderdata.cam_01.name
    cam[0]["parametresImage"]["orthographicScale"] = "_ x _ m"
    cam[0]["parametresImage"]["dimensionsCm"] = "_ x _ cm"
    cam[0]["parametresImage"]["dimensionsPixel"] = "_ x _ pixels"

    ########################################################

    save_yaml(result, filepath)
