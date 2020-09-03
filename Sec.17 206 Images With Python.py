#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 206. Images With Python

# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

from PIL import Image, ImageFilter

img1 = Image.open("./Sec.17 206 Images With Python/pikachu.jpg")

print ("img1: ", img1)
print ("img1.format: ", img1.format)
print ("img1.size: ", img1.size)
print ("img1.mode: ", img1.mode)

img1.show()

filtered_img2=img1.filter(ImageFilter.BLUR)
filtered_img2.show()
filtered_img2.save("./Sec.17 206 Images With Python/pikachu_blur.png", 'png')

filtered_img3=img1.filter(ImageFilter.SMOOTH)
filtered_img3.show()
filtered_img3.save("./Sec.17 206 Images With Python/pikachu_smooth.png", 'png')

filtered_img4=img1.filter(ImageFilter.SHARPEN)
filtered_img4.show()
filtered_img4.save("./Sec.17 206 Images With Python/pikachu_sharpen.png", 'png')

filtered_img5=img1.convert('L')   # Will convert in grey
filtered_img5.show()
filtered_img5.save("./Sec.17 206 Images With Python/pikachu_grey.png", 'png')

filtered_img6=img1.convert('L')   # Will convert in grey
filtered_img6.show()
filtered_img6.save("./Sec.17 206 Images With Python/pikachu_grey.png", 'png')
