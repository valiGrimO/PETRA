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


import importlib

import bpy


if "setup" not in locals():
    from . import setup
else:
    importlib.reload(setup)

# --------------------------------------------------
# Operators
# --------------------------------------------------


class BuildInitialSetupOperator(bpy.types.Operator):

    bl_label = "Build PETRA Setup"
    bl_idname = "petra.build_petra_setup"
    bl_description = "Build the initial PETRA Setup."
    bl_context = "objectmode"
    bl_options = {"REGISTER", "INTERNAL"}

    def execute(self, context):
        setup.build()
        return {"FINISHED"}


# --------------------------------------------------
# Panels
# --------------------------------------------------


class VIEW3D_PT_Petra_Initial_Setup(bpy.types.Panel):

    bl_label = "Initial setup"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"

    def draw(self, context):
        self.layout.operator(BuildInitialSetupOperator.bl_idname)
        self.layout.label(text="'Framing Box' location:")
        self.layout.label(text="Not implemented yet.", icon="INFO")
        self.layout.label(text="'Framing Box' rotation:")
        self.layout.label(text="Not implemented yet.", icon="INFO")
        self.layout.label(text="'Framing Box' dimension:")
        self.layout.label(text="Not implemented yet.", icon="INFO")


class VIEW3D_PT_Petra_Camera_Setup(bpy.types.Panel):

    bl_label = "Camera setup"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class VIEW3D_PT_Petra_Material_Setup(bpy.types.Panel):

    bl_label = "Material setup"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


class VIEW3D_PT_Petra_Rendering(bpy.types.Panel):

    bl_label = "Rendering"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PETRA"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        self.layout.label(text="Not implemented yet.", icon="INFO")


classes = (
    BuildInitialSetupOperator,
    VIEW3D_PT_Petra_Initial_Setup,
    VIEW3D_PT_Petra_Camera_Setup,
    VIEW3D_PT_Petra_Material_Setup,
    VIEW3D_PT_Petra_Rendering,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


# --------------------------------------------------
# Things to execute
# --------------------------------------------------


if __name__ == "__main__":
    register()
