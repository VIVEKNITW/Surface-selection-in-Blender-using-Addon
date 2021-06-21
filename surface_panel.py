import bpy

class Surface_PT_selection(bpy.types.Panel):
    """ """
    bl_label = "Select surface"
    bl_idname = "Surface_PT_selection"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "CranialPlate"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.surfaceselection")
        row = layout.row()
        row.operator("object.surfaceadd")
        row.operator("object.surfaceremove")
        row = layout.row()
        row.operator("object.clearsurface")
        row = layout.row()
        row.operator("object.surfaceseparation")
        row = layout.row()
        row.operator("object.exit")
        
