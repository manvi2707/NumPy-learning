import numpy as np

# python is very slow language. that's where numpy comes in. it helps us write python codes and works 10x faster.

arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))

# multiply all elements with 2
array2 = arr*2
print(array2)


array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]]) # 2D array

array3D = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]]) # 3D array => Array of 2D array

# number of columns must be same in each row. 
print(array3D.ndim)
print(array3D.shape) # (depth, rows, columns)

# To access element in array
print(array3D[0,0,0]) # usually in python we use chain indexing but it is slower => array3D[0][0][0]

word = array3D[0,1,2] + array3D[2,0,2] + array3D[0,0,2] + array3D[1,0,1]
print(word)

# -------> SLICING <--------

arrayy = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8,],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array[start:end:step] ; steps and indexs can be negative like in python
# row selection
print(arrayy[0:4:2]) 

# column selection
print(arrayy[:,0:3:2]) # here : means selecting every row