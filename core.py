import webbrowser

import bpy

from .register_class import _get_cls


class COU_OT_open_url(bpy.types.Operator):
    bl_idname = "object.open_url"
    bl_label = "Open URL"
    bl_description = "Open the URL of a text object."

    def execute(self, context):
        obj = context.view_layer.objects.active
        if obj and obj.type == "FONT" and obj.data.body.startswith("http"):
            webbrowser.open(obj.data.body)
        return {"FINISHED"}


class COU_OT_add_url(bpy.types.Operator):
    bl_idname = "object.add_url"
    bl_label = "Add URL"
    bl_description = "Add the a text object of URL."

    def execute(self, context):
        s = bpy.context.window_manager.clipboard
        if not (isinstance(s, str) and s.startswith("http")):
            self.report({"WARNING"}, "Copy URL")
            return {"CANCELLED"}
        bpy.ops.object.text_add(radius=0.1)
        text = bpy.context.object
        text.data.body = s
        text.name = "URL"
        text.hide_render = True
        return {"FINISHED"}


# 自動的にこのモジュールのクラスを設定
ui_classes = _get_cls(__name__)


def draw_item(self, context):
    """メニューの登録と削除用"""
    for ui_class in ui_classes:
        self.layout.operator(ui_class.bl_idname)


def register():
    """追加登録用（クラス登録は、register_class内で実行）"""
    bpy.types.VIEW3D_MT_object.append(draw_item)


def unregister():
    """追加削除用（クラス削除は、register_class内で実行）"""
    bpy.types.VIEW3D_MT_object.remove(draw_item)
