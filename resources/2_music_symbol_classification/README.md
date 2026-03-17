# Music Symbol Classification Resources

We generated resources for the music classification step of the OMR workflow. This step is condcuted by the Interactive Classifier (IC) job in Rodan. We train the IC in a few pages incrementally. The folders in each notation style show the different iterations of the training of the IC (in each iteration, a new image was given to the IC and its glyphs were classified throughly to increment the training data).

For automatically classifying the glyphs of a new image, one only needs to use the `Interactive Classifier - GameraXML - Training Data.xml` file. For starting a page from scratch, one does not need any file to start with, but using the "class names" text file (called `Interactive Classifier - Plain Text - Class Names.txt`) can be useful to have all the class names loaded in the Interactive Classifier job of Rodan. Moreover, these class names match the `classification` column of the MEI Mapping CSV table used later in the workflow (in the `MEI Encoding` job) to map these classes of symbols into their correct MEI encoding.[^1]

The file `Interactive Classifier - GameraXML - Classified Glyphs.xml` contains the classified glyphs of a given image.

### Important notes:
* In each of the folders inside each notation type, the `Column splitting` job was used on the image layers prior to them being further processed. This is, the IC received the music symbol layer already splitted into two columns.
* For the `Interactive Classifier - GameraXML - Classified Glyphs.xml` to be useful for processing the results in the next jobs (`Heuristic Pitch Finding` and `MEI Encoding`) successfully, the music symbol layer that eventually gets into the IC, **needs to have been splitted in columns** (just like the other layers would be when reaching these jobs). This is what we did as can be seen in any of the iteration folders.
* **This is not necessary** if one uses the IC just **for generating the training data** (`Interactive Classifier - GameraXML - Training Data.xml`) **or class names** (`Interactive Classifier - Plain Text - Class Names.txt`). They can be generated in un-splitted data and then be used in splitted-column data without any issues.

[^1]: Find the CSV tables in the [`4_mei_encoding`](../4_mei_encoding) folder for the two types of notations.
