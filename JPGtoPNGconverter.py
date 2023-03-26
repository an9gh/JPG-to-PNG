import sys
import os
from PIL import Image

# grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

# check is \new\ exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    img = Image.open(f'{path}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{directory}{clean_name}.png', 'png')
    print('all done!')

# loop through pokedex,
# convert images to png
# save to the new folder
