# Workflows

## BGRemoval:

Use the `Background Removal` job to obtain a foreground layer---which would include all the foreground pixels 
belonging to music symbols, staff lines, and text---and then use Pixel to cut and past the elements of this layer 
into the appropriate music symbols, staff lines, and text layers.
The foreground layer exported will be in the output port `RGBA PNG image` from the `Background Removal` job, 
which we can connect to one of the input ports of the layers in Pixel (e.g., music symbol layer). 
The other input layers of Pixel (e.g., staff lines and text) should be connected to the (optional) 
`Empty Layer` output port of `Background Removal`. Then one can use the cut & paste tools from Pixel to move the pixels 
to the appropriate layer.

We always use the `PNG (RGB)` job to process the image at the very beginning.

![BGRemoval](https://github.com/user-attachments/assets/0ca32f76-3431-4726-aa31-3bace4054ebc)
