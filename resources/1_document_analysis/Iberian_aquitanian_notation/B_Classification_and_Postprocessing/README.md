# Note: 
As indicated in the [Document Analysis README](../README.md), this folder contains the prediction of the pixel-classification models for a few folios, plus the correction of those results.
In the case of **Aquitanian notation**, an extra layer is generated for the dry-point "music reference line" (Layer 2), resulting in the following layers:

| Notation | Background | Music symbols | Reference Line | Text    | Selected Region |
| -------- | ---------- | ------------- | -------------- | ------- | --------------- |
| Aquitanian | Layer 0  | Layer 1       | Layer 2        | Layer 3 | Selected regions (Layer 4) |

This extra layer is generated manually using Pixel, as it cannot be automatically detected by a pixel-classification model as it is drawn as a dry-point line instead of using ink. For other Aquitanian manuscripts where this line is actually drawn with ink, a model can be trained to detect the pixels belonging to said line.
