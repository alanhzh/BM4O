import bpy
import os

class LoadOpenPoseCollectionOperator(bpy.types.Operator):
    bl_idname = "scene.load_openpose_collection"
    bl_label = "Load OpenPose"

    def execute(self, context):
        # 指定.blend文件的路径（相对于插件目录）
        blend_path = os.path.join(os.path.dirname(__file__), "OpenPoseRef.blend")
        
        # 构建文件内部路径
        collection_path = "\\Collection\\"
        collection_name = "OpenPoseRef"
        
        # 加载Collection
        with bpy.data.libraries.load(blend_path, link=False) as (data_from, data_to):
            data_to.collections = [name for name in data_from.collections if name == collection_name]
        
        # 将Collection添加到当前场景
        for collection in data_to.collections:
            if collection is not None:
                bpy.context.scene.collection.children.link(collection)

        # 修改3D视图的显示设置
        self.update_3d_view_display(context)

        return {'FINISHED'}
    
    def update_3d_view_display(self, context):
        for area in context.screen.areas:  # 遍历当前窗口的所有区域
            if area.type == 'VIEW_3D':  # 找到3D视图区域
                for space in area.spaces:  # 遍历找到的3D视图区域中的所有空间
                    if space.type == 'VIEW_3D':  # 确认这是一个3D视图空间
                        space.shading.type = 'MATERIAL'  # 设置着色类型为“材质”
                        space.overlay.show_relationship_lines = False  # 隐藏关系线
                break  # 假设我们只处理找到的第一个3D视图区域