import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


# Generate the data
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the training and test sets
print(f"X_train.shape: {X_train.shape}")
print(f"X_test.shape: {X_test.shape}")
print(f"y_train.shape: {y_train.shape}")
print(f"y_test.shape: {y_test.shape}")

'''
This program uses the make_classification function to generate a synthetic dataset with 1000 samples, 10 features, and 2 classes. 
The train_test_split function is then used to split the data into training and test sets, with a test set size of 20%.

The resulting training and test sets are printed to the console along with their shapes.

This is just a simple example of how to generate test data for a machine learning task in Python using the sklearn library. 
There are many other ways to generate test data, depending on the specific requirements of your machine learning task.
'''