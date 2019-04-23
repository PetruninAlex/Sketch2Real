import sys

from PIL import Image

patch_size = int(sys.argv[1])
horizontal_indentation = int(sys.argv[2])
vertical_indentation = int(sys.argv[3])
path = str(sys.argv[4])

img = Image.new('RGB', (256, 256), color='black')
pixdata = img.load()
for i in range(patch_size):
    for j in range(patch_size):
        pixdata[i + horizontal_indentation, j + vertical_indentation] = (255, 255, 255)
img.save(path)
