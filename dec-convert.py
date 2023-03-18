"""Multiply each channel of 3 integer code r g b by some ratio.

Then print as 3 integer code."""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('r', help='red as int')
parser.add_argument('g', help='green as int')
parser.add_argument('b', help='blue as int')
parser.add_argument('ratio', help='float as ratio')
args = parser.parse_args()

r = int(args.r)
g = int(args.g)
b = int(args.b)
ratio = float(args.ratio)

channels = [r, g, b]

for i in range(len(channels)):
    channels[i] = int(channels[i] * ratio)

print(channels)
