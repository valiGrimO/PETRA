bl_info = {
    "name": "PETRA",
    "author": "Valentin Grimaud",
    "version": (0, 4, 0),
    "blender": (3, 1, 2),
    "location": "View3D > Sidebar > New Tab",
    "description": "Protocole Employing TRee dimension models in Archaeology",
    "warning": "",
    "wiki_url": "https://github.com/valigrimo/PETrA",
    "tracker_url": "https://github.com/valigrimo/PETrA/issues",
    "category": "Render",
}

# --------------------------------------------------
# Blender UI Scripting Overview
# --------------------------------------------------
#
# Start here: https://blender.stackexchange.com/a/57332
#
# Type abbreviations:
#
#    HT – Header Type
#    MT – Menu Type
#    OT – Operator Type
#    PT – Panel Type
#    UL – UI List
#
# Class naming convention:
#
#   {CATEGORY}_{Type abbreviation}_{name}
#
# To learn from official examples, see:
#
#   https://github.com/blender/blender/tree/master/release/scripts/startup
#   https://docs.blender.org/api/current
#

import importlib
from pathlib import Path
import re

import bpy
from bpy.props import BoolProperty, FloatProperty, StringProperty
from bpy.types import Operator, Panel


PATTERN_CAMERA_NAME = re.compile(r"Cam-0([1-6])")


if "setup" not in locals():
    from . import layout_information, paradata, render_layers, setup
else:
    importlib.reload(layout_information)
    importlib.reload(paradata)
    importlib.reload(render_layers)
    importlib.reload(setup)


# --------------------------------------------------
# Properties
# --------------------------------------------------


class PetraPropertyGroup(bpy.types.PropertyGroup):

    documentation_scale: FloatProperty(
        name="Documentation scale",
        description="The scale of the printed image",
        unit="NONE",
        default=0.05,
        update=lambda self, context: bpy.ops.petra.apply_render_parameters_to_scene(),
    )
    spatial_resolution: FloatProperty(
        name="Spatial resolution",
        description="Unscaled size of 1 pixel in mm. Equivalent to 25.4 / unscaled PPI",
        # This sets the unit to 'mm'. See: https://git.io/J4cZe
        unit="CAMERA",
        subtype="DISTANCE_CAMERA",
        default=1,
        update=lambda self, context: bpy.ops.petra.apply_render_parameters_to_scene(),
    )
    layer_C1_PRT: BoolProperty(name="C1: Color (from texture)", default=True)
    layer_C1_PRV: BoolProperty(name="C1: Color (from vertex color)", default=True)
    layer_H1_Masks: BoolProperty(name="H1: Masks", default=True)
    layer_H2_OBN: BoolProperty(name="H2: Outline by normals", default=True)
    layer_L1_AmbientOcclusion: BoolProperty(name="L1: Ambient occlusion", default=True)
    layer_R1_Shading: BoolProperty(name="R1: Shading", default=True)
    layer_R2_ContourLines: BoolProperty(name="R2: Contour lines", default=True)
    layer_R3_DeviationMap: BoolProperty(name="R3: Distance map", default=True)
    layer_R4_Pointiness: BoolProperty(name="R4: Pointiness", default=True)
    layer_R5_Aspect: BoolProperty(name="R5: Aspect", default=True)
    layer_R6_Slope: BoolProperty(name="R6: Slope", default=True)


# --------------------------------------------------
# Operators
# --------------------------------------------------


class PETRA_OT_build_initial_setup(Operator):

    bl_idname = "petra.build_petra_setup"
    bl_label = "Build PETRA Setup"
    bl_description = "Build the initial PETRA Setup."
    bl_context = "objectmode"
    bl_options = {"REGISTER", "INTERNAL"}

    def execute(self, context):
        setup.build()
        return {"FINISHED"}


class PETRA_OT_apply_render_parameters_to_scene(Operator):

    bl_idname = "petra.apply_render_parameters_to_scene"
    bl_label = "Apply to scene"
    bl_description = (
        "Apply the selected camera to the X- and Y-resolution of the scene dimensions."
    )

    def execute(self, context):
        camera_params = extract_chosen_camera_parameters(context)
        camera_resolution = camera_params["px"]

        render_settings = context.scene.render
        render_settings.resolution_x = camera_resolution[0]
        render_settings.resolution_y = camera_resolution[1]

        return {"FINISHED"}


class PETRA_OT_produce_documentation(Operator):

    bl_idname = "petra.produce_documentation"
    bl_label = "PRODUCE DOCUMENTATION"
    bl_description = "Produce the PETRA Documentation."

    def execute(self, context):
        for layer in layers_iterator():
            # skip layers which aren't selected
            if not getattr(context.scene.petra, layer):
                continue
            render_layers.render(layer)

        return {"FINISHED"}


class PETRA_OT_export_scene_paradata(Operator):

    bl_idname = "petra.export_scene_paradata"
    bl_label = "Export Scene Paradata"
    bl_description = "Export the scene paradata YAML file."

    def execute(self, context):
        if not bpy.data.filepath:
            popup(text="Save Blender file first.")
            return {"FINISHED"}

        blend_filepath = Path(bpy.data.filepath)
        yaml_filename = f"{blend_filepath.stem}_paradata.yaml"
        yaml_filepath = blend_filepath.parent / yaml_filename

        paradata.generate_yaml(context, yaml_filepath)

        popup(
            title="Export successful.",
            text=f"Paradata saved to\n{yaml_filepath}",
        )

        return {"FINISHED"}


class PETRA_OT_export_layout_information(Operator):

    bl_idname = "petra.export_layout_information"
    bl_label = "Export Layout Information"
    bl_description = "Export the layout information file."

    def execute(self, context):
        blend_filepath = Path(bpy.data.filepath)
        svg_filename = f"{blend_filepath.stem}_layout_information.svg"
        svg_filepath = blend_filepath.parent / svg_filename

        layout_information.generate_svg(context, svg_filepath)

        popup(
            title="Export successful.",
            text=f"Layout information saved to\n{svg_filepath}",
        )

        return {"FINISHED"}


class PETRA_OT_activate_and_preview_scene_camera(Operator):

    bl_idname = "petra.activate_and_preview_scene_camera"
    bl_label = "Preview Camera"
    bl_description = "Activate and preview camera"

    def invoke(self, context, event):
        chosen_camera = context.active_object

        # Adjust current timeline marker
        for marker in context.scene.timeline_markers:
            if marker.camera == chosen_camera:
                context.scene.frame_current = marker.frame

        # Adjust the 3D-view perspective (other options: "PERSP", "ORTHO")
        context.area.spaces[0].region_3d.view_perspective = "CAMERA"

        # Apply the selected camera to the X- and Y-resolution of the scene dimensions.
        context.space_data.camera = chosen_camera  # needed to ensure call below works
        bpy.ops.petra.apply_render_parameters_to_scene()

        return {"FINISHED"}


class PETRA_OT_preview_layer(Operator):

    bl_idname = "petra.preview_layer"
    bl_label = "Preview Layer"
    bl_description = "Show what rendered layer looks like without creating a file"

    active_layer: StringProperty()

    def invoke(self, context, event):
        render_layers.preview(self.active_layer)

        return {"FINISHED"}


# --------------------------------------------------
# Panels
# --------------------------------------------------


class PetraPanelMixin:

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"


class PETRA_PT_initial_setup(PetraPanelMixin, Panel):

    bl_label = "Initial setup"

    def draw(self, context):
        """Draw UI elements into the panel UI layout."""
        layout = self.layout

        layout.operator(PETRA_OT_build_initial_setup.bl_idname)

        if "PETRA" not in bpy.data.collections:
            return

        framing_box = bpy.data.collections["PETRA"].objects["Framing Box"]
        lock_kwds = dict(text="", emboss=False, icon="DECORATE_UNLOCKED")

        # location
        col = layout.column(align=True)
        col.label(text="'Framing Box' location:")
        split = col.split(factor=0.8)
        split.prop(framing_box, "location", text="")
        split.prop(framing_box, "lock_location", **lock_kwds)

        # rotation
        col = layout.column(align=True)
        col.label(text="'Framing Box' rotation:")
        split = col.split(factor=0.8)
        split.prop(framing_box, "rotation_euler", text="")
        split.prop(framing_box, "lock_rotation", **lock_kwds)

        # dimensions
        layout.column().prop(framing_box, "dimensions", text="'Framing Box' dimensions")


class PETRA_PT_camera_setup(PetraPanelMixin, Panel):

    bl_label = "Camera setup"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        """If this method returns a non-null output, then the panel can be drawn."""
        return bpy.data.collections.get("PETRA")

    def draw(self, context):
        objects = bpy.data.collections["PETRA"].objects
        cameras = [o for o in objects if o.type == "CAMERA"]
        cameras.sort(key=lambda o: o.name)
        chosen_camera = bpy.context.space_data.camera

        layout = self.layout

        col = layout.column(align=True)
        col.label(text="Printed documentation:")
        col.prop(context.scene.petra, "documentation_scale", text="Scale")
        col.prop(context.scene.petra, "spatial_resolution", text="Spatial resolution")
        # col.operator(PETRA_OT_apply_render_parameters_to_scene.bl_idname)
        ppi = paradata.BlenderData(context).resolution_of_image
        col.label(text=f"Resolution: {ppi} ppi", icon="INFO")
        printed_size = extract_chosen_camera_dimensions(context)
        col.label(text=f"Printed size: {printed_size}", icon="INFO")

        layout.label(text="Camera manager:")
        for camera in cameras:
            if not is_valid_framing_box_camera(camera):
                continue
            row = layout.row(align=True)
            row.context_pointer_set("active_object", camera)
            is_chosen_camera = camera == chosen_camera
            row.operator(
                "petra.activate_and_preview_scene_camera",
                text="",
                icon=f"RESTRICT_VIEW_{'OFF' if is_chosen_camera else 'ON'}",
                emboss=is_chosen_camera,
            )
            row.prop(camera, "name", text="", emboss=True)


class PETRA_PT_camera_setup_settings(PetraPanelMixin, Panel):

    bl_label = "Settings"
    bl_parent_id = "PETRA_PT_camera_setup"

    def draw(self, context):
        if "PETRA" not in bpy.data.collections:
            return

        self.layout.label(text="Dimensions:")

        row = self.layout.row(align=True)
        render_settings = context.scene.render
        row.prop(render_settings, "resolution_x", text="H")
        row.prop(render_settings, "resolution_y", text="V")
        row.enabled = False
        self.layout.prop(render_settings, "resolution_percentage", text="")
        self.layout.prop(
            render_settings, "use_border", text="Render Region", icon="SHADING_BBOX"
        )

        selected_camera = bpy.context.scene.camera.data
        if not isinstance(selected_camera, bpy.types.Camera):
            return

        row = self.layout.row(align=True)
        row.prop(selected_camera, "shift_x", text="Shift H")
        row.prop(selected_camera, "shift_y", text="Shift V")

        row = self.layout.row(align=True)
        row.prop(selected_camera, "clip_start", text="Clip Start")
        row.prop(selected_camera, "clip_end", text="Clip End")


class PETRA_PT_material_setup(PetraPanelMixin, Panel):

    bl_label = "Layer of information setup"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        """If this method returns a non-null output, then the panel can be drawn."""
        return bpy.data.collections.get("PETRA")

    def draw(self, context):
        self.layout.label(text="List of layers:")
        for layer in layers_iterator():
            row = self.layout.row(align=True)
            operator = row.operator(
                "petra.preview_layer",
                text="",
                icon="RESTRICT_VIEW_ON",
            )
            operator.active_layer = layer
            row.prop(context.scene.petra, layer)


class PETRA_PT_rendering(PetraPanelMixin, Panel):

    bl_label = "Rendering"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        """If this method returns a non-null output, then the panel can be drawn."""
        return bpy.data.collections.get("PETRA")

    def draw(self, context):
        row = self.layout.row(align=True)
        row.scale_y = 2.5
        row.operator(PETRA_OT_produce_documentation.bl_idname)
        self.layout.operator(PETRA_OT_export_scene_paradata.bl_idname)
        self.layout.operator(PETRA_OT_export_layout_information.bl_idname)


classes = (
    PetraPropertyGroup,
    PETRA_OT_activate_and_preview_scene_camera,
    PETRA_OT_apply_render_parameters_to_scene,
    PETRA_OT_build_initial_setup,
    PETRA_OT_export_layout_information,
    PETRA_OT_export_scene_paradata,
    PETRA_OT_preview_layer,
    PETRA_OT_produce_documentation,
    PETRA_PT_initial_setup,
    PETRA_PT_camera_setup,
    PETRA_PT_camera_setup_settings,
    PETRA_PT_material_setup,
    PETRA_PT_rendering,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.petra = bpy.props.PointerProperty(type=PetraPropertyGroup)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.petra


# --------------------------------------------------
# Helpers
# --------------------------------------------------


def popup(text="", title="Information", icon="INFO"):
    def draw(self, context):
        lines = text.split("\n")
        for line in lines:
            self.layout.label(text=line)

    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


def extract_chosen_camera_parameters(context):
    chosen_camera = context.space_data.camera

    camera_params = layout_information.make_camera_parameters(bpy.context)
    camera_number = PATTERN_CAMERA_NAME.match(chosen_camera.name)[1]
    camera_index = int(camera_number) - 1

    return camera_params[camera_index]


def is_valid_framing_box_camera(camera):
    return bool(PATTERN_CAMERA_NAME.match(camera.name) and camera.data.animation_data)


def extract_chosen_camera_dimensions(context):
    """
    Returns dimensions of chosen camera in cm as string.

    Example
    -------
    >>> extract_chosen_camera_dimensions(bpy.context)
    '10.0 cm x 10.0 cm'
    """
    camera_params = extract_chosen_camera_parameters(context)

    # convert width and height from mm to cm
    width = round(camera_params["width"] / 10, 1)
    height = round(camera_params["height"] / 10, 1)

    return f"{width} cm x {height} cm"


def layers_iterator():
    # layer_name = layer_property.keywords["name"]
    for identifier in PetraPropertyGroup.__annotations__.keys():
        if not identifier.startswith("layer_"):
            continue
        yield identifier


if __name__ == "__main__":
    register()
