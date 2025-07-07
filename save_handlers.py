import bpy

from bpy.app.handlers import persistent

from .addon_preferences import get_addon_preferences

no_shading_areas_list = []


def set_no_shading():

    global no_shading_areas_list

    no_shading_areas_list.clear()

    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == "VIEW_3D":
                if area.spaces[0].shading.type in ["MATERIAL", "RENDERED"]:
                    no_shading_areas_list.append(
                        (area, area.spaces[0].shading.type)
                    )
                    area.spaces[0].shading.type = "SOLID"

def restore_no_shading():

    for area, shading_type in no_shading_areas_list:
        area.spaces[0].shading.type = shading_type


@persistent
def set_no_shading_save_handler(scene):
    prefs = get_addon_preferences()
    if not prefs.no_shading:
        return

    print("BETTERSAVE --- No shading set handler")
    set_no_shading()

@persistent
def restore_no_shading_save_handler(scene):
    prefs = get_addon_preferences()
    if not prefs.no_shading:
        return

    print("BETTERSAVE --- No shading restore handler")
    restore_no_shading()

@persistent
def set_compression_save_handler(scene):
    prefs = get_addon_preferences()
    if prefs.compression == "NONE":
        return

    print("BETTERSAVE --- Compression set handler")
    bpy.ops.wm.save_mainfile(compress=True)


### REGISTER ---
def register():
    bpy.app.handlers.save_pre.append(set_no_shading_save_handler)
    bpy.app.handlers.save_post.append(restore_no_shading_save_handler)

    # bpy.app.handlers.save_pre.append(set_compression_save_handler)

def unregister():
    bpy.app.handlers.save_pre.remove(set_no_shading_save_handler)
    bpy.app.handlers.save_post.remove(restore_no_shading_save_handler)

    # bpy.app.handlers.save_pre.remove(set_compression_save_handler)
