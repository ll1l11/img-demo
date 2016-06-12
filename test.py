# -*- coding: utf-8 -*-
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

s = 'abc\naaaa\ndd\tdddd\bdd\n\ddd'

x = 500
y =  700

img = Image.new(mode='RGB', size=(x, y), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font='MFShangHei_Noncommercial-Regular.otf', size=20)

draw.text((0, 0), s, font=font, fill=(0, 0, 0))
img.save('aaa.bmp')
