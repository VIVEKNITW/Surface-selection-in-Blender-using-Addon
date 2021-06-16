import bpy

def check_vertex_grp():
    obj = bpy.context.object
    for name in obj.vertex_groups.keys():
        obj.vertex_groups.remove(obj.vertex_groups.get(name))