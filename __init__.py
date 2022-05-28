from subprocess import run

import bpy

bl_info = {
    "name": "OpenVSCode",
    "author": "tsutomu",
    "version": (0, 1),
    "blender": (3, 1, 0),
    "support": "TESTING",
    "category": "Object",
    "description": "",
    "location": "View3D > Object",
    "warning": "",
    "doc_url": "https://github.com/SaitoTsutomu/OpenVSCode",
}


class COC_OT_open_vscode(bpy.types.Operator):
    bl_idname = "object.open_vscode"
    bl_label = "Open VSCode"
    bl_description = "Open the file of bpy.data.texts."

    def execute(self, context):
        for text in bpy.data.texts:
            if s := text.filepath:
                run(["code", s])
        return {"FINISHED"}


def draw_item(self, context):
    self.layout.operator(COC_OT_open_vscode.bl_idname)


def register():
    bpy.utils.register_class(COC_OT_open_vscode)
    bpy.types.TEXT_MT_text.append(draw_item)


def unregister():
    bpy.utils.unregister_class(COC_OT_open_vscode)
    bpy.types.TEXT_MT_text.remove(draw_item)
