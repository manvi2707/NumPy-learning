import numpy as np

# Broadcasting allows NumPy to perform operations on array
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape

# The dimensions have the same size
# OR
# One of the dimensions has size of 1

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1],
                   [2],
                   [3],
                   [4]])

print(array1.shape)
print(array2.shape) # here dimensions are (1,4) and (4,1) but they are compatible as if one is 4 other is 1. 
# dimensions must either be same or one is 1.
# dimensions (2,4) and (4,1) will not be compatible and will throw error.
# dimensions (4,1) and (4,1) are compatible

print(array1 * array2)

arr1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
arr2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)