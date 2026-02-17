import numpy as np

# Scalar arithemetic

array = np.array([1.01, 2.5, 3.99])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

# Vectorized math functions

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array)) # to always round down
print(np.ceil(array)) # to always round up
print(np.pi)


# Element-wise arithemetic
# apply operations between single elements between 2 arrays

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)


# Comparison Operators
scores = np.array([91, 55, 100, 73, 82, 64])

print(scores > 60)

scores[scores < 60] = 0
print(scores)
