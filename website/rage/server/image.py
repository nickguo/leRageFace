import os, sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import rage.sentiment.ragesent
import random
import os

class RageFaceGenerator:
    def Generate(self, string):
        (values, sentences) = rage.sentiment.ragesent.getRageList(string)
        imageList = []
        for i in range(len(values)):
            female = ""
            pos = values[i]
            if "Derpina" in sentences[i]:
                female = "female"
            if(pos <= .2):
                rageFace = Image.open( os.path.join(os.path.dirname(__file__),female + "10.png"))
            elif(.2 < pos <= .45):
                number = random.randint(7,10)
                rageFace = Image.open( os.path.join(os.path.dirname(__file__),female + str(number) + ".png"))
            elif(.45 < pos <= .6):
                number = random.randint(4,6)
                rageFace = Image.open( os.path.join(os.path.dirname(__file__),female + str(number) + ".png"))
            elif(.6 < pos <= .7):
                number = random.randint(0,3)
                rageFace = Image.open( os.path.join(os.path.dirname(__file__),female + str(number) + ".png"))
            else:
                rageFace = Image.open(os.path.join(os.path.dirname(__file__),female + "0.png"))
            
            rageFace = rageFace.resize((150, 150), Image.ANTIALIAS)
            img_w,img_h = rageFace.size
            background = Image.new('RGBA', (200,200), (255,255,255,255))
            bg_w,bg_h=background.size
            offset=((bg_w-img_w),(bg_h-img_h))
            background.paste(rageFace,offset)
            draw = ImageDraw.Draw(background)
            font = ImageFont.truetype(os.path.join(os.path.dirname(__file__),"courier.ttf"), 15)
            text = sentences[i]
            textList = []
            counter = 0
            while(counter < len(text)):
                edge = counter + 20
                if(edge < len(text)):
                    while(text[edge] != " "):
                        edge = edge - 1
                    edge = edge + 1
                    textList.append(text[counter:edge])
                    counter = edge
                else:
                    textList.append(text[counter:])
                    break
            x = 6
            y = 6
            for i in range(len(textList)):
                draw.text((x,y), textList[i], (0,0,0), font=font)
                y  = y + 16
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
        if (len(values)%2 == 1 and len(values) != 1):
            draw = ImageDraw.Draw(background)
            draw.rectangle(((201,y + 1),(199,y + 199)), outline = "black")
            draw.rectangle(((200,y),(400,y + 200)), outline = "black")
        image_name = (str)(random.randint(1,10000000)) + ".jpg"
        background.save(os.path.join(os.path.abspath(os.path.dirname(__file__)+'/../static/img'), image_name))
        return image_name
    

