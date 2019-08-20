#!/usr/bin/env python3

from PIL import Image

im0 = Image.open('C.png')
box = (100, 100, 800, 700)
region0 = im0.crop(box)
im1 = Image.open('lain.jpg')
im1.paste(region0, box)
im1.show()
