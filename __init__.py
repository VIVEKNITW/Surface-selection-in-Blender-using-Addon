# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Surface selection",
    "author" : "Vivekanand Shanbhag",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .surface_panel import Surface_PT_selection
from .surface_operator import Surface_OT_selection, Surface_OT_extraction, Surface_OT_add, Surface_OT_remove, Surface_OT_clear, Surface_OT_exit

classes = (Surface_PT_selection, Surface_OT_selection, Surface_OT_extraction, Surface_OT_add, Surface_OT_remove, Surface_OT_clear, Surface_OT_exit)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=CranialMyProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()