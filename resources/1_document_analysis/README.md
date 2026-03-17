# Document Analysis Resources

The two folders `Iberian_aquitanian_notation` and `Iberian_square_notation` contain the same file structure:

- `A_Training` folder:
  - `models` folder: Models trained to classify the pixels as belonging to one of the following layers.

    | Notation | Background | Music symbols | Staff lines | Text    | Selected Region |
    | -------- | ---------- | ------------- | ----------- | ------- | --------------- |
    | Square   | Layer 0    | Layer 1       | Layer 2     | Layer 3 | Selected regions (Layer 4) |
    | Aquitanian | Layer 0  | Layer 1       |             | Layer 2 | Selected regions (Layer 3) |

    The models were trained suing the `Parchwise Analysis of Music Document, Training` job (also known as "Paco's Training" job for its author) and the data from the `pixel_ground_truth_data` folder.
    
  - `pixel_ground_truth_data` folder: The images and layers of said images that were used to train the pixel-classification models (see above). These layers were generated using `Pixel.js`.

- A `B_Classification_and_Postprocessing` folder: Contains the prediction of the pixel-classification models in other folios, plus the correction of those results.

  - In the case of Aquitanian notation, an extra layer is generated for the dry-point "music reference line" (which is Layer 2), resulting in the following layers:

    | Notation | Background | Music symbols | Reference Line | Text    | Selected Region |
    | -------- | ---------- | ------------- | -------------- | ------- | --------------- |
    | Aquitanian | Layer 0  | Layer 1       | Layer 2        | Layer 3 | Selected regions (Layer 4) |

      This extra layer is generated manually using Pixel, as it cannot be automatically detected by a pixel-classification model as it is drawn as a dry-point line instead of using ink. For other Aquitanian manuscripts where this line is actually drawn with ink, a model can be trained to detect the pixels belonging to said line.

  - In the case of square notation, some images had their full set of layers corrected (see folders that start with `Pixel_js-ZIP`) and others only had the music symbol layer corrected (see fodlers that start with `CorrOnlyMusicSymbolLayer_Pixel_js-ZIP`), as the music symbol layer is the only one that will serve to train models for symbol classification.
