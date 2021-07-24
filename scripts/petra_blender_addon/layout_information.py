"""
Tools to generate Inkscape SVGs with layout information.
"""

from pathlib import Path

from .filetools import read, save
from .paradata import BlenderData


MODULE_PATH = Path(__file__).parent

RENDERED_IMAGES_FOLDER = "temp"
SVG_TEMPLATE_FILEPATH = MODULE_PATH / "templates" / "layout_information.svg"
LAYERS_TO_INCLUDE_FILEPATH = MODULE_PATH / "templates" / "layers_to_include.txt"

SVG_LAYERS_INSERT_AFTER_THIS = "</metadata>"


def make_svg_for_layer(layer_name, relative_directory, suffix, U2, V2, W2):
    cameras = [
        {"x": 20, "y": V2 + 30, "width": U2, "height": W2},
        {"x": U2 + 30, "y": V2 + 30, "width": V2, "height": W2},
        {"x": U2 + V2 + 40, "y": V2 + 30, "width": U2, "height": W2},
        {"x": 2 * U2 + V2 + 50, "y": V2 + 30, "width": V2, "height": W2},
        {"x": 20, "y": 20, "width": U2, "height": V2},
        {"x": 20, "y": V2 + W2 + 40, "width": U2, "height": V2},
    ]

    return f"""
  <g id="{layer_name}" inkscape:label="{layer_name}" inkscape:groupmode="layer">
    <image id="Cam-01_{layer_name}" xlink:href="{relative_directory}/Cam-01_{layer_name}{suffix}" x="{cameras[0]["x"]}" y="{cameras[0]["y"]}" width="{cameras[0]["width"]}" height="{cameras[0]["height"]}" preserveAspectRatio="none" />
    <image id="Cam-02_{layer_name}" xlink:href="{relative_directory}/Cam-02_{layer_name}{suffix}" x="{cameras[1]["x"]}" y="{cameras[1]["y"]}" width="{cameras[1]["width"]}" height="{cameras[1]["height"]}" preserveAspectRatio="none" />
    <image id="Cam-03_{layer_name}" xlink:href="{relative_directory}/Cam-03_{layer_name}{suffix}" x="{cameras[2]["x"]}" y="{cameras[2]["y"]}" width="{cameras[2]["width"]}" height="{cameras[2]["height"]}" preserveAspectRatio="none" />
    <image id="Cam-04_{layer_name}" xlink:href="{relative_directory}/Cam-04_{layer_name}{suffix}" x="{cameras[3]["x"]}" y="{cameras[3]["y"]}" width="{cameras[3]["width"]}" height="{cameras[3]["height"]}" preserveAspectRatio="none" />
    <image id="Cam-05_{layer_name}" xlink:href="{relative_directory}/Cam-05_{layer_name}{suffix}" x="{cameras[4]["x"]}" y="{cameras[4]["y"]}" width="{cameras[4]["width"]}" height="{cameras[4]["height"]}" preserveAspectRatio="none" />
    <image id="Cam-06_{layer_name}" xlink:href="{relative_directory}/Cam-06_{layer_name}{suffix}" x="{cameras[5]["x"]}" y="{cameras[5]["y"]}" width="{cameras[5]["width"]}" height="{cameras[5]["height"]}" preserveAspectRatio="none" />
  </g>"""


def generate_svg(context, filepath):
    f"""
    Generate an SVG file based on rendered images.

    Scan the rendered images directory for images matching certain
    patterns and generate an SVG file including matched images.

    Parameters
    ----------
    context: bpy.types.Context
        Current windowmanager and data context.
    filepath : str or Path
        The location to save the resulting SVG file in.

        Note: In the same directory, there should be a folder named
        "{RENDERED_IMAGES_FOLDER}" containing the rendered images.

    Examples
    --------
    >>> generate_svg('test.svg')

    """
    # Setup variables
    # --------------------------------------------------
    rendered_images_path = Path(filepath).parent / RENDERED_IMAGES_FOLDER
    layers_to_include = read(LAYERS_TO_INCLUDE_FILEPATH).split()
    svg_template = read(SVG_TEMPLATE_FILEPATH)

    blenderdata = BlenderData(context)
    U1, V1, W1 = blenderdata.framing_box.dimensions
    DS = blenderdata.documentation_scale

    # Compute
    # --------------------------------------------------
    # size of the printed images (in mm)
    U2 = round(U1 * DS * 1000, 2)
    V2 = round(V1 * DS * 1000, 2)
    W2 = round(W1 * DS * 1000, 2)

    # Stitch together the SVG.
    # --------------------------------------------------
    separator = SVG_LAYERS_INSERT_AFTER_THIS
    beginning, end = svg_template.split(separator, maxsplit=1)
    beginning += separator
    # insert blenderdata into rest of template
    for key, value in vars(blenderdata).items():
        end = end.replace(f"{{blenderdata.{key}}}", str(value))
    middle_parts = []
    current_index = 0
    for layer in layers_to_include:
        image_filename = find_file_in_directory_by_stem(
            "Cam-01_" + layer, rendered_images_path
        )
        # skip layer if image not found
        if not image_filename:
            continue

        current_index += 1
        text = make_svg_for_layer(
            layer_name=layer.replace(" ", "_"),  # Note: SVG ids can't have whitespace
            relative_directory=RENDERED_IMAGES_FOLDER,
            suffix=image_filename.suffix,
            U2=U2,  # in mm
            V2=V2,
            W2=W2,
        )
        middle_parts.append(text)
    final_svg_text = "".join((beginning, *reversed(middle_parts), end))

    save(final_svg_text, filepath)


# --------------------------------------------------
# Helpers
# --------------------------------------------------


def find_file_in_directory_by_stem(file_stem, directory):
    """
    Find a file in a directory by its stem. Return filename.

    A file's stem is the part before the dot. So for example, in the
    file "Cam-01_C1_PRV.png" the file stem is "Cam-01_C1_PRV".

    Parameters
    ----------
    file_stem : str
        The file stem to look for.

    directory : str or Path
        Absolute path to a folder.

    Returns
    -------
    Path or None
        The filename if a file is found; otherwise None.

    Examples
    --------
    >>>find_file_in_directory_by_stem('Cam-01_C1_PRV', '/home/vgrimaud/temp')
    Path('Cam-01_C1_PRV.png')

    """
    for filepath in Path(directory).iterdir():
        if file_stem == filepath.stem:
            return Path(filepath.name)
