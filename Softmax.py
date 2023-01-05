"""
This program defines a matrix of input data X, a matrix of weights W, and a vector of biases b. It then calculates the dot product of the input
data and the weights, and applies the softmax function to the result. The softmax function converts the dot product into a probability distribution,
 where each element represents the probability of a given input data sample belonging to a particular class.

In this example, the input data consists of three samples with three features each, and the weights and biases are also three-dimensional. The dot
product is therefore a 3x3 matrix, and the softmax function is applied to each row of the matrix to produce a 3x3 probability matrix.

You can modify this program to fit your specific machine learning scenario by changing the shape and values of the input data, weights, and biases.
You can also use additional features and classes by increasing the dimensions of the matrices and vectors. Consult the Numpy documentation for more
information on matrix operations and the softmax function.
"""

import numpy as np

# define the input data
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# define the weights
W = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# define the biases
b = np.array([1, 2, 3])

# calculate the dot product of the input data and the weights
z = np.dot(X, W) + b

# apply the softmax function to the dot product
probabilities = np.exp(z) / np.sum(np.exp(z), axis=1, keepdims=True)

# print the probabilities
print(probabilities)

