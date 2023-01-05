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

This is just a simple example of how to use the naive Bayes theorem for classification in Python using the sklearn library. There are many other ways 
to use the naive Bayes theorem, and many other libraries and tools available for implementing it in Python.
'''
