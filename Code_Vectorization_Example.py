"""
Vectorizing code using NumPy
"""

import numpy as np

# Create a random array of integers
arr = np.random.randint(0, 10, size=100)

# Use a for loop to square each element of the array
for i in range(arr.size):
    arr[i] = arr[i] ** 2

# Print the squared array
print(arr)

# Vectorize the code using NumPy's square function
arr = np.square(arr)

# Print the squared array
print(arr)
