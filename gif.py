#!/usr/bin/env python3

from PIL import Image, ImageSequence

im = Image.open("spongebob.gif")

out = im.crop((200, 200, 400, 400)
for frame in ImageSequence.Iterate(im):
    im.rotate(45)

im.show()






#try:
#    for i in range(10):
#        im.seek(i)
#
#except EOFError:
#    pass
