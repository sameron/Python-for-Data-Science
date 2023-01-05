# Naive Bayes is implemented using the sklearn library

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load the iris dataset
X, y = load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian naive Bayes classifier
classifier = GaussianNB()

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test)

# Calculate the accuracy of the predictions
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy:.2f}")

'''
This program uses the load_iris function to load the iris dataset, and the train_test_split function to split the data into training and test sets.

It then creates a Gaussian naive Bayes classifier using the GaussianNB class, trains the classifier on the training data using the fit method, and 
makes predictions on the test data using the predict method.

Finally, it calculates the accuracy of the predictions by comparing them to the true labels (y_test) and printing the mean accuracy.

The naive Bayes algorithm is a simple and effective technique for probabilistic classification. It is based on the idea of applying Bayes' theorem to classify objects based on the features that describe them.

Some common use cases for the naive Bayes algorithm include:
  Text classification: The naive Bayes algorithm is often used for text classification tasks such as spam detection, sentiment analysis, and topic classification.
  Classification of discrete features: The naive Bayes algorithm is particularly well-suited for classification tasks with discrete features (e.g., boolean, categorical, or count data).
  High-dimensional data: The naive Bayes algorithm can handle high-dimensional data efficiently, making it a good choice for problems with a large number of features.
  Fast training and prediction: The naive Bayes algorithm is fast to train and predict, making it a good choice for problems where speed is important.
  
Overall, the naive Bayes algorithm is a simple and effective tool for probabilistic classification that is well-suited for a wide range of problems. It is particularly useful for classification tasks with discrete features, high-dimensional data, and/or a need for fast training and prediction.
'''
