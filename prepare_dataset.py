import argparse
import os
import warnings

import scipy
from PIL import Image

from extract_edges import extract_edges

warnings.filterwarnings("ignore", category=DeprecationWarning)

parser = argparse.ArgumentParser(description='Receiving directories info for data preparation')
parser.add_argument("--contentDir", type=str, default=None)
parser.add_argument("--destDir", type=str, default=None)
parser.add_argument("--trainRatio", type=float, default=0.7)
parser.add_argument("--testRatio", type=float, default=0.15)
parser.add_argument("--valRatio", type=float, default=0.15)
args = parser.parse_args()

if args.contentDir == None or args.destDir == None:
    print("Please put values for args --contentDir --destDir")
    exit(0)

if args.trainRatio + args.testRatio + args.valRatio != 1:
    print("The sum of ratios should be 1")
    exit(0)

content_dir = args.contentDir
dest_dir = args.destDir
list_of_files = os.listdir(content_dir)
list_of_files.sort()
number_of_files = len(list_of_files)

a_train = dest_dir + "A/train/"
a_test = dest_dir + "A/test/"
a_val = dest_dir + "A/val/"

b_train = dest_dir + "B/train/"
b_test = dest_dir + "B/test/"
b_val = dest_dir + "B/val/"

os.system("mkdir " + dest_dir + "A/")
os.system("mkdir " + a_train)
os.system("mkdir " + a_test)
os.system("mkdir " + a_val)

os.system("mkdir " + dest_dir + "B/")
os.system("mkdir " + b_train)
os.system("mkdir " + b_test)
os.system("mkdir " + b_val)

counter_train = args.trainRatio * number_of_files
counter_test = args.testRatio * number_of_files
counter_val = args.valRatio * number_of_files

for file in list_of_files:
    img_path = args.contentDir + file
    img = Image.open(img_path).resize((224, 224))
    edges = extract_edges(img)

    if counter_train > 0:
        img.save(a_train + file)
        scipy.misc.imsave(b_train + file, edges)
        counter_train -= 1
        continue

    if counter_val > 0:
        img.save(a_val + file)
        scipy.misc.imsave(b_val + file, edges)
        counter_val -= 1
        continue

    if counter_test > 0:
        img.save(a_test + file)
        scipy.misc.imsave(b_test + file, edges)
        counter_test -= 1
        continue

os.system(
    "python datasets/combine_A_and_B.py --fold_A " + dest_dir + "A/ " + "--fold_B " + dest_dir + "B/ " + "--fold_AB " + dest_dir)
