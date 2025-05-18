# License Plate (Detection - Recognition - Identification - Verification)

## Installing the required libraries:
```
pip install -r requirements.txt
```
!["image"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/License%20Plate%20PipeLine/io/input/image_test.jpg)
!["image"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/License%20Plate%20PipeLine/io/output/plate_image_result_0.jpg)

## predict your plates
Please first download the trained weights from the link below and place them in the weights folder.
[pre-trained](https://drive.google.com/drive/folders/1r1nRO4QSM9jbH0II5h_iWN2D_MFXlTo7)

```
python identification.py
```
Arguments you can modify:
```
--input_image path
--threshold 0-1
```

!["image"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/License%20Plate%20PipeLine/io/output/example.png)

## Verification Plate
We have a database containing a collection of license plates.
First, add your own plates to the database, then use the system.

```
python verification.py
```

!["image"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/License%20Plate%20PipeLine/io/output/example_1.png)