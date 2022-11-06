from bpy.types import Panel 

class B_PT_Bakery_UI_Layout(Panel):
    bl_label = "Bakery (Batch Job Runner)"
    bl_idname = "B_PT_Bakery_UI_Layout"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Batch Runner"

    def draw(self, context):
        layout = self.layout
        column = layout.column()

        column.operator(
            operator='',
            text='Run Batch Job Runner',
            icon='PLAY'
        )

