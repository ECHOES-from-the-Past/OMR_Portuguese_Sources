# Models Training Data
These models were trained only for the classification of `Music Symbols` and `Text`, since the staff layer is actually not drawn in ink in the manuscript (but rather it is made by a scratching the parchment with something pointy). The groundtruth data to generate these models are the files in the [`pixel_ground_truth_data`](./pixel_ground_truth_data) folder: 

- `Image.png`
- `rgba PNG - Layer 0 (Background).png`
- `rgba PNG - Layer 1.png`, the music symbol layer
- `rgba PNG - Layer 2.png`, the text layer
- `rgba PNG - Selected regions.png`

To use these files as training data for the `Training model for Parchwise Analysis of Music Document, Training` job (also known as "Paco's Training" job for its author), one has to compress together into a ZIP file named `Pixel_js - ZIP.zip`. 


The extra folder [`also_reference_line_layer`](./pixel_ground_truth_data/also_reference_line_layer) that can be found in this `pixel_ground_truth_data` directory has actually an extra layer for the scratched staff line:

- `Image.png`
- `rgba PNG - Layer 0 (Background).png`
- `rgba PNG - Layer 1.png`, the music symbol layer
- `rgba PNG - Layer 2.png`, the staff layer (the reference line for the music symbols, which is part of the ruled lines made by scratching the parchment)
- `rgba PNG - Layer 3.png`, the text layer
- `rgba PNG - Selected regions.png`

We cannot use the staff layer for training given that it is a scratch in the parchment rather thank an inked line. However, in most Aquitanian manuscripts, this line is actually drawn in red or black ink, so one should also label it to use it for pixel classification of the document.
