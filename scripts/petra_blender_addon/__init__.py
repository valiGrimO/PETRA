bl_info = {
    "name": "PETRA",
    "author": "Valentin Grimaud",
    "version": (0, 2, 2),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > New Tab",
    "description": "Protocole d'Exploitation des représentations TRidimensionnelles en Archéologie.",
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

import bpy
from bpy.types import Operator, Panel


if "setup" not in locals():
    from . import layout_information, paradata, setup
else:
    # hffssafsaffasfaasfassaf
    importlib.reload(layout_information)
    importlib.reload(paradata)
    importlib.reload(setup)


# --------------------------------------------------
# Properties
# --------------------------------------------------
class PetraPropertyGroup(bpy.types.PropertyGroup):
    documentation_scale: bpy.props.FloatProperty(
        name="Documentation scale", unit="NONE", default=0.05
    )
    spatial_resolution: bpy.props.FloatProperty(
        name="Spatial resolution", unit="LENGTH", default=0.0005
    )


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


class PETRA_OT_produce_documentation(Operator):

    bl_idname = "petra.produce_documentation"
    bl_label = "PRODUCE DOCUMENTATION"
    bl_description = "Produce the PETRA Documentation."

    def execute(self, context):
        popup("Not implemented yet.")
        return {"FINISHED"}


class PETRA_OT_export_scene_paradata(Operator):

    bl_idname = "petra.export_scene_paradata"
    bl_label = "Export Scene Paradata"
    bl_description = "Export the scene paradata YAML file."

    def execute(self, context):
        if not bpy.data.filepath:
            popup(text=f"Save Blender file first.")
            return {"FINISHED"}

        blend_filepath = Path(bpy.data.filepath)
        yaml_filename = f"{blend_filepath.stem}_paradata.yaml"
        yaml_filepath = blend_filepath.parent / yaml_filename

        print(blend_filepath, yaml_filename, yaml_filepath)
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
    bl_description = "Activate and preview camera."

    def invoke(self, context, event):

        # Adjust timeline markers
        for marker in context.scene.timeline_markers:
            if marker.camera == context.active_object:
                context.scene.frame_current = marker.frame

        # Adjust the 3D-view perspective (other options: "PERSP", "ORTHO")
        context.area.spaces[0].region_3d.view_perspective = "CAMERA"

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
        self.layout.operator(PETRA_OT_build_initial_setup.bl_idname)
        # self.layout.label(text="'Framing Box' location:")
        # self.layout.label(text="Not implemented yet.", icon="INFO")
        # self.layout.label(text="'Framing Box' rotation:")
        # self.layout.label(text="Not implemented yet.", icon="INFO")
        # self.layout.label(text="'Framing Box' dimension:")
        # self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_camera_setup(PetraPanelMixin, Panel):

    bl_label = "Camera setup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        if "PETRA" not in bpy.data.collections:
            self.layout.label(text="no PETRA collection found...", icon="INFO")
            return

        objects = bpy.data.collections["PETRA"].objects
        cameras = [o for o in objects if o.type == "CAMERA"]
        cameras.sort(key=lambda o: o.name)
        chosen_camera = bpy.context.space_data.camera

        layout = self.layout

        layout.label(text="Under development...", icon="INFO")
        layout.label(text="Documentation parameter:")
        layout.prop(context.scene.petra, "documentation_scale")
        layout.prop(context.scene.petra, "spatial_resolution")

        layout.label(text="Camera manager:")
        for camera in cameras:
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

        self.layout.label(text="Dimensions")

        row = self.layout.row(align=True)
        render_settings = context.scene.render
        row.prop(render_settings, "resolution_x", text="H")
        row.prop(render_settings, "resolution_y", text="V")
        self.layout.prop(render_settings, "resolution_percentage", text="")
        self.layout.prop(
            render_settings, "use_border", text="Render Region", icon="SHADING_BBOX"
        )

        selected_object = bpy.context.object.data
        if not isinstance(selected_object, bpy.types.Camera):
            return
        selected_camera = selected_object

        row = self.layout.row(align=True)
        row.prop(selected_camera, "shift_x", text="Shift H")
        row.prop(selected_camera, "shift_y", text="Shift V")

        row = self.layout.row(align=True)
        row.prop(selected_camera, "clip_start", text="Clip Start")
        row.prop(selected_camera, "clip_end", text="Clip End")


class PETRA_PT_material_setup(PetraPanelMixin, Panel):

    bl_label = "Material setup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_material_setup_general_settings(PetraPanelMixin, Panel):

    bl_label = "General Settings"
    bl_parent_id = "PETRA_PT_material_setup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_material_setup_contour_lines_settings(PetraPanelMixin, Panel):

    bl_label = "Contour Lines Settings"
    bl_parent_id = "PETRA_PT_material_setup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_material_setup_deviation_map_settings(PetraPanelMixin, Panel):

    bl_label = "Deviation Map Settings"
    bl_parent_id = "PETRA_PT_material_setup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_rendering(PetraPanelMixin, Panel):

    bl_label = "Rendering"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        row = self.layout.row(align=True)
        row.scale_y = 2.5
        row.operator(PETRA_OT_produce_documentation.bl_idname)
        self.layout.operator(PETRA_OT_export_scene_paradata.bl_idname)
        self.layout.operator(PETRA_OT_export_layout_information.bl_idname)


classes = (
    PetraPropertyGroup,
    PETRA_OT_activate_and_preview_scene_camera,
    PETRA_OT_build_initial_setup,
    PETRA_OT_export_layout_information,
    PETRA_OT_export_scene_paradata,
    PETRA_OT_produce_documentation,
    PETRA_PT_initial_setup,
    PETRA_PT_camera_setup,
    PETRA_PT_camera_setup_settings,
    PETRA_PT_material_setup,
    PETRA_PT_material_setup_general_settings,
    PETRA_PT_material_setup_contour_lines_settings,
    PETRA_PT_material_setup_deviation_map_settings,
    PETRA_PT_rendering,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Set default length unit to mm.
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


if __name__ == "__main__":
    register()
