# Author: michael-gh1
# Originally contributed by Zekium and Modder4869 from Discord

import bpy

# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty
from bpy.types import Operator

from setup_wizard.models import CustomOperatorProperties
from setup_wizard.texture_import_setup.game_texture_importers import GameTextureImporter, GameTextureImporterFactory
from setup_wizard.texture_import_setup.texture_importer_service import TextureImporterService


class GI_OT_GenshinImportTextures(Operator, ImportHelper, CustomOperatorProperties):
    """Select the folder with the model's textures to import"""
    bl_idname = "genshin.import_textures"  # important since its how we chain file dialogs
    bl_label = "Genshin: Import Textures - Select Character Model Folder"

    # ImportHelper mixin class uses this
    filename_ext = "*.*"
    
    import_path: StringProperty(
        name = "Path",
        description = "Path to the folder containing the files to import",
        default = "",
        subtype = 'DIR_PATH'
        )

    filter_glob: StringProperty(
        default="*.*",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        game_texture_importer: GameTextureImporter = \
            GameTextureImporterFactory.create(self.game_type, self, context)

        texture_importer_service = TextureImporterService(game_texture_importer)
        status = texture_importer_service.import_textures()

        super().clear_custom_properties()
        return status or {'FINISHED'}


register, unregister = bpy.utils.register_classes_factory(GI_OT_GenshinImportTextures)
