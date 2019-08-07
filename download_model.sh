#!/bin/bash

mkdir tmp
mkdir checkpoints
cd checkpoints
gdown https://drive.google.com/uc?id=1wSVL-jXauT-4xYb2_UQ6ZPwZ4j98_NGC
unzip best_model.zip
rm best_model.zip
cd ..
