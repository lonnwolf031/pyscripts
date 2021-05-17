import PIL
import sys
import os
import os.path
from PIL import Image
import argparse
Image.MAX_IMAGE_PIXELS = None

'''
AUTHOR: © Lonn, 2020
USE: make a pixelated mosaic of an image. 
High-res image converted to small size and then enlarged with nearest-neighbor
'''

parser = argparse.ArgumentParser('Image to mosaic art')
parser.add_argument('--source')
parser.add_argument('--xtiles')
parser.add_argument('--sizetiles')

def makeSmaller(img):
    width = xtiles
    ratio_w = width / img.width
    resize_width = width
    resize_height = round(ratio_w * img.height)
    img_resize = img.resize((resize_width, resize_height), Image.ANTIALIAS)
    return img_resize

def makeMosaic(resized_img):
    #numpy and nearest neighbour
    pass


try:
    args = parser.parse_args()
    image_path = str(args.source)
    xtiles = int(args.xtiles)
    sizetiles = int(args.sizetiles)
except Exception as e:
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


if os.path.exists(image_path):
    try:
        img = Image.open(image_path)
        makeSmaller(img)
    except Exception as e:
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    sys.exit();
else:
    print("The file does not exist. Program will terminate.")
    sys.exit();

