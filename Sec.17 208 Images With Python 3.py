#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 208. Images With Python 3

# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

# https://unsplash.com/     -    Free photos

from PIL import Image, ImageFilter

img10 = Image.open("./Sec.17 206 Images With Python/astro.jpg")
print("astro.jpg:           ", img10)

# .thumbnail will modify picture, keeping aspect ratio
MAX_SIZE=400,400
img10.thumbnail(MAX_SIZE)  
img10.show()

img10.save("./Sec.17 206 Images With Python/astro_thumbnail.jpg")

img11 = Image.open("./Sec.17 206 Images With Python/astro_thumbnail.jpg")
print("astro_thumbnail.jpg: ", img11)
