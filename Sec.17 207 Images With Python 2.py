#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 207. Images With Python 2

# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

# https://unsplash.com/t/current-events - Free photos

from PIL import Image, ImageFilter

img1 = Image.open("./Sec.17 206 Images With Python/pikachu.jpg")

img7 = img1.rotate(90)
img7.show()
img7.save("./Sec.17 206 Images With Python/pikachu_rotate.png", 'png')

# Resize to 50% of the original size
new_size=(int(img1.size[0]/2), int(img1.size[1]/2))
img8 = img1.resize(new_size)
img8.show()
img8.save("./Sec.17 206 Images With Python/pikachu_resize.png", 'png')

# Coordinates start from top left. 
# box8 - 120,140 top left and 400,370 bottom right corners
box8=(120, 140, 400, 370)
img8 = img1.crop(box8)
img8.show()
img8.save("./Sec.17 206 Images With Python/pikachu_crop.png", 'png')
