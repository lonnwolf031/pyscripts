import PIL
import sys
import os
import os.path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

'''
AUTHOR: © Lonn, 2020
USE: make a dedicated folder with duplicates of the images to resize as the original files will be overwritten
This script resizes images to a given size maintaining original aspect ratio
'''

image_path = sys.argv[1]
if os.path.exists(image_path):
    continue
else:
    print("The file does not exist. Program will terminate.")
    sys.exit();


#f = r'path//to//files'
width = 800
height = 600

for file in os.listdir(image_path):
    f_img = f+"/"+file
    img = Image.open(f_img)
    ratio_w = width / img.width
    ratio_h = height / img.height
    if ratio_w < ratio_h:
        # It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * img.height)
    else:
        # Fixed by height
        resize_width = round(ratio_h * img.width)
        resize_height = height
    img_resize = img.resize((resize_width, resize_height), Image.ANTIALIAS)
    img_resize.save(f_img)
