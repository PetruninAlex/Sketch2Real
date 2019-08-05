# PortraitPainting2RealImage

We propose a new approach for generating realistic images out of portrait painting.
Our idea is:
1)extract the edges out of an image - using canny algorithm (without the edge-linking step)
2)create negative out of the picture
2)run our pix2pix with perceptual loss pretrained model 
# Instructions
## Installation
- Clone this repo:
```bash
git clone https://github.com/PetruninAlex/PortraitPainting2RealImage.git
cd PortraitPainting2RealImage
```
- Download our model from google drive (need gdown): 
```bash
pip install gdown
bash download_model.sh
```

## Test our model
```bash
python test.py --dataroot /path/To/Test/Folder --name TODO --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch
```
## Train your own model
- Prepare your data set for training:
```bash
TODO
```
- Train a model:
```bash
python train.py --dataroot /path/To/Data --name your_name_to_model --model pix2pix --direction BtoA
```
- Test the model:
```bash
python test.py --dataroot /path/To/Data --name your_name_to_model --model pix2pix --direction BtoA
```


