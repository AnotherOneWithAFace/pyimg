#!/usr/bin/env python3

from PIL import Image, ImageDraw

im = Image.open('lain.jpg')
im1 = Image.open('C.png')

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=256, width=10) # Down Diagonal
draw.line((0, im.size[1], im.size[0], 0), fill=256, width=10) # Up Diagonal
draw.line(((im.size[0] / 2), 0, (im.size[0] / 2), (im.size[0] / 2)), fill=256, width=10) # Vertical
draw.line((0, (im.size[1] / 2), im.size[0], (im.size[1] / 2)), fill=256, width=10) # Horizontal

q1 = (im.size[0] / 4)
q2 = (im.size[1] / 4)
q3 = (q1 * 3)
q4 = (q2 * 3)

box = (q1, q2, q3, q4)
region = im.crop(box)

im1.paste(region, (300, 200, 900, 600))

im1.show()

#region.show()
#im.show()
