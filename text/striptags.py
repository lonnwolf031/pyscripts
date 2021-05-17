import re
import sys
import os

'''
AUTHOR: © Lonn, 2021
USE: strip html/xml-like tags from text, for instance from downloaded transcripts
'''

text = ""

ifile = sys.argv[1]

new_file_name = sys.argv[1].replace('.txt', '_edit.txt')

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


if os.path.exists(ifile):
   with open(ifile, 'r') as file:
       try:
          data = file.read()
          text = cleanhtml(data)
          print(text)
       except :
           print("an error occurred")
           sys.exit()
   with open(new_file_name, 'w') as f:
   	f.write(text)
