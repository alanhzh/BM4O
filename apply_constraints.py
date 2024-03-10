import bpy

class OT_ApplyConstraints(bpy.types.Operator):
    bl_idname = "object.apply_constraints"
    bl_label = "BVH > OpenPose"

    def execute(self, context):
        armature = context.active_object  # 使用当前选中的骨架对象
        # armature = bpy.context.selected_objects[0]
        objects_to_bones = {
            "Head": ("Head", None),  # Empty对象"Head"对应骨骼"Head"
            "1": ("Spine2", 0.87),   # 1号物体对应骨骼"Spine2"，Head/Tail值为0.87
            "2": ("RightArm", None),  # 以下物体对应的骨骼名称
            "3": ("RightForeArm", None),
            "4": ("RightHand", None),
            "5": ("LeftArm", None),
            "6": ("LeftForeArm", None),
            "7": ("LeftHand", None),
            "8": ("RightUpLeg", None),
            "9": ("RightLeg", None),
            "10": ("RightFoot", None),
            "11": ("LeftUpLeg", None),
            "12": ("LeftLeg", None),
            "13": ("LeftFoot", None),
        }

        for obj_name, (bone_name, head_tail) in objects_to_bones.items():
            if obj_name in bpy.data.objects:
                obj = bpy.data.objects[obj_name]
                obj.constraints.clear()
    
                constraint = obj.constraints.new(type='COPY_TRANSFORMS')
                constraint.target = armature
                constraint.subtarget = bone_name

                if obj_name == "1" and head_tail is not None:
                    bpy.context.view_layer.objects.active = obj  # 选中1号物体
                    constraint.head_tail = head_tail

        return {'FINISHED'}