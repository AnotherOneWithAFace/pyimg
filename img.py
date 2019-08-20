#!/usr/bin/env python3

from PIL import Image

im = Image.open('lain.jpg')
box = (200, 200, 400, 400)
region = im.crop(box)
region = region.transpose(Image.ROTATE_90)
im.paste(region, box)
im.show()

def roll(image, delta):
    # Rolls an image on its side

    xsize, ysize = image.size
    delta %= xsize
    if delta == 0:
        return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, ysize, xsize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image

roll(im, 90)
image.show()
