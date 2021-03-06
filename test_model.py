import argparse
import os
import warnings

import scipy
from PIL import Image

from extract_edges import extract_edges

warnings.filterwarnings("ignore", category=DeprecationWarning)

parser = argparse.ArgumentParser(description='Receiving directory for test')
parser.add_argument("--dir", type=str, default=None)
args = parser.parse_args()

dir = args.dir
list_of_files = os.listdir(dir)
number_of_images = len(list_of_files)

for file in list_of_files:
    img_path = dir + file
    img = Image.open(img_path).resize((224, 224))
    edges = extract_edges(img)
    scipy.misc.imsave("./tmp/" + file, edges)

os.system(
    "python test.py --dataroot ./tmp --name best_model --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch --num_test " + str(
        number_of_images))

for file in list_of_files:
    os.system("rm ./tmp/" + file)
