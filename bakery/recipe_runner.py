import bpy
import logging
import json
import sys

from bakery.operator_executor import OperatorExecutor
from bakery.recipes.setup_wizard_recipe import SetupWizardRecipe

from setup_wizard.tests.logger import Logger


argv = sys.argv
argv = argv[argv.index('--') + 1:]
print(f'argv: {argv}')

# source_folder = argv[0]
# destination_folder = argv[1]
recipe = json.loads(argv[0])
timestamp = recipe.get('timestamp')

Logger(f'bakery\\logs\\{timestamp}.log')
logger = logging.getLogger(__name__)


operators = SetupWizardRecipe(recipe, **recipe).generate_recipe()
character_name = recipe.get('character_name')

cube = bpy.context.scene.objects.get('Cube')
if cube:
    logger.info('Deleting Cube')
    bpy.data.objects.remove(cube)
    logger.info('Deleted Cube')

logger.info(f'Starting recipe for {character_name}')

for operator in operators:
    try:
        # operator_executor = OperatorExecutor(**operator)
        # operator_executor.execute()
        operator.execute()
    except Exception as ex:
        logger.error(ex)
        logger.error(f'Failed recipe for {character_name}')
        bpy.ops.wm.quit_blender()

logger.info(f'Completed recipe for {character_name}')

filename = f'{character_name}.blend'
logger.info(f'Saving file for {character_name} as: {filename}')
bpy.ops.wm.save_as_mainfile(filepath=f'{recipe.get("destination_folder")}/{filename}')
logger.info(f'Saved file for {character_name} as: {filename}')

bpy.ops.wm.quit_blender()