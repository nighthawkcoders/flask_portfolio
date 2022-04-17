#!/usr/bin/python
from PIL import Image, ImageFont, ImageDraw
from requests import get
import random

sponges = {1:"smallsponge1.jpeg", 2:"smallsponge2.jpeg", 3:"medsponge.jpeg", 4:"bigsponge1.jpeg", 5:"bigsponge2.jpeg"}

chosen_sponge = random.randint(1, 5)

spongebob_img = Image.open(sponges.get(chosen_sponge))

ip = get('https://api.ipify.org').text

spongeheight = spongebob_img.height
spongewidth = spongebob_img.width

while spongeheight%3==0:
    spongeheight = spongeheight + 1

text_width = int(spongeheight/10)

title_font = ImageFont.truetype('impact.ttf', text_width)
title_text = ip

image_editable = ImageDraw.Draw(spongebob_img)

image_editable.text((random.randrange(spongewidth)/2, random.randrange(spongeheight)/2), title_text, (random.randrange(255), random.randrange(255), random.randrange(255)), font=title_font)

spongebob_img.save("spongeresult.jpeg")
