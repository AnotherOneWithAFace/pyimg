#!/usr/bin/env python3

from PIL import Image, ImageDraw
import sys

def main():
    im = Image.open(sys.argv[1])
    #im1 = Image.open(sys.argv[2])

    draw = ImageDraw.Draw(im)
    draw.line((0, 0, im.size), fill=256, width=10)
    draw.line((0, im.size[1], im.size[0], 0), fill=256, width=10)
    draw.line(((im.size[0] / 2), 0, (im.size[0] / 2), (im.size[0] / 2)), fill=256, width=10)
    draw.line((0, (im.size[1] / 2), im.size[0], (im.size[1] / 2)), fill=256, width=10) # Horizontal

    im.show()

main()

#print(sys.argv)
