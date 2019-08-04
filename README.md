# PortraitPainting2RealImage

We propose a new approach for generating realistic images out of portrait painting.
Our idea is:
1)extract the edges out of an image - using canny algorithm (without the edge-linking step)
2)create negative out of the picture
2)run our pix2pix with perceptual loss pretrained model 
# Instructions
- Clone this repo:
```bash
git clone https://github.com/PetruninAlex/PortraitPainting2RealImage.git
cd PortraitPainting2RealImage
```
- Test our model:
on one image:
```bash
TODO
```
on a whole folder:
```bash
TODO
```

- Prepare data set for training:
If you have a data set of real portraits you can run this script.
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


