import numpy as np


# Select integer value 
rng = np.random.default_rng(seed=1)
print(rng.integers(low=1, high=101, size=(3,2)))

# Select floating value
np.random.seed(seed = 1)
print(np.random.uniform(low=-1, high=1, size=(3,3)))

# shuffle method
array = np.array([1, 2, 3, 4, 5])
rng = np.random.default_rng()
rng.shuffle(array)
print(array)

fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
fruit = rng.choice(fruits, size=(3,3))
print(fruit)