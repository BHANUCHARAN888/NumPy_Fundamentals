import numpy as np

arr1 = np.array([1,2,3,4,5,6])
# ___Reshape___
# print(arr1.shape)

# print(arr1.reshape(3,2))
# print(arr1.reshape(2,3))

# print(arr1.reshape(2,-1))
# print(arr1.reshape(3,-1))
# print(arr1.reshape(-1,3))
# print(arr1.reshape(-1,2))
#--------------------------------------

# ___Flatten___ converts to 1D
arr2 = np.array([
    [1,2,3],
    [4,5,6]
])
# print(arr2.flatten()) #it is copy
# print(arr2) #original remain same
#--------------------------------------

# ___Ravel___ converts to 1D
# but changes remain same 
flat = arr2.ravel()
flat[0] = 100
# print(arr2)
# print(flat)
#--------------------------------------

# ___Transpose___
arr3 = np.array([
    [1,2,3],
    [2,3,4]
])
# print(arr3.shape)
# print(arr3.T)
# print(arr3.transpose())
#--------------------------------------

# ___Broadcasting___
# without numpy
for i in arr1:
    i = i + 10
# with numpy
arr1 + 10

# ___Matrix + Scalar
matrix = np.array([
    [1,2],
    [3,4]
])
# print(matrix + 100)

#___Matrix + Vector
matrix = np.array([
    [1,2,3],
    [4,5,6]
])
vector = np.array([10,20,30])
# print(matrix + vector)
matrix = np.array([
    [1],
    [2],
    [3]
])
vector = np.array([4,5,6])
# print(matrix + vector)
#---------------------------------------

# Shape A	Shape B 	Works?
# (3,)	    (3,)	     ✅
# (2,3)   	(3,)	     ✅
# (4,3)  	(3,)	     ✅
# (2,3) 	(2,1)	     ✅
# (2,3) 	(2,2)	     ❌