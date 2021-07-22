bl_info = {
    "name": "PETRA",
    "author": "Valentin Grimaud",
    "version": (0, 2, 0),
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

import importlib

import bpy
from bpy.types import Operator, Panel


if "setup" not in locals():
    from . import setup
else:
    importlib.reload(setup)


# --------------------------------------------------
# Operators
# --------------------------------------------------


class PETRA_OT_BuildInitialSetup(Operator):

    bl_label = "Build PETRA Setup"
    bl_idname = "petra.build_petra_setup"
    bl_description = "Build the initial PETRA Setup."
    bl_context = "objectmode"
    bl_options = {"REGISTER", "INTERNAL"}

    def execute(self, context):
        setup.build()
        return {"FINISHED"}


class PETRA_OT_ProduceDocumentation(Operator):

    bl_idname = "petra.produce_documentation"
    bl_label = "PRODUCE DOCUMENTATION"
    bl_description = "Produce the PETRA Documentation."

    def execute(self, context):
        popup("Not implemented yet.")
        return {"FINISHED"}


class PETRA_OT_ExportSceneParadata(Operator):

    bl_idname = "petra.export_scene_paradata"
    bl_label = "Export Scene Paradata"
    bl_description = "Export the scene paradata YAML file."

    def execute(self, context):
        popup("Not implemented yet.")
        return {"FINISHED"}


class PETRA_OT_ExportLayoutInformation(Operator):

    bl_idname = "petra.export_layout_information"
    bl_label = "Export Layout Information"
    bl_description = "Export the layout information file."

    def execute(self, context):
        popup("Not implemented yet.")
        return {"FINISHED"}


class PETRA_OT_ActivateAndPreviewSceneCamera(Operator):

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


class PETRA_PT_InitialSetup(Panel):

    bl_label = "Initial setup"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"

    def draw(self, context):
        self.layout.operator(PETRA_OT_BuildInitialSetup.bl_idname)
        # self.layout.label(text="'Framing Box' location:")
        # self.layout.label(text="Not implemented yet.", icon="INFO")
        # self.layout.label(text="'Framing Box' rotation:")
        # self.layout.label(text="Not implemented yet.", icon="INFO")
        # self.layout.label(text="'Framing Box' dimension:")
        # self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_CameraSetup(Panel):

    bl_idname = "PETRA_PT_CameraSetup"
    bl_label = "Camera setup"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        if "PETRA" not in bpy.data.collections:
            self.layout.label(text="no PETRA collection found...", icon="INFO")
            return

        self.layout.label(text="Under development...", icon="INFO")
        self.layout.label(text="Camera manager:")

        cameras = [
            o for o in bpy.data.collections["PETRA"].objects if o.type == "CAMERA"
        ]
        cameras.sort(key=lambda o: o.name)
        chosen_camera = bpy.context.space_data.camera

        for camera in cameras:
            row = self.layout.row(align=True)
            row.context_pointer_set("active_object", camera)
            is_chosen_camera = camera == chosen_camera
            row.operator(
                "petra.activate_and_preview_scene_camera",
                text="",
                icon=f"RESTRICT_VIEW_{'OFF' if is_chosen_camera else 'ON'}",
                emboss=is_chosen_camera,
            )
            row.prop(camera, "name", text="", emboss=False)


class PETRA_PT_CameraSetupSettings(Panel):

    bl_label = "Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_parent_id = "PETRA_PT_CameraSetup"

    def draw(self, context):
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


class PETRA_PT_MaterialSetup(Panel):

    bl_idname = "PETRA_PT_MaterialSetup"
    bl_label = "Material setup"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_MaterialSetup_GeneralSettings(Panel):

    bl_label = "General Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_parent_id = "PETRA_PT_MaterialSetup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_MaterialSetup_ContourLinesSettings(Panel):

    bl_label = "Contour Lines Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_parent_id = "PETRA_PT_MaterialSetup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_MaterialSetup_DeviationMapSettings(Panel):

    bl_label = "Deviation Map Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_parent_id = "PETRA_PT_MaterialSetup"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class PETRA_PT_Rendering(Panel):

    bl_label = "Rendering"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        row = self.layout.row(align=True)
        row.scale_y = 2.5
        row.operator(PETRA_OT_ProduceDocumentation.bl_idname)
        self.layout.operator(PETRA_OT_ExportSceneParadata.bl_idname)
        self.layout.operator(PETRA_OT_ExportLayoutInformation.bl_idname)


classes = (
    PETRA_OT_ActivateAndPreviewSceneCamera,
    PETRA_OT_BuildInitialSetup,
    PETRA_OT_ExportLayoutInformation,
    PETRA_OT_ExportSceneParadata,
    PETRA_OT_ProduceDocumentation,
    PETRA_PT_InitialSetup,
    PETRA_PT_CameraSetup,
    PETRA_PT_CameraSetupSettings,
    PETRA_PT_MaterialSetup,
    PETRA_PT_MaterialSetup_GeneralSettings,
    PETRA_PT_MaterialSetup_ContourLinesSettings,
    PETRA_PT_MaterialSetup_DeviationMapSettings,
    PETRA_PT_Rendering,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


# --------------------------------------------------
# Helpers
# --------------------------------------------------


def popup(text="", title="Information", icon="INFO"):
    def draw(self, context):
        self.layout.label(text=text)

    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


if __name__ == "__main__":
    register()
