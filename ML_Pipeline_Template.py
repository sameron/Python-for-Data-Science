import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
# from sklearn.externals import joblib

# Load the data
X = ...  # Load the feature data for the images
y = ...  # Load the labels for the images

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

# Fit the pipeline to the training data
pipeline.fit(X_train, y_train)

# Evaluate the pipeline on the test data
accuracy = pipeline.score(X_test, y_test)
print("Accuracy:", accuracy)

# Save the pipeline to a file
# joblib.dump(pipeline, 'pipeline.pkl')
