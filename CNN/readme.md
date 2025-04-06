# CNN

## Model Comparison on CIFAR-100, CIFAR-10, MNIST, and Fashion-MNIST
I trained the CIFAR-100, CIFAR-10, MNIST, and Fashion-MNIST datasets using TensorFlow and Keras with two different approaches:

1. **MLP (Multilayer Perceptron)**
2. **CNN + MLP (Convolutional Neural Network + MLP)**  

The results were presented in a table for comparison.  

### Key Points of Analysis:
- **Accuracy Comparison:** How much improvement does CNN+MLP provide over MLP, especially for complex datasets like CIFAR-10 and CIFAR-100?  
- **Overfitting:** Does MLP overfit more on complex datasets?  
- **Convergence Speed:** Which model reached higher accuracy faster?  
- **Resource Consumption:** Comparison of memory and GPU/CPU usage.  
- **Effect of Additional Layers:** How does adding more layers impact CNN+MLP performance?  

### Results:

| Dataset        | MLP (Machine Learning) | CNN + MLP (Deep Learning) |
|---------------|----------------------|-------------------------|
| MNIST        | 97%                  | 98%                     |
| Fashion MNIST | 86%                  | 86%                     |
| CIFAR-10     | 10%                   | 69%                     |
| CIFAR-100    | 1%                    | 32%                     |



## You can see some information about datasets:
- [MNIST](https://keras.io/api/datasets/mnist/)
- [Fashion MNIST](https://keras.io/api/datasets/fashion_mnist/)
- [CIFAR-10](https://keras.io/api/datasets/cifar10/)
- [CIFAR-100](https://keras.io/api/datasets/cifar100/)

