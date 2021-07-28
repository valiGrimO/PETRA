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

        # Note: this is in millimetres.
        self.spatial_resolution = params.spatial_resolution

        self.resolution_of_image = round(
            self.documentation_scale / (self.spatial_resolution / 25.4)
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

    result["nomObjetDocumenté"] = "this is a test"

    rotations = blenderdata.framing_box.rotation_euler
    result["definitionBoiteEnglobante"]["rotationY"] = rotations[0]
    result["definitionBoiteEnglobante"]["rotationY"] = f"{rotations[1]}°"
    result["definitionBoiteEnglobante"]["rotationZ"] = "this is a test"

    item = result["caracteristiquesImage"]
    item["echelleDocumentation"] = blenderdata.documentation_scale_fraction

    result["cameras"][0]["nomDeLaVue"] = blenderdata.cam_01.name

    ########################################################

    save_yaml(result, filepath)
