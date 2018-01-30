#我要加一句话
from PIL import Image,ImageFont,ImageDraw
im=Image.open('./0.png')
w,h=im.size
font=ImageFont.truetype()
draw=ImageDraw.Draw(im)
draw.text((w/5,h/5),"ok",fill=(255,0,0),font=font)
im.save('1.png','png')