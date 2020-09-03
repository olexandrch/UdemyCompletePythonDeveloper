#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 209. Exercise: JPG to PNG Pokedex Converter

# Program to convert JPG to PNG. Provide two arguments. 
# First - a folder with .jpg files.
# Second - a folder where .png will be stored.

import sys
import os
from PIL import Image

# grab the first and second arguments



# check if Second folder exists and create if not.

# loop through the folder, convert to .png and save to the new folder




img10 = Image.open("./Sec.17 206 Images With Python/astro.jpg")
print("astro.jpg:           ", img10)

# .thumbnail will modify picture, keeping aspect ratio
MAX_SIZE=400,400
img10.thumbnail(MAX_SIZE)  
img10.show()

img10.save("./Sec.17 206 Images With Python/astro_thumbnail.jpg")

img11 = Image.open("./Sec.17 206 Images With Python/astro_thumbnail.jpg")
print("astro_thumbnail.jpg: ", img11)
