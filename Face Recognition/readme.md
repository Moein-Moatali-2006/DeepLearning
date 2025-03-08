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
|Train :|0.9955|0.0219|
|Validation :|0.8780|1.1940|

- Three tested images, all of which were correctly predicted.

!["output"]()

## Run and test :

```
pip install -r requirements.txt
```
Your image dimensions must be 1024×1024.

