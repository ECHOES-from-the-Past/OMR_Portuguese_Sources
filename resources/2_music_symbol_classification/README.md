# Music Symbol Classification Resources

For automatically classifying the glyphs of a new image, one only needs to use the `Interactive Classifier - GameraXML - Training Data.xml` file. For starting a page from scratch, one does not need any file to star with, but using the "class names" text file (called `Interactive Classifier - Plain Text - Class Names.txt`) can be useful to have all the class names loaded in the Interactive Classifier job of Rodan. Moreover, these class names match the `classification` column of the MEI Mapping CSV table used later in the workflow (in the `MEI Encoding` job) to map these classes of symbols into their correct MEI encoding.[^1]

The file `Interactive Classifier - GameraXML - Classified Glyphs.xml` contains the classified glyphs of a given image:
- In the case of the file for _Iberian square notation_, the file contains the classified glyphs belonging to the [image of the opening of the 144-145 pages](/resources/1_document_analysis/Iberian_square_notation/pixel_ground_truth_data/Image.png) in the [P-BRs Ms. 034](https://pemdatabase.eu/source/47612). 
- In the case of the file for _Iberian Aquitanian notation_, the file contains the classified glyphs belonging to the [image of 035r](/resources/1_document_analysis/Iberian_aquitanian_notation/pixel_ground_truth_data/Image.png) in the [Salamanca Missal, E-SAu Ms. 2637 (ACm)](https://pemdatabase.eu/source/48357).

[^1]: Find the CSV tables in the [`4_mei_encoding`](./resources/4_mei_encoding/) folder for the two types of notations.
