import json
from pathlib import Path

HCT_THEME_COLOR: str = "b55162"
DARK_THEME_COLOR: str = "3daee9"
LIGHT_THEME_COLOR: str = "3daef3"


# Source: https://github.com/Alexhuszagh/BreezeStyleSheets/blob/main/configure.py#L82
def load_json_ignore_comments(path: Path) -> dict:
    """Load config.json file, ignoring comments //.

    Source: https://github.com/Alexhuszagh/BreezeStyleSheets/blob/main/configure.py#L82
    """
    with open(path) as f:
        lines = f.read().splitlines()
    lines = [i for i in lines if not i.strip().startswith("//")]
    return json.loads("\n".join(lines))


def hex_color_times_ratio(hex_color: str, ratio: float) -> str:
    """Given 6-hexit color code rrggbb, multiply by ratio
    and output a 6-hexit color code rrggbb.

    :param hex_color: rrggbb
    :type hex_color: str
    :param ratio: 0.0 <= ratio <= 1.0
    :type ratio: float
    :return: hex_color * ratio
    :rtype: str"""
    if len(hex_color) != 6:
        raise Exception("rrggbb hex_color")
    if ratio < 0 or ratio > 1:
        raise Exception("0 <= ratio <= 1, you inputted outside this range")
    channels = bytes.fromhex(hex_color)
    rv = str(
        hex(
            int(channels[0] * ratio) << 16
            | int(channels[1] * ratio) << 8
            | int(channels[2] * ratio)
        )
    )[2:]
    if len(rv) < 6:
        rv = "0" * (6-len(rv)) + rv
    return rv

def hex_color_to_dec(hex_color: str) -> tuple[int, int, int]:
    """
    :param hex_color:
    :type hex_color: str
    :return: (r, g, b) in dec
    :rtype: tuple[int, int, int]"""
    if len(hex_color) != 6:
        raise Exception("rrggbb hex_color")
    channels = bytes.fromhex(hex_color)
    return (channels[0], channels[1], channels[2])
