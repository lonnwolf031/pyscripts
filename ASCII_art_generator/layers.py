'''
As far as I see it, you can easily transform the white pixels of your image to
transparent with Pillow and them mask them layer upon layer.

To convert white pixels to transparent, you need to first convert the image data
to buffer and then re-create it from the buffer, here is a sample code:
'''



from PIL import Image
# your loop here
img = Image.open('img.png')
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("mod_img1.png", "PNG")
# Then do your usual paste as you are doing in your code.

background = Image.open("mod_img1.png")
foreground = Image.open("mod_img2.png")

background.paste(foreground, (0, 0), foreground)
background.show()
