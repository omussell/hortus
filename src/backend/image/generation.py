
from PIL import Image, ImageDraw

def generate_image():
    #return "Hello"
 
    #img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    # 
    #d1 = ImageDraw.Draw(img)
    #d1.text((10,10), "Hello World", fill=(255,255,0))
    
    im = Image.new('RGB', (500, 300), (128, 128, 128))
    draw = ImageDraw.Draw(im)
    draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
    draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
    draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)
    im.save('my_image.png')