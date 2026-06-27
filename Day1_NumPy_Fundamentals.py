# Creating Arrays
import numpy as np
# Creating a 1D array
arr1 = np.array([1,2,3,4,5])
# print(arr1)
#Creating a 2D array
arr2 = np.array([[1,2],[3,4]])
# print(arr2)
# ---------------------------------------------
# ___Dimensions(ndim)___
# 1D
arr3 = np.array([1,2,3,4])
# print(arr3.ndim)
# 2D
arr4 = np.array([[1,2],[3,4]])
# print(arr4.ndim)
# 3D
arr5 = np.array([
    [
        [1,2],
        [3,4]
    ]
])
# print(arr5.ndim)
# -----------------------------------------------
# ___Shapes___
arr6 = np.array([
    [1,2,3],
    [4,5,6]
])
# print(arr6.shape) 2 rows, 3 columns
arr7 = np.array([
    [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
    ],
    [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
    ]
])
# print(arr7.shape) 2 blocks, 3 rows, 4 columns
# ------------------------------------------------
# ___Size___ total elements
arr8 = np.array([
    [1,2,3],
    [4,5,6]
])
# print(arr8.size)
# --------------------------------------------------
# ___dtype___
arr9 = np.array([1,2,3])
# print(arr9.dtype)
arr10 = np.array([1.2,3.67,4.5])
# print(arr10.dtype)
# --------------------------------------------------
# ___zeros()___ 
# print(np.zeros((2,3)))

# ___ones()___ 
# print(np.ones((3,2)))

# ___full()___ 
# print(np.full((2,2),20))

# ___eye()___ 
# print(np.eye(3))

# ___arange()___ 
# print(np.arange(1,10))
# print(np.arange(0,20,3))

# ___linspace()___ 
# print(np.linspace(0,5,3))