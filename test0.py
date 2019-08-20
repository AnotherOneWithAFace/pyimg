#!/usr/bin/env python3

from PIL import Image, ImageDraw
import sys

im = Image.open(sys.argv[1])
draw = ImageDraw.Draw(im)
draw.line((((im.size[0] / 2), im.size[1] / 2), im.size), fill=256, width=5)
im.show()
