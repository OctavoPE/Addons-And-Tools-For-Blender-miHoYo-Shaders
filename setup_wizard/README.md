# [Blender] Character Setup Wizard Addon for  HoYoverse Shaders

> You should view this on Github or some other Markdown reader if you aren't!

The goal of this tool is to streamline the character setup process. Whether it's importing the materials, importing the character model, setting up the outlines (geometry nodes) or configuring the outline colors to be game accurate, this tool has got it all! Your one-stop-shop for setting up your characters in Blender!

**Important**: This tool is intended to be used with:
* Festivity's Genshin Impact Shader, found here: https://github.com/festivize/Blender-miHoYo-Shaders
* Festivity's Honkai: Star Rail Shader, found here: https://github.com/festivities/Blender-StellarToon
* Nya222's Honkai: Star Rail Shader, found here: https://discord.com/channels/894925535870865498/1127604826885328926 (Omatsuri Discord Server)
* JaredNyts' Punishing: Gray Raven Shader, found here: https://discord.com/channels/894925535870865498/1186597049198727259 (Omatsuri Discord Server)

**Compatibility**: This tool has been tested on **Blender (and Goo Blender) Version >= 3.3.0** and attempts to support older versions of Blender, but working functionality is not guaranteed.

:star: If this Addon is useful, please be sure to **Star** the repository! :star:

## Table of Contents
1. [Tutorials/Screenshots](#tutorialsscreenshots)
2. [Quick Start Guide](#quick-start-guide)
3. [How to Disable Components](#how-to-disable-components-on-the-ui)
4. [Features/Components](#featurescomponents)
5. [Steps (Detailed Guide)](#steps-detailed-guide)
6. [Development Roadmap/Future Features](#development-roadmap--future-features)
7. ["Tested" Character Models](#tested-character-models)
8. [Credits](#credits)

## Tutorials/Screenshots
### Screenshot of the Tool

![alt text](/assets/genshin_tab.png)
![alt text](/assets/star_rail_tab.png)
![alt text](/assets/pgr_tab.png)

### Tutorials

A few kind souls have created some video tutorials (for educational purposes, not officially endorsed)
* (Micchi — Genshin Impact-focused) https://youtu.be/S7mFQveRNcc
* (fnoji — Honkia Star Rail-focused) https://www.youtube.com/watch?v=QY37vbfrLh4



## Quick Start Guide
1. Go to the Releases page and download the latest `Setup_Wizard_UI_Addon.zip`
2. Open Blender (new file or one with no models)
3. Install the Setup Wizard
    * Edit > Preferences > Install > Select `Setup_Wizard_UI_Addon.zip`
4. Open up the N-Panel (Hit the 'N' key)
5. Select the `Genshin Impact` tab or `Honkai Star Rail` tab`
6. Click the `Run Entire Setup` button
    * Outlines are supported for Blender Version >= 3.3 (you can either disable the outline-related components or use the Basic Setup instead)
7. Select the folder with the character model and textures (lightmaps, diffuses, etc.)
8. Select the blend file containing the Shaders
    * **This only needs to be done the first time you run this tool.** This is because the filepath gets cached for future usage (click the clear cache button if you want to reset this value).
    * Examples
        * `miHoYo - Genshin Impact.blend`
        * `miHoYo - Genshin Impact - Goo Engine.blend`
        * `HSR_Shader_1.055.blend`
9. Select the `miHoYo - Outlines.blend` file with Festivity's Outlines Shaders
    * **This only needs to be done the first time you run this tool.** This is because the filepath gets cached for future usage (click the clear cache button if you want to reset this value).
    * Examples
        * `Blender-miHoYo-Shaders/miHoYo - Outlines.blend`
        * `HSR_Shader_1.055.blend`
10. Select the material data JSON files for the outlines
    * Shift+Click or Ctrl+Click the JSON files that you want to use (normally all of them)

## How to Disable Components on the UI
This tool is broken up into many different components. The `config_ui.json` file can be used to enable or disable specific steps when running the `Run Entire Setup` or `Basic Setup`.

Note: Outlines Setup is automatically disabled when running Blender Versions < v3.3.0

Example of Disabling Outlines from `Run Entire Setup`:
```
        "GENSHIN_OT_setup_wizard_ui": [
            "IMPORTANT_PLACEHOLDER_VALUE_KEEP_INDEX_ABOVE_0_setup_wizard_ui",
            "import_character_model", 
            "delete_empties",
            "import_materials",
            "replace_default_materials",
            "import_character_textures",
            "fix_transformations",
            "setup_head_driver",
            "set_color_management_to_standard",
            "delete_specific_objects"
        ],
```

In the example above, these were removed from the original `config_ui.json`:
```
            "import_outlines",
            "setup_geometry_nodes",
            "import_outline_lightmaps",
            "import_material_data",
```

You can disable any step (component) in the Setup Wizard UI by removing the step from the list in `config_ui.json`.

<br>

You can disable the cache for any step by unchecking the `Cache Enabled` checkbox.
* The cache (`cache.json.tmp`) is used to "save" your previous choice for future usage that uses the same folder/file
    * Character Model Filepath
        * Saves the character model folder file path selected
        * You may want to disable the cache if you are importing textures that are different from the character model (not the usual workflow)
        * Used when importing textures and outline lightmaps
    * Shader Blend File Path
        * Saves the file path to the selected shader blend file
        * Used when importing materials from:
            * `miHoYo - Genshin Impact.blend`
            * `miHoYo - Genshin Impact - Goo Engine.blend`
            * `HSR_Shader_#.##.blend`
    * Shader Outlines File Path
        * Saves the file path to the Outlines blend file
        * Used when importing outlines from:
            * `miHoYo - Outlines.blend`
            * `HSR_Shader_#.##.blend`


### Other Notes:
* The `component_name` or names in the `config.json` or `config_ui.json` should NOT be renamed. This is how the Setup Wizard identifies and triggers the next step/component.
* Metadata found in `config.json` is simply there to help provide human readable information and what each component requires (what should be selected on the file explorer window). (`config.json` is used by the Legacy Setup Wizard which is run through the F3 search)

## Features/Components

> Note: Ideally these steps won't change too much between releases! If they do, I will make note of it in the release notes.

1. Import Character Model
2. Delete Empties
3. Import Materials (Select Shader's `.blend` file)
4. Replace/Re-Assign Default Character Model Materials (and rename)
5. Import Character Textures
6. Import Outlines (Select Shader's Outlines `.blend` file)
7. Setup Outlines (Geometry Nodes)
8. Import Lightmaps for Outlines
9. Import Material Data
10. ~~Fix Mouth Outlines~~ - (Legacy, may return in future releases) **[Disabled by Default]** 
11. Fix Transformations on the Character
12. Setup Head Driver
13. Set Color Management to 'Standard'
14. Delete EffectMesh
15. Set Up ArmTwist Bone Constraints


## Steps (Detailed Guide)
<details>
    <summary>Expand</summary>
    <br>

> Note: Ideally these steps won't change too much between releases! If they do, I will make note of it in the release notes.

> Note: These instructions have been written for Festivity's Genshin Impact shader, but other shaders, such as Nya222's HSR Shader, have a similar setup!

1. Import Character Model
    * This step will: 
        * Import the character model which should be a .fbx file
        * Hide EffectMesh (gets deleted in a later step) and EyeStar
        * Add 'UV1' UV Map to ALL meshes (I think the important one is just Body though?)
        * Resets the location and rotation bones in pose mode and sets the armature into an A-pose (this is is done because we import with `force_connect_children`)
        * Connects the Normal Map if the texture exists for the character model
    * Select the folder that contains the character model and textures. **It is assumed that the textures for the character are also in this folder.**
2. Delete Empties
    * This step deletes Empty type objects in the scene
    * No selection needed.
3. Import Materials
    * This step imports `miHoYo - Genshin Hair`, `miHoYo - Genshin Face`, `miHoYo - Genshin Body` and `miHoYo - Genshin Outlines`.
    * **This step uses the cache (if enabled)** so you do not need to re-select the `miHoYo - Genshin Impact.blend` after selecting it on first use.
    * Select the blend file containing Festivity's Shaders `miHoYo - Genshin Impact.blend` or `miHoYo - Genshin Impact - Goo Engine.blend`.
4. Replace Default Character Model Materials (and rename)
    * This step replaces/re-assigns the default character model materials to the shader's materials.
    * Naming Convention of Genshin Materials (and their Shader nodes): `miHoYo - Genshin {Body Part}` 
        * `{Body Part}` can be `Hair`, `Body`, `Dress`, `Dress1`, `Dress2`, etc.
    * Yes, this tool also handles special exceptions for characters like: `Yelan`, `Collei` and `Rosaria` who may have their `Dress` set to `Hair` instead of the usual `Body`.
    * No selection needed.
5. Import Character Textures
    * This step imports the character textures and assigns them to the materials imported in Step `Import Materials`.
    * Yes, this tool also handles special exceptions for characters like: `Yelan`, `Collei` and `Rosaria` who may have their `Dress` set to `Hair` instead of the usual `Body`.
    * **This step uses the cache (if enabled)** so you do not need to select a folder. It uses what was selected in Step `Import Character Model` (unless you've disabled it).
6. Import `miHoYo - Outlines`
    * This step imports the `miHoYo - Outlines` node group, which is found in the `experimental-blender-3.3` folder.
    * Select the `miHoYo - Outlines.blend` file.
    * **This step uses the cache (if enabled)** so you do not need to re-select the `miHoYo - Outlines.blend` after selecting it on first use.
7. Setup Outlines (Geometry Nodes)
    * This step creates and sets up the Outlines (Geometry Nodes modifier)
    * Naming Convention of Geometry Nodes: `GeometryNodes {Mesh Name}`
        * {Mesh Name} can be `Body`, `Face`, `Face_Eye`, `Brow` (`Face_Eye` and `Brow` don't really get used though and `Face_Eye` has Outline Thickness set to 0.0 by default)
    * Naming Convention of Outline Materials: `miHoYo - Genshin {Body Part} Outlines`
        * `{Body Part}` can be `Hair`, `Body`, `Dress`, `Dress1`, `Dress2`, etc.
    * No selection needed.
8. Import Lightmaps for Outlines
    * This step imports Lightmap textures and assigns them to to materials.
    * Yes, this tool also handles special exceptions for characters like: `Yelan`, `Collei` and `Rosaria` who may have their `Dress` set to `Hair` instead of the usual `Body`.
    * **This step uses the cache (if enabled)** so you do not need to select a folder. It uses what was selected in Step `Import Character Model` or Step `Import Character Textures` (unless you've disabled them).
9. Import Material Data
    * This step imports JSON files containing material data with useful information for shader accuracy, such as specular colors, metalmap scale, metallic colors, outline colors, shininess values, etc.
    * Select the JSON files with the material data (Ctrl + Click or Shift + Click).
10. ~~Fix Mouth Outlines~~ (Legacy, may be return in future releases) - **[Disabled by Default]**
    * This step "fixes" outlines on the mouth (Face) by assigning a Camera to the geometry node and setting Depth Offset. You will likely need to manually change the Depth Offset depending on your scene.
    * This step may not be needed if you use BetterFBX to import your model (not confirmed)
12. Make Character Upright
    * This step will reset the rotation and scale of the character armature and set the character armature to 90 degrees on the x-axis (standing upright).
    * No selection needed.
13. Setup Head Driver
    * This step will setup the Head Driver constraint so that face shadows work
    * No selection needed.
14. Set Color Management to 'Standard'
    * This step will set the Color Management to Standard (normally Filmic)
    * No selection needed.
15. Delete Specific Objects
    * This step deletes specific object(s) which is only EffectMesh at this time.
    * No selection needed.
16. Set Up ArmTwist Bone Constraints
    * This step will create Copy Rotation Bone Constraints on the ArmTwist bones to the Forearm bone (if the ArmTwist bones exist). 
    * It does this by reorienting the ArmTwist bones so the ArmTwist bone's Tail points towards the Forearm bone's Head.
    * Afterwards, it creates Copy Rotation Bone Constraints on the ArmTwist bones.
    * If you do not want these Bone Constraints, you can easily select the bones and turn off the bone constraint.
    * No selection needed.
</details>

<br>

## Development Roadmap / Future Features
### Features
- [X] Head Driver Setup
- [X] Make model upright if not upright (?)
- [X] ~~Scale up x100~~ Reset Scale (scaled to 1.0)
- [X] Character Ramp Type Mapping (automatically plug correct Body Ramp Type from Global Material Properties)
    - Requires knowing all characters who have a different the Body Ramp Type than the default
- [X] BetterFBX Support/Fix UV map imports (only one UV map is imported)
    - BetterFBX supported! The option is enabled by default if the addon is installed 
    - Created UV1 UV map which allows for underskirt textures (Zhongli, Lumine, etc.) 
      - This provides a texture, but not the correct texture on things like underskirts or the opposite side of some clothing
- [X] Color Management Filmic -> Standard
- [X] Turn Setup Wizard into an Addon
- [X] UI Setup Wizard Addon
- [ ] Update Configuration from UI (checkboxes that enable/disable steps)
- [ ] Batch Character Setup
- [X] Basic NPC Support
- [X] Basic Monster Support
- [X] Honkai Star Rail Support
### Refactoring
- [X] Refactor Material Assignment Mapping (externalize/centralize it to one locaiton)
- [ ] Refactor Import Outline Lightmaps component
- [ ] Refactor config.json from a dictionary to a List of dictionaries?
- [ ] Cache Service
- [ ] Invoker Class
- [ ] import_order.py is becoming too big
- [ ] invoke_next_step may not need to cache anymore since we can cache directly in Operators
- [X] Automated Tests
- [X] Support for Multiple Shader Versions/Games
### Misc.
- [X] Crude design diagram depicting how this tool and the components interact and work
- [ ] A refreshed design diagram with the UI Addon flow

(Legacy Setup Wizard Flow)
![alt text](https://user-images.githubusercontent.com/8632035/183316362-8a47f471-0fa4-4a3d-8e17-ea2c2a9a852e.png)

## "Tested" Character Models
Automated tests are run each release on all playable characters and a small subset of NPC characters.
<br>
This Setup Wizard should work on all playable characters, but if you do find any issues or need help, don't hesitate to reach out in the #help channel on Discord or open up an issue in this repository.

----

## :star: Credits :star:

Thanks to all those who helped answer the questions I had while building out this tool and learning about Blender on Festivity's Discord server.
<br>
**Shoutout to those in the #help channel assisting others**, hats off to you for your hard work and dedication to helping others.
<br>
And lastly all the wonderful people who I've collaborated, it's an been an absolutely tremendous and wonderful journey and experience.
<br>
* [@Festivity](https://github.com/festivities) 
— [YouTube](https://www.youtube.com/channel/UCXCTHNBA8TVs0s5aQuNtWwg)
| [Twitter](https://x.com/festivizing) 
* TheyCallMeSpy
* Sultana
* M4urlcl0
* Modder4869 
* [@BonnyAnimations](https://github.com/BonnyAnimations) 
— [YouTube](https://www.youtube.com/@BonnyAnimations) 
| [Twitter](https://x.com/BonnyTweetsOFF)
* Enthralpy 
— [YouTube](https://www.youtube.com/@Enthralpy)
| [Twitter](https://x.com/Enthralpy)
* [@OctavoPE](https://github.com/OctavoPE) 
— [Twitter](https://x.com/Llama3D)
* JaredNyts 
— [Twitter](https://twitter.com/jared_nyts)
* SubutaiProduction 
— [YouTube](https://www.youtube.com/@SubutaiProduction) 
| [Twitter](https://twitter.com/SubutaiEdits)
* Aiko 
— [YouTube](https://www.youtube.com/@AikoDesu)
| [Twitter](https://x.com/Aiko__ya)

Cheers and Happy Blending
