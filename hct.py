#!/usr/bin/env python

"""Compiles the theme json file, to stylesheet.qss and resources.py files.

Appends the stuff in append.qss to stylesheet.qss.

Lastly, moves stylesheet.qss and resources.py to PATH_TO_HCT_REPO_THEMES_DIR.

If you're using this, you will need to change PATH_TO_HCT_REPO_THEMES_DIR.

First create a new JSON in theme/. Make some changes.

Then run python hct.py <name-of-json> <theme-color>. Then you can fire up HCT with the new theme.

If we make changes to the directory structure, then this file will need to be modified slightly."""

import argparse
import os
import shutil
from pathlib import Path
import json
from helpers import load_json_ignore_comments, hex_color_times_ratio, hex_color_to_dec

PATH_TO_HCT_REPO_THEMES_DIR: Path = (
    Path().home()
    / "Documents"
    / "GitHub"
    / "COMP523"
    / "HeadCircumferenceTool"
    / "src"
    / "GUI"
    / "themes"
)
"""Modify this if you're not Jesse, unless you stole his computer idk"""

parser = argparse.ArgumentParser()
parser.add_argument("theme", help="name of theme")
parser.add_argument("color", help="theme color as 6-hexit rrggbb string")
args = parser.parse_args()
theme_name: str = args.theme

color: str = args.color
color_dec: tuple[int, int, int] = hex_color_to_dec(color)
r, g, b = color_dec[0], color_dec[1], color_dec[2]

dark_color: str = hex_color_times_ratio(color, 0.843137)
dark_color_dec: tuple[int, int, int] = hex_color_to_dec(dark_color)
dark_r, dark_g, dark_b = dark_color_dec[0], dark_color_dec[1], dark_color_dec[2]

darker_color: str = hex_color_times_ratio(color, 0.607843)
darker_color_dec: tuple[int, int, int] = hex_color_to_dec(darker_color)
darker_r, darker_g, darker_b = darker_color_dec[0], darker_color_dec[1], darker_color_dec[2]

# Modify a few entries in the JSON based on args.color
json_dict: dict = load_json_ignore_comments(Path("theme") / (theme_name + '.json'))
json_dict["highlight"] = "#" + color
json_dict["highlight:dark"] = "#" + dark_color
json_dict["highlight:alternate"] = "#" + darker_color
json_dict["view:checked"] = "#" + color
json_dict["view:hover"] = f"rgba({r}, {g}, {b}, 0.1)"
json_dict["slider:foreground"] = "#" + color
json_dict["scrollbar:hover"] = "#" + color
if "light" in theme_name:
    json_dict["highlight"] = f"rgba({r}, {g}, {b}, 0.5)"
    json_dict["highlight:dark"] = f"rgba({dark_r}, {dark_g}, {dark_b}, 0.5)"
    json_dict["highlight:alternate"] = f"rgba({darker_r}, {darker_g}, {darker_b}, 0.6)"
    json_dict["view:hover"] = f"rgba({r}, {g}, {b}, 0.2)"
    json_dict["scrollbar:hover"] = f"rgba({r}, {g}, {b}, 0.8)"
    json_dict["scrollbar:background"] = "#bfc0c0"
    json_dict["scrollbar:background:hover"] = "#9f9f9e"

# Overwrite old json
# If you want to see the old JSON with comments, check the file history of
# dark-hct.json, light-hct.json, dark.json, light.json
with open(Path("theme") / (theme_name + '.json'), 'w') as theme_json:
    json.dump(json_dict, theme_json, indent=4)
    theme_json.write("\n")

# Compile stuff
# These commands are from the BSS README
os.system(f"python configure.py --styles={theme_name} --resource custom.qrc")
os.system(
    f"python configure.py --styles={theme_name} --extensions=all --pyqt6 --resource custom.qrc --compiled-resource resources.py"
)

theme_dir = PATH_TO_HCT_REPO_THEMES_DIR / theme_name
if not theme_dir.exists():
    print("PATH_TO_HCT_REPO_THEMES_DIR is incorrect")
    exit(1)

stylesheet_path: Path = Path.cwd() / "dist" / "qrc" / theme_name / "stylesheet.qss"
# Append new QSS content to the end of the stylesheet
# If something conflicts with what's already in the stylesheet, then maybe need to
# overwrite instead of append
# And if adding more things, definitely find a better way to do this lol
with open(Path("append.qss"), 'r') as append_file:
    stuff_to_append: str = append_file.read()
with open(stylesheet_path, "a") as stylesheet:
    stylesheet.write(stuff_to_append)
shutil.copy(str(stylesheet_path), str(theme_dir / "stylesheet.qss"))

# Compile resources
# There should not be a reason to modify this
resource_path: Path = Path.cwd() / "resources.py"
data = 0
with open(resource_path, "r") as original:
    data = original.read()
    data = data.replace("from PyQt5 import QtCore", "from PyQt6 import QtCore")
with open(resource_path, "w") as new:
    new.write(data)
shutil.copy(str(resource_path), str(theme_dir / "resources.py"))
os.remove(str(resource_path))

print("Success")
