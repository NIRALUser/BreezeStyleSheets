# BreezeStyleSheets fork

This is a fork of [https://github.com/Alexhuszagh/BreezeStyleSheets](https://github.com/Alexhuszagh/BreezeStyleSheets) for HeadCircumferenceTool's GUI.

I wrote a script that takes a theme name and 6-hexit color and modifies the theme, compiles, and puts it in the HCT repo.

Copy theme/dark-hct.json (for dark theme) or theme/light-hct.json (for light theme) and paste to a new file in theme/.

Edit `hct.py` `PATH_TO_HCT_REPO_THEMES_DIR` with the path to your HCT themes/ directory.

Then run this command with the name of the file.

```text
usage: python hct.py [-h] theme color

positional arguments:
  theme       name of theme
  color       theme color as 6-hexit rrggbb string

options:
  -h, --help  show this help message and exit
```

For example, run `python hct.py dark-hct b55162` to compile dark-hct.json, modify colors in the JSON, compile to stylesheet.qss and resources.py, and copy to the HCT repo.
