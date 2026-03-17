# Square Notation:

## Training Part (`A_Training` folder)

The models in the [`A_training/models`](./A_training/models) folder were trained only for the classification of `Music Symbols`, `Staff Lines`, and `Text`, since the staff layer is actually not drawn in ink in the manuscript (but rather it is made by a scratching the parchment with something pointy). The groundtruth data to generate these models are the files in the [`A_Training/pixel_ground_truth_data`](./A_training/pixel_ground_truth_data) folder: 

- `Image.png`
- `rgba PNG - Layer 0 (Background).png`
- `rgba PNG - Layer 1.png`, the music symbol layer
- `rgba PNG - Layer 2.png`, the staff lines layer
- `rgba PNG - Layer 3.png`, the text layer
- `rgba PNG - Selected regions.png`

To use these files as training data for the `Training model for Parchwise Analysis of Music Document, Training` job (also known as "Paco's Training" job for its author), one has to compress together into a ZIP file named `Pixel_js - ZIP.zip`. 


## Classification Part (`B_Classification_and_Postprocessing` folder)

This folder contains the results of applying the previous models to the classification of other folios, and the correction of said results. 
Some of the images' layers were fully corrected (see folders starting with `Pixel_js-ZIP`), 
while for others **only** the music symbol layer was corrected (see folders starting with `CorrOnlyMusiSymbolLayer_Pixel_js-ZIP`) as this is the layer used to train the Interactive Classifier (IC) used for symbol recognition.
