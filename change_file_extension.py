import os
import cv2
import glob
import sys

files = os.listdir(r"path")
for file in files:
    if file.endswith(".jpeg"):
    #if '.jpg' in file:
        newfile = os.path.join(r"path",file).replace('.jpeg', '.jpg')
        os.rename(os.path.join(r"path",file), newfile)

