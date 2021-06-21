import bpy
from .surface_helper_functions import check_vertex_grp

class Surface_OT_selection(bpy.types.Operator):
    """ """
    bl_label = "Select surface"
    bl_idname = "object.surfaceselection"
    
    def execute(self, context):
        bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
        bpy.data.brushes["Draw"].curve_preset = 'CONSTANT'

        return {'FINISHED'}


class Surface_OT_remove(bpy.types.Operator):
    """ """
    bl_label = "Remove"
    bl_idname = "object.surfaceremove"
    
    def execute(self, context):
        bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
        bpy.data.brushes["Draw"].blend = 'MIX'
        bpy.context.scene.tool_settings.unified_paint_settings.weight = 0

        return {'FINISHED'}


class Surface_OT_add(bpy.types.Operator):
    """ """
    bl_label = "Add"
    bl_idname = "object.surfaceadd"
    
    def execute(self, context):
        bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
        bpy.data.brushes["Draw"].blend = 'MIX'
        bpy.context.scene.tool_settings.unified_paint_settings.weight = 1

        return {'FINISHED'}


class Surface_OT_clear(bpy.types.Operator):
    """ """
    bl_label = "clear selection"
    bl_idname = "object.clearsurface"
    
    def execute(self, context):
        check_vertex_grp()
        bpy.ops.object.vertex_group_add()

        return {'FINISHED'}



class Surface_OT_extraction(bpy.types.Operator):
    """ """
    bl_label = "Separate selection"
    bl_idname = "object.surfaceseparation"
    
    def execute(self, context):

        bpy.ops.object.vertex_group_invert()
        bpy.ops.object.vertex_group_invert()

        obj = bpy.context.object

        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action='DESELECT')
        
        bpy.ops.object.vertex_group_set_active(group = 'Group')
        bpy.ops.object.vertex_group_select()

        bpy.ops.mesh.duplicate_move()
        bpy.ops.mesh.separate(type = "SELECTED")
        bpy.ops.object.mode_set(mode="OBJECT")

        return {'FINISHED'}


class Surface_OT_exit(bpy.types.Operator):
    """ """
    bl_label = "Exit"
    bl_idname = "object.exit"
    
    def execute(self, context):
        bpy.ops.object.mode_set(mode="OBJECT")
        
        return {'FINISHED'}

