# Emoji_Text_Classification

## Labels:
!["labels"](https://github.com/Moein-Moatali-2006/DeepLearning/blob/main/Text_Classification/labels.png)

## result with different dimensions(50d,100d,200d,300d)

|feature vector dimensions|Train loss|Train accuracy|Test loss|Test accuracy|Inference Time|
|-------------------------|----------|--------------|---------|-------------|--------------|
|50d|0.1332|0.9647|0.3029|0.8185|138ms|
|100d|0.0339|0.9962|0.4719|0.8080|177ms|
|200d|0.0070|1.0000|0.4825|0.8423|180ms|
|300d|0.0030|1.0000|0.4492|0.8185|188ms|

## How to change dimensions:
```python 
model_50 = EmojiTextClassifier()
X_train_raw, Y_train, X_test_raw, Y_test = model_50.load_dataset("dataset/train.csv", "dataset/test.csv")
model_50.load_feature_vectors(name="glove.6B.50d.txt") # change file name

X_train = model_50.vectorize_dataset(X_train_raw,D=50) # change D for dimension
X_test = model_50.vectorize_dataset(X_test_raw,D=50) # change D for dimension

model_50.train(X_train, Y_train, epochs=250)
model_50.test(X_test, Y_test)

result_test = model_50.predict("I love programming",D=50) # change D for dimension
print("predict:",result_test)
```