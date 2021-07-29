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

    # begining of yaml file

    # Note: if `blenderdata` misses a value,
    # then edit the BlenderData class above.
    blenderdata = BlenderData(context)

    # title
    result["nomObjetDocumenté"] = "Fill it manually for the moment" # Have to find where to get the name
    
    # definition Framing Box
    framingBox = result["definitionBoiteEnglobante"]
    framingBox["locationX"] = f"{locations[0]} m"
    framingBox["locationY"] = f"{locations[1]} m"
    framingBox["locationZ"] = f"{locations[2]} m"

    rotations = blenderdata.framing_box.rotation_euler
    framingBox["rotationX"] = f"{rotations[0]}°"
    framingBox["rotationY"] = f"{rotations[1]}°"
    framingBox["rotationZ"] = f"{rotations[2]}°"
    
    framingBox["dimensionX"] = f"{scale[0]} m"
    framingBox["dimensionY"] = f"{scale[1]} m"
    framingBox["dimensionZ"] = f"{scale[2]} m"

    # caracteristiques documentation
    docInfo = result["caracteristiquesImage"]
    docInfo["echelleDocumentation"] = blenderdata.documentation_scale_fraction
    docInfo["resolutionImage"] = blenderdata.resolution_of_image "ppi"
    docInfo["resolutionSpatiale"] = "1 px = " blenderdata.spatial_resolution "mm"

    # cameras
    # we should find a way to apply this to each camera present in the collection 'PETRA'
    
    Cam_01 = result["cameras"][0]
    Cam_01["nomDeLaVue"] = blenderdata.cam_01.name
    
    Cam_01["parametresImage"]["orthographicScale"] = 
    Cam_01["parametresImage"]["dimensionsCm"] = 
    Cam_01["parametresImage"]["dimensionsPixel"] = 
    
    Cam_01["parametresCamera"]["clippingStart"] = f"{bpy.data.cameras["Cam-01"].clip_start} m"
    Cam_01["parametresCamera"]["clippingEnd"] = f"{bpy.data.cameras["Cam-01"].clip_end} m"
    
    Cam_01["parametresCamera"]["shiftX"] = f"{bpy.data.cameras["Cam-01"].shift_x} m"
    Cam_01["parametresCamera"]["shiftY"] = f"{bpy.data.cameras["Cam-01"].shift_y} m"
    
    Cam_01["parametresCamera"]["relativeLocationX"] = f"{bpy.data.objects["Cam-01"].location[0]} m"
    Cam_01["parametresCamera"]["relativeLocationY"] = f"{bpy.data.objects["Cam-01"].location[1]} m"
    Cam_01["parametresCamera"]["relativeLocationZ"] = f"{bpy.data.objects["Cam-01"].location[2]} m"
    
    Cam_01["parametresCamera"]["relativeRotationX"] = f"{bpy.data.objects["Cam-01"].rotation[0]} m"
    Cam_01["parametresCamera"]["relativeRotationY"] = f"{bpy.data.objects["Cam-01"].rotation[1]} m"
    Cam_01["parametresCamera"]["relativeRotationZ"] = f"{bpy.data.objects["Cam-01"].rotation[2]} m"

    # end of yaml file

    save_yaml(result, filepath)
