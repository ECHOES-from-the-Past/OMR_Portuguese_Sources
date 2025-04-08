# Music Symbol Classification Resources

For automatically classifying the glyphs of a new image, one only needs to use the `Interactive Classifier - GameraXML - Training Data.xml` file. For starting a page from scratch, one does not need any file to star with, but using the "class names" text file (called `Interactive Classifier - Plain Text - Class Names.txt`) can be useful to have all the class names loaded in the Interactive Classifier job of Rodan. Moreover, these class names match the `classification` column of the MEI Mapping CSV table used later in the workflow (in the `MEI Encoding` job) to map these classes of symbols into their correct MEI encoding.[^1]

The file `Interactive Classifier - GameraXML - Classified Glyphs.xml` contains the classified glyphs of a given image:
- In the case of the file for _Iberian square notation_, the file contains the classified glyphs belonging to the [image of the opening of the 144-145 pages](/resources/1_document_analysis/Iberian_square_notation/pixel_ground_truth_data/Image.png) in the [P-BRs Ms. 034](https://pemdatabase.eu/source/47612). 
- In the case of the file for _Iberian Aquitanian notation_, the file contains the classified glyphs belonging to the [image of 035r](/resources/1_document_analysis/Iberian_aquitanian_notation/pixel_ground_truth_data/Image.png) in the [Salamanca Missal, E-SAu Ms. 2637 (ACm)](https://pemdatabase.eu/source/48357).

**Important notes:**
* For the `Interactive Classifier - GameraXML - Classified Glyphs.xml` to be useful for processing the results in the next jobs (`Heuristic Pitch Finding` and `MEI Encoding`) successfully, the music symbol layer that eventually gets into the IC, needs to have been splitted in columns (just like the other layers would be when reaching these jobs).
* This is not necessary if one uses the IC just for generating the training data (`Interactive Classifier - GameraXML - Training Data.xml`) or class names (`Interactive Classifier - Plain Text - Class Names.txt`). They can be generated in un-splitted data and then be used in splitted-column data without any issues.

[^1]: Find the CSV tables in the [`4_mei_encoding`](../4_mei_encoding) folder for the two types of notations.
