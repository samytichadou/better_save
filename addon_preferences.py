import bpy
import os


class BETTERSAVE_PF_addon_prefs(bpy.types.AddonPreferences) :
    bl_idname = __package__

    no_shading : bpy.props.BoolProperty(
        name = "No shading view",
        description = "Prevent save with shaded view",
        default = True,
    )
    compression : bpy.props.EnumProperty(
        name = "Compression",
        description = "Compression of the save file",
        items = [
            ("NONE", "None", "Do nothing"),
            ("COMPRESSION", "Compression", "Ensure file is compressed"),
            ("NOCOMPRESSION", "No Compression", "Ensure file is not compressed"),
        ],
        default = "NONE",
    )


    def draw(self, context) :
        layout = self.layout

        col = layout.column(align=True)
        col.label(text="Save file options :")
        col.prop(self, "no_shading")
        # col.prop(self, "compression")


# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(__package__)
    return getattr(addon, "preferences", None)


### REGISTER ---
def register():
    bpy.utils.register_class(BETTERSAVE_PF_addon_prefs)

def unregister():
    bpy.utils.unregister_class(BETTERSAVE_PF_addon_prefs)
