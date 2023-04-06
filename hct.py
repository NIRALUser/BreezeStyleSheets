#!/usr/bin/env python
"""Compiles the theme and moves stylesheet.qss and resources.py to the HCT repo.

If you're using this, you will need to change PATH_TO_HCT_REPO_THEMES_DIR.

First create a new JSON in theme/. Make some changes.

Then run python hct.py <name-of-json>. Then you can fire up HCT with the new theme.

If we make changes to the directory structure, then this file will need to be modified slightly."""

import argparse
import os
import shutil
from pathlib import Path
import time

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

parser = argparse.ArgumentParser()

parser.add_argument("theme", help="name of theme")

args = parser.parse_args()

theme_name = args.theme

os.system(f"python configure.py --styles={theme_name} --resource custom.qrc")

# time.sleep(3)

os.system(
    f"python configure.py --styles={theme_name} --extensions=all --pyqt6 --resource custom.qrc --compiled-resource resources.py"
)

# time.sleep(3)

theme_dir = PATH_TO_HCT_REPO_THEMES_DIR / theme_name

if not theme_dir.exists():
    theme_dir.mkdir()

stylesheet_path: Path = Path.cwd() / "dist" / "qrc" / theme_name / "stylesheet.qss"
with open(stylesheet_path, "a") as stylesheet:
    stylesheet.write(
        "/* To make QMessageBox font not bold */\nQMessageBox QLabel {\n\tfont-weight: normal;\n}\n"
    )
shutil.copy(str(stylesheet_path), str(theme_dir / "stylesheet.qss"))

resource_path: Path = Path.cwd() / "resources.py"

data = 0

with open(resource_path, "r") as original:
    data = original.read()
    data = data.replace("from PyQt5 import QtCore", "from PyQt6 import QtCore")

with open(resource_path, "w") as new:
    new.write(data)

shutil.copy(str(resource_path), str(theme_dir / "resources.py"))

print("Success")
