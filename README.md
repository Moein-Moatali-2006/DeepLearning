# DeepLearning (Tensorflow)

## 7.1 Introduction to Deep Learning
* Face Recognition

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/Face%20Recognition/output.png)

## 7.2 Hello CNN

| Dataset        | MLP (Machine Learning) | CNN + MLP (Deep Learning) |
|---------------|----------------------|-------------------------|
| MNIST        | 97%                  | 98%                     |
| Fashion MNIST | 86%                  | 86%                     |
| CIFAR-10     | 10%                   | 69%                     |
| CIFAR-100    | 1%                    | 32%                     |


You can see some information about datasets:
- [MNIST](https://keras.io/api/datasets/mnist/)
- [Fashion MNIST](https://keras.io/api/datasets/fashion_mnist/)
- [CIFAR-10](https://keras.io/api/datasets/cifar10/)
- [CIFAR-100](https://keras.io/api/datasets/cifar100/)


## 7.3 Custom Dataset CNN
* 5 Animal Detection
* 17 Flowers Detection whit data `augmentation`

|Dataset|Accuracy|Loss|
|-------|-----|----------|
|train|82%|0.4628|
|validation|62%|1.1029|

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/Custom%20Dataset%20CNN/5%20Animals/images/confusian_mx.png)


![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/Custom%20Dataset%20CNN/Flowers/output/whit_augmentation.png)
![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/Custom%20Dataset%20CNN/Flowers/output/result.png)


## 7.4 Transfer Learning
* 7-7 faces
[dataset](https://drive.google.com/drive/folders/1WGSotRtFPYGuxPEGkWWRsBPlVXFSvl7p?usp=sharing)

* [Akhund and Human Detection](https://drive.google.com/drive/folders1awNU2wbo6owr3Pfyy8KIy70T5sdi41VD)
* [wandb](https://wandb.ai/)

|Algorithm|Accuracy|Loss|
|---------|--------|----|
|Train|0.9935|0.0194|
|Validation|0.8667|2.6953|

|Algorithm|Accuracy|Loss|
|---------|--------|----|
|CNN |70%|1.18|
|Transfer Learning CNN |91%|0.27|


## 7.5 CNN Regression
* Kaggle
* Age Prediction
* Home Prices Prediction 

## 7.6 Object Detection
* YOLO
* Persian License Plate Recognition

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/YOLO/test1.png)
![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/YOLO/test2.png)


## 7.7 OCR (Optical Character Recognition)
* DTRB
* easyOCR
* Deep Text Recognition Benchmark

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/OCR/EasyOCR/output_tests/text_en.png)
![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/OCR/EasyOCR/output_tests/latin_plate.png)
![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/OCR/EasyOCR/output_tests/irani_plate.png)

## PipeLine 
* License Plate Detection
* License Plate Recognition
* License Plate Identification
* License Plate Verification

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/License%20Plate%20PipeLine/io/input/image_test.jpg)

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/License%20Plate%20PipeLine/io/output/plate_image_result_0.jpg)

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/License%20Plate%20PipeLine/io/output/example.png)

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/License%20Plate%20PipeLine/io/output/example_1.png)

## 7.9 Audio Classification
* Identify sounds in audio clips
* Make Audio Dataset (using PyDub)
* Fit Model on Dataset (using TensorFlow)
* Predict Persian Singers 🎙🇮🇷  (using spleeter)

#### Train 

Friends:
|Data|Accuracy|Loss|
|----|--------|----|
|Train|93%|0.2067|
|Validation|97%|0.0963|


#### Train singers

Singers( Hayedeh - Moein - Mohsen Chavoshi - Siavash Ghomayshi - Yas):
|Data|Accuracy|Loss|
|----|--------|----|
|Train|76%|0.5921|
|Validation|95%|0.1988|


## 7.10 Face Recognition
* Face Verification
* Face Identification
* Face ID

|Data|Accuracy|Loss|
|----|--------|----|
|Train :|0.9010|0.3660|
|Validation :|0.8750|0.5269|

![image](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/Face%20Recognition/output.png)

## 7.11 Text Classification
* Emoji Text Classification

|feature vector dimensions|Train loss|Train accuracy|Test loss|Test accuracy|Inference Time|
|-------------------------|----------|--------------|---------|-------------|--------------|
|50d|0.1332|0.9647|0.3029|0.8185|138ms|
|100d|0.0339|0.9962|0.4719|0.8080|177ms|
|200d|0.0070|1.0000|0.4825|0.8423|180ms|
|300d|0.0030|1.0000|0.4492|0.8185|188ms|

## 7.12 TensorFlow For Experts
* Training various datasets using TensorFlow Expert Mode and evaluating the results (accuracy and loss)

|Dataset|Accuracy|Loss|
|-------|--------|----|
|Mnist|0.98|0.1|
|Cifar-10|0.66|1.2|
|Titanic|0.85|0.41|

## 7.13 GAN(Generative Adversarial Network)
* Mnist
* Fashion_Mnist
* CelebA

![gif](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/GAN/Mnist/dcgan.gif)
![gif](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/GAN/Fashion_Mnist/Fashion_Mnist.gif)
![gif](https://github.com/Moein-Moatali-2006/DeepLearning/raw/main/GAN/CelebA/output.png)
