## OCR Pipeline (example:)
- Image => Text detection => character segmentation => character recognition

## sliding Windows.
- Text detection
  - aspect ratio.
  - step-size/stride parameter
  - larger patch size
  - expansion
- Character segmentation
  - sliding windows to find the separation region.

## Getting into lots of data.
- firstly: have a  low bias algorithm, then: train it on a large dataset.
- sythesize random font/voice and random background. 
  - add distortion/warping, different aspect ratio.
- example: speech recognition

- do I have a low bias classifier? learning curve (there are other curves, x: d, x: lambda, etc.)
  - add and engineer features to make sure that you have one
- how much effort to put to get 10* more data?

## how to optimize pipeline?
- allocate how much resource on each box?

- accuracy
  - suppose first box is working perfectly, what would be the accuracy?
  - suppose first and second are working perfectly, what would be the accuracy?
  - ...
  - calculate the upside potential (how much would you possibly gain, if ... were perfect.)
  
