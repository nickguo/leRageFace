import os, sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sentiment.rage
import random

(values, sentences) = sentiment.rage.getRageList("One day Lucy was walking. Then she was Nathan. And then a bird pooped on them. Oh fuck. The end.")

imageList = []

for i in range(len(values)):
    pos = values[i]
    if(pos <= .3):
        rageFace = Image.open("/root/leRageFace/server/10.png")
    elif(.3 < pos <= .4):
        number = random.randint(7,10)
        rageFace = Image.open("/root/leRageFace/server/" +  str(number) + ".png")
    elif(.4 < pos <= .5):
        number = random.randint(4,6)
        rageFace = Image.open("/root/leRageFace/server/" + str(number) + ".png")
    elif(.5 < pos <= .6):
        number = random.randint(0,3)
        rageFace = Image.open("/root/leRageFace/server/" + str(number) + ".png")
    else:
        rageFace = Image.open("/root/leRageFace/server/0.png")
    
    rageFace = rageFace.resize((150, 150), Image.ANTIALIAS)
    img_w,img_h = rageFace.size
    background = Image.new('RGBA', (200,200), (255,255,255,255))
    bg_w,bg_h=background.size
    offset=((bg_w-img_w),(bg_h-img_h))
    background.paste(rageFace,offset)
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("courier.ttf", 15)
    text = sentences[i]
    textList = []
    counter = 0
    while(counter < len(text)):
        edge = counter + 20
        if(edge < len(text)):
            while(text[edge] != " "):
                edge = edge - 1
            textList.append(text[counter:edge])
            counter = edge
        else:
            textList.append(text[counter:])
            break
    x = 1
    y = 1
    for i in range(len(textList)):
        draw.text((x,y), textList[i], (0,0,0), font=font)
        y  = y + 20
    draw.rectangle(((1,1),(199,199)), outline = "black")
    draw.rectangle(((0,0),(200,200)), outline = "black")
    imageList.append(background)

height = len(values)/2 + len(values)%2
background = Image.new('RGBA', (400, height*200), (255,255,255,255))
y = 0
x = 0
for i in range(len(values)):
    if(i%2 == 0):
        x = 0
    else:
        x = 200
    if(i%2 == 0 and i != 0):
        y += 200
    background.paste(imageList[i],((x),(y)))
if (len(values)%2 == 1):
    draw = ImageDraw.Draw(background)
    draw.rectangle(((201,y + 1),(199,y + 199)), outline = "black")
    draw.rectangle(((200,y),(400,y + 200)), outline = "black")
background.save("final.jpg")
    

