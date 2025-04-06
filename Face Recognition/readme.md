# Face Recognition

In this project, the faces of several famous individuals in Iran have been processed, and you can identify them using their test images.

## Used Libraries:
- TensorFlow 
- Scikit-Learn
- DeepFace
- Numpy
- Pandas 
- Matplotlib.pyplot 
- OpenCV
- Ast

## Algorithm :
First, I preprocessed the images to remove potential noise. Then, I created a dataset from the preprocessed images. Using DeepFace and a multilayer neural network, I built a model to predict individuals' faces. Our processing method was generally classification.

|Data|Accuracy|Loss|
|----|--------|----|
|Train :|0.9010|0.3660|
|Validation :|0.8750|0.5269|

- Three tested images, all of which were correctly predicted.

!["output"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/Face%20Recognition/output.png)

## Run and test :

```
pip install -r requirements.txt
```
Your image dimensions must be 1024×1024.

