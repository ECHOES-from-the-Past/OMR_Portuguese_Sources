# Models Training Data
These models were trained only for the classification of Music Symbols and Text, since the staff layer is actually not drawn in ink in the manuscript (but rather it is made by a scratching the parchment with something pointy). Therefore, the training data consists on everything that is not exactly what it is in the [pixel_ground_truth_data](../pixel_ground_truth_data) folder because: 

1. `Layer 2` (originally, the staff line) is substituted by `Layer 3` (originally, the text)
2. `Layer 0` (the background) is different as it doesn't exclude the scratched parchment of the music reference line. So, we are providing here the appropriate ground truth data for these models
