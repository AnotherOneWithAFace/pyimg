#!/usr/bin/env python3

from PIL import Image, ImageEnhance

im = Image.open('lain.jpg').convert("RGB")
out0 = im.resize((1024, 1024))
out1 = out0.crop((100, 100, 400, 400)).rotate(45)
im.paste(out1, (100, 100, 400, 400))
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast!")
