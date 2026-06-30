import numpy as np
# ___Random Integer___
# print(np.random.randint(1,10))

# Generate multiple integer
# print(np.random.randint(1,100,size=5))

# Generate a matrix
# print(np.random.randint(1,100,size=(3,3)))
#--------------------------------------------

# ___Random Floats___
# print(np.random.rand())

# Multiple floats
# print(np.random.rand(5))

# Matrix
# print(np.random.rand(3,4))
#--------------------------------------------

# ___Standard Normal Distribution___
# print(np.random.randn())

# Multiple values
# print(np.random.randn(5))

# Matrix
# print(np.random.randn(3,3))
#---------------------------------------------

# ___Seed___
# without seed
# print(np.random.randint(1,100,5))

# With seed
np.random.seed(1)
# print(np.random.randint(1,100,5))
#---------------------------------------------

# ___Shuffle___
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
# print(arr)
np.random.shuffle(arr)
# print(arr)
#---------------------------------------------

# ___Choice___
arr = np.array([10,20,30,40,50])
# print(np.random.choice(arr))
# print(np.random.choice(arr))

# print(np.random.choice(arr, size=3))
# print(np.random.choice(arr, size=3, replace=False))
#----------------------------------------------

# ___Uniform Distribution___
# print(np.random.uniform(1,5,size=10))
#----------------------------------------------

# ___Normal Distribution___
# marks = np.random.normal(
#     loc = 70,
#     scale = 8,
#     size = 20
# )
# print(marks)
#------------------------------------------------

# ___Random Sampling___
# arr = np.arange(100)
# sample = np.random.choice(
#     arr,
#     size=20,
#     replace=False
# )
# print(sample)
#------------------------------------------------