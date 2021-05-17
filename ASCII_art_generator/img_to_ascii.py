import sys
import os
from PIL import Image
from PIL import ImageFont, ImageDraw
import argparse
import traceback


'''
AUTHOR: © Lonn, 2020
USE:
'''

parser = argparse.ArgumentParser('Image to ASCII art')
parser.add_argument('--source')
parser.add_argument('--layers', type=int, default=5)
try:
    args = parser.parse_args()
    image_path = str(args.source)
    numlayers = int(args.layers)
    print(numlayers)
except Exception as e:
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


asciitxtlayerstack = []
asciiimglayers = []

new_width = 120
new_height = 120
fontsize = 40

sizex = 0
sizey = 0

fnt = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansMono.ttf", fontsize)

# pass the image as command line argument
# image_path = sys.argv[1]

# arg for numlayers

thresholdstep = 255 // numlayers

if os.path.exists(image_path):
    try:
        img = Image.open(image_path)
    except:
        print("Failed to open image")
else:
    print("The file does not exist. Program will terminate.")
    sys.exit();


def layertoascii(lr):
    # resize the image
    width, height = lr.size
    aspect_ratio = height / width

    global new_height
    new_height = int(round(aspect_ratio * new_width * 0.55))
    lr = lr.resize((new_width, int(new_height)))
    lr = lr.convert('L')
    pixels = lr.getdata()

    # replace each pixel with a character from array
    chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_text = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_text = "\n".join(ascii_text)
    #print(ascii_text)
    text_file = open("Output.txt", "w")
    text_file.write(ascii_text + "\n\n")
    text_file.close()
    asciitxtlayerstack.append(ascii_text)


def layertoimglayer(ascii_layers):
    no = 0
    for y in asciitxtlayerstack:
        try:
            strline = y.partition("\n")[0]
            print("strlen" + str(len(strline)))
            lnx, lny = fnt.getsize(strline)
            for i, l in enumerate(y):
                pass
            textlength = i + 1

            global sizex, sizey

            sizex = int(round(lnx))
            sizey = int(round(lny * textlength))

            print("sizex = " + str(sizex))
            print("sizey = " + str(sizey))
        except Exception as e:
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

        out = Image.new("RGB", (sizex, sizey), (255, 255, 255))

        # get a font


        # get a drawing context
        d = ImageDraw.Draw(out)
        #
        # # draw multiline text
        d.multiline_text((10, 10), y, font=fnt, fill=(0, 0, 0))
        out.putalpha(1)
        asciiimglayers.append(out)
        #
        out.save(str(no) + ".png")
        # no = no + 1

    # out.show()


def makesingleimg(asciiimglayers):
    temp = Image.new("RGB", (new_width, new_height), (255, 255, 255))
    temp.putalpha(1)
    for lr in asciiimglayers:
        lr.putalpha(1)
        temp = Image.alpha_composite(temp, lr)
    final = temp.save("result.png")


for x in range(numlayers):
    lr = img.copy()
    threshold = x * thresholdstep
    lr = lr.point(lambda p: p > threshold and 255)
    layertoascii(lr)
    layertoimglayer(asciitxtlayerstack)
   # makesingleimg(asciiimglayers)
