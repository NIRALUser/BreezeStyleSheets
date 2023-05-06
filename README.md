# BreezeStyleSheets fork

This is a fork of [https://github.com/Alexhuszagh/BreezeStyleSheets](https://github.com/Alexhuszagh/BreezeStyleSheets) used for [NeuroRuler's](https://github.com/NIRALUser/NeuroRuler) GUI stylesheets.

I wrote a script that compiles every theme JSON file in theme/ to `stylesheet.qss` and `resources.py` and moves them, along with the JSON file, over to the NR repo.

First, change `nr.py`'s `PATH_TO_NR_REPO_THEMES_DIR` to the path to your NR themes/ directory.

The script requires `pyrcc5`. On macOS, use this command.

```sh
pip3 install pyqt5 --config-settings --confirm-license= --verbose
```

[Source](https://stackoverflow.com/a/74377566)

## Add to stylesheet

Modify `append.qss`. Whatever is there will be appended to *every* theme's stylesheet when running `nr.py`.

If appending won't work for your change, then you'll need to modify `nr.py` to replace instead of append.

## Add theme with new main color

This won't create a brand-new theme. It'll just create a theme that looks the same as dark-nr or light-nr but with a different main color.

Copy `theme/dark-nr.json` (for dark theme) or `theme/light-nr.json` (for light theme) and paste to a new file in `theme/`.

Change the `"highlight"` field to the main color of your new theme. `nr.py` will use this main color overwrite several fields of your new JSON.

For changes that are more involved than just adding a new color, `nr.py` would need to be modified.

## Modify color schemes

This is how you would make significant changes to all themes.

As the BSS README says, not a lot of fields should differ between themes. For example, I ran `diff` on some of the original theme JSON's, and this was the output:

<details>
    <summary>dark vs. dark-green</summary>

```bash
❯ diff theme/dark.json theme/dark-green.json
8,10c8,10
<     "highlight": "#3daee9",
<     "highlight:dark": "#2a79a3",
<     "highlight:alternate": "#2f88b7",
---
>     "highlight": "#33b833",
>     "highlight:dark": "#2b992b",
>     "highlight:alternate": "#1f991f",
15,16c15,16
<     "view:checked": "#334e5e",
<     "view:hover": "rgba(61, 173, 232, 0.1)",
---
>     "view:checked": "#325c32",
>     "view:hover": "rgba(63, 232, 63, 0.1)",
28c28
<     "slider:foreground": "#3daee9",
---
>     "slider:foreground": "#33b833",
31c31
<     "checkbox:light": "#58d3ff",
---
>     "checkbox:light": "#40e640",
33c33
<     "scrollbar:hover": "#3daee9",
---
>     "scrollbar:hover": "#33b833",
```
</details>

<details>
    <summary>dark vs. light</summary>

```bash
❯ diff theme/dark.json theme/light.json
4,41c4,41
<     "foreground": "#eff0f1",
<     "foreground:light": "#ffffff",
<     "background": "#31363b",
<     "background:alternate": "#31363b",
<     "highlight": "#3daee9",
<     "highlight:dark": "#2a79a3",
<     "highlight:alternate": "#2f88b7",
<     "midtone": "#76797c",
<     "midtone:light": "#b0b0b0",
<     "midtone:dark": "#626568",
<     "midtone:hover": "#8a8d8f",
<     "view:checked": "#334e5e",
<     "view:hover": "rgba(61, 173, 232, 0.1)",
<     "toolbar:horizontal:background": "#31363b",
<     "toolbar:vertical:background": "#31363b",
<     "view:corner": "#31363b",
<     "view:header:border": "#76797c",
<     "view:header": "#31363b",
<     "view:border": "#31363b",
<     "view:background": "#1d2023",
<     "text:background": "#1d2023",
<     "tab:background:selected": "#31363b",
<     "tab:background": "#2c3034",
<     "tree": "#afafaf",
<     "slider:foreground": "#3daee9",
<     "slider:handle:background": "#1d2023",
<     "menu:disabled": "#76797c",
<     "checkbox:light": "#58d3ff",
<     "checkbox:disabled": "#c8c9ca",
<     "scrollbar:hover": "#3daee9",
<     "scrollbar:background": "#1d2023",
<     "scrollbar:background:hover": "#76797c",
<     "button:background": "#31363b",
<     "button:background:pressed": "#454a4f",
<     "button:border": "#76797c",
<     "button:checked": "#626568",
<     "button:disabled": "#454545",
<     "close:hover": "#eff0f1",
---
>     "foreground": "#31363b",
>     "foreground:light": "#272b2f",
>     "background": "#eff0f1",
>     "background:alternate": "#eaebec",
>     "highlight": "rgba(51, 164, 223, 0.5)",
>     "highlight:dark": "rgba(45, 147, 200, 0.5)",
>     "highlight:alternate": "rgba(71, 184, 243, 0.6)",
>     "midtone": "#bab9b8",
>     "midtone:light": "#bab9b8",
>     "midtone:dark": "rgba(106, 105, 105, 0.7)",
>     "midtone:hover": "#787876",
>     "view:checked": "#b9dae7",
>     "view:hover": "rgba(61, 173, 232, 0.2)",
>     "toolbar:horizontal:background": "#eff0f1",
>     "toolbar:vertical:background": "#eff0f1",
>     "view:corner": "#eff0f1",
>     "view:header": "#eff0f1",
>     "view:header:border": "#bab9b8",
>     "view:border": "#bab9b8",
>     "view:background": "#eff0f1",
>     "text:background": "#eff0f1",
>     "tab:background:selected": "#eff0f1",
>     "tab:background": "#d9d8d7",
>     "tree": "#4b4b4b",
>     "slider:foreground": "#3daef3",
>     "slider:handle:background": "#eff0f1",
>     "menu:disabled": "#bab9b8",
>     "checkbox:light": "#272b2f",
>     "checkbox:disabled": "#6a6e71",
>     "scrollbar:hover": "rgba(51, 164, 223, 0.8)",
>     "scrollbar:background": "#eff0f1",
>     "scrollbar:background:hover": "#c7c7c6",
>     "button:background": "#eaebec",
>     "button:background:pressed": "#bedfec",
>     "button:border": "#bab9b8",
>     "button:checked": "#c7c7c6",
>     "button:disabled": "#b4b4b4",
>     "close:hover": "#31363b",
43c43
<     "dock:background": "#31363b",
---
>     "dock:background": "#eaebec",
45,48c45,48
<     "critical": "#80404a",
<     "information": "#406880",
<     "question": "#634d80",
<     "warning": "#99995C"
---
>     "critical": "#ff8c9f",
>     "information": "#8cd5ff",
>     "question": "#c08cff",
>     "warning": "#ffff8c"
```
</details>

But if you really want to change the themes, then you would do so in `nr.py`.
