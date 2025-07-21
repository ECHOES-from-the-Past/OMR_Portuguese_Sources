This folder contains the layers used for testing the work done on finding the middle staff line between two lyric lines. The layers belong to the following folios in the [Salamanca Missal](https://pemdatabase.eu/gallery-item/8771):
- Folio [008v Seq 001](https://pemdatabase.eu/media/8771/download?attachment)
- Folio [015v Seq 001](https://pemdatabase.eu/media/8784/download?attachment)
- Folio [018r Seq 001](https://pemdatabase.eu/media/8789/download?attachment)
- Folio [020r](https://pemdatabase.eu/media/8793/download?attachment)
- Folio [029v Seq 001](https://pemdatabase.eu/media/8812/download?attachment)
- Folio [043v Seq 001](https://pemdatabase.eu/media/8837/download?attachment)
- Folio [055v Seq 001](https://pemdatabase.eu/media/8864/download?attachment)

The `build_mei_file.py` can be used in a local version of Rodan for the Aquitanian workflow as part of `MEI Encoding` (would replace the original `build_mei_file.py`). It uses 5 staff lines (setting `@lines = 5` in `<staffDef>`) with the middle line being the original line, 2 ledger lines above, and 2 ledger lines below. It also updates the clef's line (by setting `@clef.line = 2` in `<staffDef>`) to properly align neumes to the staff. 

**Note:** If the `build_mei_file.py` is not used, the user will have to change these values manually. 
