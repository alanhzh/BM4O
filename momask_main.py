import bpy
import requests
import json
import os

class OT_Main(bpy.types.Operator):  # No change needed here
    bl_idname = "my.operator"
    bl_label = "Generate"

    def execute(self, context):
        d_text = context.scene.my_text_input
        d_sec = str(context.scene.my_int_input)
        d_title = context.scene.my_title_input
        d_path = context.scene.my_path_input
        d_check = context.scene.my_check_input
        
        if not d_title:
            d_title = "momaskmotion"
            print("Since the folder name was not entered, I created a folder using 'momaskmotion'.")
        if not d_text:
            d_text = "a person jumping."
            print("There was no text input, so I entered 'a person jumping.'")
        
        data = {
            "text": d_text,
            "sec": d_sec,
            "title": d_title,
            "dir": d_path,
        }
        if os.path.isdir(d_path):
            if not d_path[-1] == "\\":
                 d_path = d_path+"\\"
            response = requests.post(
                "http://localhost:8000/gent2m/",
                data=json.dumps(data),
                headers={'Content-type': 'application/json'})
            print(d_path+d_title+"\\animations\\0\\")
            dir_path = d_path+d_title+"\\animations\\0\\"
            # Stores files with the .bvh extension in a list.
            bvh_files = [os.path.join(dir_path, file) for file in os.listdir(dir_path) if file.endswith('.bvh')]
            for file in bvh_files:
                if "_ik" in file:
                    ik_bvh = file
                else:
                    fk_bvh = file
            if d_check:
                bpy.ops.import_anim.bvh(filepath=ik_bvh)
            else:
                bpy.ops.import_anim.bvh(filepath=fk_bvh)

        else:
            print("Directory does not exist Please enter path")
        return {'FINISHED'}