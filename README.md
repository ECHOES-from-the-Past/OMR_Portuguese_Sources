# OMR_Portuguese_Sources

Resources for the Optical Music Recognition (OMR) for Aquitanian and Iberian square notations as found in the manuscripts:
- [Salamanca Missal, E-SAu Ms. 2637 (ACm)](https://pemdatabase.eu/source/48357) in _Aquitanian notation, Portuguese style_
- [P-BRs Ms. 034](https://pemdatabase.eu/source/47612) in _Iberian square notation_

The resources for each of the four steps of an OMR workflow can be found in each in the following folders:
- **Document Analysis** in [`resources/1_document_analysis/`](https://github.com/ECHOES-from-the-Past/OMR_Portuguese_Sources/tree/main/resources/1_document_analysis)
- **Music Symbol Classification** in [`resources/2_music_symbol_classification/`](https://github.com/ECHOES-from-the-Past/OMR_Portuguese_Sources/tree/main/resources/2_music_symbol_classification)
- **Music Reconstruction** in the folder for processing of the text in [`resources/3_text_alignment/`](https://github.com/ECHOES-from-the-Past/OMR_Portuguese_Sources/tree/main/resources/3_text_alignment)
- **Music Encoding** in [`resources/4_mei_encoding/`](https://github.com/ECHOES-from-the-Past/OMR_Portuguese_Sources/tree/main/resources/4_mei_encoding)

## The Case of Iberian Aquitanian and Square notations

### Iberian Square Notation
Square notation in this Iberian source shows some peculiarities:
1. Extra symbols. For example, the lengüeta, which implies a repeated note and looks like:

   <img src="./resources/4_mei_encoding/_images/square/SQlenguetaup.jpg" width="56p" alt="LenguetaUp"/>  ![LenguetaDown](./resources/4_mei_encoding/_images/square/lenguetadown.png)
     
2. Symbols that are used with a different functionality. For example, the following symbol that looks like a plica but it is not representing a liquescent, but a repeated note.

   ![TwoTailsDown](./resources/4_mei_encoding/_images/square/twostemsdown.png)

### Portuguese-Style Aquitanian Notation
In early Iberian Aquitanian sources, like the Salamanca Missal, there is a music reference line and no clefs. In the Salamanca Missal, in particular, the music reference is a dry-point line (other sources might show this line in red or black ink).

