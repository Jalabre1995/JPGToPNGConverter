#First thing we have to do is grap the files from the Pokiindex folder 
import sys
import os
from PIL import Image

#Grab the first and second argument 
image_folder = sys.argv[1]
output_folder = sys.argv[2]
#check is New/ exist if not create it
print(image_folder, output_folder)
# loop through Pokidex using the os module
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

#save to the new folder