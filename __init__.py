import bpy

from .apply_constraints import OT_ApplyConstraints
from .load_openpose import LoadOpenPoseCollectionOperator
from .momask_main import OT_Main

bl_info = {
    "name": "BM4O",
    "author": "alanhzh+GPT",
    "version": (0, 1),
    "blender": (3, 6, 0),
    "location": "3DView Port > Object",
    "description": "https://ericguo5513.github.io/momask/ + Openpose fit.",
    "category": "Object"
}


class BM4O_UIPanel(bpy.types.Panel):  # Class name corrected with _PT_ prefix
    bl_label = "MomaskGenOpenPose"
    bl_idname = "BM4O_UIPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'mkop'

    def draw(self, context):
        layout = self.layout

        #Text input field
        layout.row().prop(context.scene, "my_path_input")        
        layout.row().prop(context.scene, "my_title_input")
        layout.row().prop(context.scene, "my_text_input")
        layout.row().prop(context.scene, "my_check_input")
        layout.label(text = "200fps = 10seconds")
        layout.row().prop(context.scene, "my_int_input")
        # 生成按钮
        layout.operator("my.operator")
        # layout.operator("scene.load_openpose_collection", text="Load OpenPose")

        # 检查"OpenPoseRef" Collection是否已经被加载到当前场景
        if "OpenPoseRef" not in bpy.context.scene.collection.children:
            # 如果没有找到"OpenPoseRef" Collection，显示"Load OpenPose"按钮
            layout.operator("scene.load_openpose_collection", text="Load OpenPose")
        else:
            # 如果已经找到，则不显示按钮
            # 这里你可以选择显示一个文本标签作为提示，例如：
            layout.label(text="OpenPoseRef already loaded.")
        # 约束按钮
        layout.operator("object.apply_constraints")




def register():
    bpy.utils.register_class(BM4O_UIPanel)  # Register with corrected name
    bpy.utils.register_class(LoadOpenPoseCollectionOperator)
    bpy.types.Scene.openpose_loaded = bpy.props.BoolProperty(default=False) # 添加用于检测OpenPoseRef是否已加载的自定义属性
    bpy.utils.register_class(OT_ApplyConstraints)
    bpy.types.Scene.my_path_input = bpy.props.StringProperty(name="Path", default="E:\\")    
    bpy.types.Scene.my_title_input = bpy.props.StringProperty(name="foldername", default="momaskmotion")
    bpy.types.Scene.my_text_input = bpy.props.StringProperty(name="Text", default="a person jumping.")
    bpy.types.Scene.my_check_input = bpy.props.BoolProperty(name="IK")
    bpy.types.Scene.my_int_input = bpy.props.IntProperty(name="length_fps", default=200, min=1, max=10000)
    bpy.utils.register_class(OT_Main)

def unregister():
    bpy.utils.unregister_class(BM4O_UIPanel)  # Unregister with corrected name
    bpy.utils.unregister_class(LoadOpenPoseCollectionOperator)
    del bpy.types.Scene.openpose_loaded
    bpy.utils.unregister_class(OT_ApplyConstraints)
    del bpy.types.Scene.my_path_input    
    del bpy.types.Scene.my_text_input
    del bpy.types.Scene.my_title_input
    del bpy.types.Scene.my_int_input
    del bpy.types.Scene.my_check_input
    bpy.utils.unregister_class(OT_Main)

if __name__ == "__main__":
    register()

