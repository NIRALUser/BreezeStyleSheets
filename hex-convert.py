"""Multiply each channel of 6-hexit code rrggbb by some ratio.

Then print as 6-hexit hexcode."""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('hex', help='6-hexit code rrggbb')
parser.add_argument('ratio', help='ratio as float')
args = parser.parse_args()

channels = bytes.fromhex(args.hex)
ratio = float(args.ratio)

rv = int(channels[0] * ratio) << 16 | int(channels[1] * ratio) << 8 | int(channels[2] * ratio)

print(hex(rv))
