# BreezeStyleSheets fork

This is a fork of [https://github.com/Alexhuszagh/BreezeStyleSheets](https://github.com/Alexhuszagh/BreezeStyleSheets) used for HeadCircumferenceTool's GUI stylesheets.

I wrote a script that compiles every theme JSON file in theme/ to `stylesheet.qss` and `resources.py` and moves them, along with the JSON file, over to the HCT repo.

First, change `hct.py` `PATH_TO_HCT_REPO_THEMES_DIR` to the path to your HCT themes/ directory.

## Add to stylesheet

Modify `append.qss`. Whatever is there will be appended to *every* theme's stylesheet when running `hct.py`.

If appending won't work for your change, then you'll need to modify `hct.py` to replace instead of append.

## Add new theme

Copy `theme/dark-hct.json` (for dark theme) or `theme/light-hct.json` (for light theme) and paste to a new file in `theme/`.

Change the `"highlight"` field to the main color of your new theme. `hct.py` will overwrite several fields of your new JSON using this main color.

For changes that are more involved than just adding a new color, `hct.py` would need to be modified.
