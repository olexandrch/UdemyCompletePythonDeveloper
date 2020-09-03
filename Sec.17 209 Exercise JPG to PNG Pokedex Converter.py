#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 209. Exercise: JPG to PNG Pokedex Converter

# Program to convert JPG to PNG. Provide two arguments. 
# First - a folder with .jpg files.
# Second - a folder where .png will be stored.

import sys
import os
import pathlib
from PIL import Image

# grab the first and second arguments

if len(sys.argv) != 3:
    script_name = pathlib.Path(str(sys.argv[0]))
    print("Program to convert JPG to PNG. Provide two arguments." )
    print(f"Run it as: python '{script_name.name}' FolderWithJPG/ FolderToStorePNG/ ")
    os._exit(1)

inputFolder = pathlib.Path(str(sys.argv[1]))
outputFolder = pathlib.Path(str(sys.argv[2]))
# print(inputFolder)
# print(outputFolder)

# check if Input Folder exists.
if not inputFolder.exists():
    print(f'"{inputFolder}" folder does not exist. Provide existing folder. Exiting ...')
    os._exit(1)

# check if Second folder exists and create if not.
if not outputFolder.exists():
    print(f'"{outputFolder}" folder does not exist. Creating ...')
    outputFolder.mkdir()
else:
    print(f'{outputFolder} folder exist. Continuing ...')

# loop through the folder, convert .jpg to .png and save to the new folder

jpg_files = list(inputFolder.glob('*.jpg'))

for file in jpg_files:
    print (f'processing {file} file ...')
    img = Image.open(file)
    
    full_file_name = pathlib.PurePath(outputFolder, file.stem + ".png")
    # print (full_file_name)
    img.save(str(full_file_name), 'png')
  
