# Audio Classifier

In this project, voices of different individuals have been processed and prepared for training.
This project utilizes deep artificial neural network architectures built with TensorFlow and Keras.
To use the Telegram bots or the models themselves, please install the required libraries by running the 'requirements.txt' file.

```
pip install -r requirements.txt
```

## Train 

Friends:
|Data|Accuracy|Loss|
|----|--------|----|
|Train|93%|0.2067|
|Validation|97%|0.0963|


## Train singers

Singers( Hayedeh - Moein - Mohsen Chavoshi - Siavash Ghomayshi - Yas):
|Data|Accuracy|Loss|
|----|--------|----|
|Train|76%|0.5921|
|Validation|95%|0.1988|


## Make Dataset:
To create your own dataset, simply set the names of your directories accordingly, and then start the training process.

### My data:
[Dataset](https://drive.google.com/drive/folders/1ZljJR96bwZE624SD03K79XxDqmZn2oiE)


## Telegram BOT:
```
python bot.ipynb 
python bot_singers.ipynb
```
Set Models : \
voice_model.h5 ---> bot.ipynb
singers_model.h5 ---> bot_singers.ipynb

![image](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/Audio%20Classification/output_bot.jpg)