import sys
import os
from os import path
from PIL import Image, ImageFilter
from PIL import Image
Actual_folder = sys.argv[1]
new_folder= sys.argv[2]
print(Actual_folder,new_folder)
if path.exists(new_folder) and path.isdir(new_folder):
    pass
else:
    os.mkdir(new_folder)
for img in os.listdir(Actual_folder):
    cleanname=path.splitext(img)[0]
    img1=Image.open(f'{Actual_folder}{img}')
    img1.save(f'{new_folder}{cleanname}.png','png')
    print("done")