import os
import sys

horizontal_patches = int(sys.argv[1])
vertical_patches = int(sys.argv[2])
patch_size = sys.argv[3]
checkpoints_path = sys.argv[4]
input_path = sys.argv[5]
mask_path = sys.argv[6]
output_path = sys.argv[7]

for i in range(horizontal_patches):
    for j in range(vertical_patches):
        os.system("python patch_generator.py " + str(patch_size) + " " + str(patch_size * j) + " " + str(patch_size * i))
        os.system("python test.py " +
                  "--checkpoints " + str(checkpoints_path) + " " +
                  "--input " + str(input_path) + " " +
                  "--mask " + str(mask_path) + " " +
                  "--output " + str(output_path))
