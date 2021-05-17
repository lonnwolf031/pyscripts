import cv2
import os
import sys

'''
AUTHOR: © Lonn, 2021
USE: encode messages in images
'''

message_max_len = 100

def check_validity(path):
    if os.path.exists(path):
        pass
    else:
        print("One of the files does not exist. Program will terminate.")
        sys.exit()

def get_msg(msg_path):
    with open(msg_path) as f:
        contents = f.read()
        if len(contents) < message_max_len:
            return contents
        else:
            print("message is too long. Program will terminate")
            sys.exit()

def char_generator(message):
  for c in message:
    yield ord(c)

def pure_imagename(path):
  pure_imgname = str(path).split(".")
  return pure_imgname[0]

def get_image(image_path):
  img = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)
  if img is None:
      print("Image could not be read")
      sys.exit()
  return img

def gcd(x, y):
  while(y):
    x, y = y, x % y

  return x

def encode_image(image_location, msg):
  img = get_image(image_location)
  msg_gen = char_generator(msg)
  pattern = gcd(len(img), len(img[0]))
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i+1 * j+1) % pattern == 0:
        try:
          img[i-1][j-1][0] = next(msg_gen)
        except StopIteration:
          img[i-1][j-1][0] = 0
          return img

def decode_image(img_loc):
  img = get_image(img_loc)
  pattern = gcd(len(img), len(img[0]))
  message = ''
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i-1 * j-1) % pattern == 0:
        if img[i-1][j-1][0] != 0:
          message = message + chr(img[i-1][j-1][0])
        else:
          return message

def main():
    print("This script lets you encode and decode a batch of images in a directory \n")
    directory = str(input("Enter path...\n"))
    for entry in os.scandir(directory):
        if (entry.path.endswith(".jpg") or entry.path.endswith(".png")) and entry.is_file():
            img_path = str(entry.path)
            print("Checking validity of your image...")
            check_validity(img_path)
            pure_imgname = pure_imagename(img_path)
            print("Now enter the path of your message in a text file. (*.txt). Note: the maximum allowed message is 100 characters. \n")
            msg_path = str(input("Enter path..."))
            print("Checking validity of your text...")
            check_validity(msg_path)
            msg = get_msg(msg_path)
            print("Encoding...")
            encodedimg = encode_image(img_path, msg)
            newfile = pure_imgname + ".png"
            cv2.imwrite(newfile, encodedimg)
    sys.exit()

if __name__ == "__main__":
    main()
