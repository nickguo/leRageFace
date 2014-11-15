import os, sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

rageFace = Image.open("images/troll.jpg")

#font = ImageFont.truetype("~/../usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)

draw = ImageDraw.Draw(rageFace)
draw.text((10,10), "Troll" ,(0,0,0))#, font=font)
draw = ImageDraw.Draw(rageFace)
rageFace.save("test.jpg")


