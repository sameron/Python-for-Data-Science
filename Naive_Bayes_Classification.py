
"""
Naive Bayes algorithm for classifying anomalies in an image is to extract features from the image, and then
 use the naive Bayes algorithm to classify the image based on those features.
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

# Load the iris dataset and extract the first two features
X, y = load_iris(return_X_y=True)
X = X[:, :2]

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

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

# Classify a new, anomalous sample
anomalous_sample = np.array([[-2, 2]])
anomalous_sample = scaler.transform(anomalous_sample)
prediction = classifier.predict(anomalous_sample)[0]
print(f"Prediction for anomalous sample: {prediction}")
