# Workflows

## BGRemoval Workflow

**Summary:** This workflow allows to save time in the Pixel classification part of the OMR.

It uses the `Background Removal` job to obtain a foreground layer---which would include all the foreground pixels 
belonging to music symbols, staff lines, text, images, etc.---and then use Pixel to cut and paste the elements of this layer into the appropriate music symbols, staff lines, and text layers.

The foreground layer obtained by the `Background Removal` job is given by its output port `RGBA PNG image`. This output port can be connected to one of the layer (optional) input ports in Pixel (e.g., music symbol layer). 
The remaining input layers of Pixel (e.g., staff lines and text) should be connected to the (optional) 
`Empty Layer` output port from the `Background Removal` job. Then one can use the cut & paste tools from Pixel to move the pixels from the foreground layer into the appropriate layer (e.g., cut them from the music symbol layer to paste them in the appropriate staff lines or text layers).

**Important note:** We always use the `PNG (RGB)` job to process the image at the very beginning.

### Workflow
![BGRemoval](./images/BGRemoval.png)

### Workflow annotated for ports
![BGRemoval - annotated](./images/BGRemoval%20-%20annotated.png)
