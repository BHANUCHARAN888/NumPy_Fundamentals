import numpy as np
# Accessing Elements 1D Array
# +0  1  2  3  4 positive index
# 10 20 30 40 50
# -5 -4 -3 -2 -1 negative index
arr1 = np.array([10,20,30,40,50])
# print(arr1[0]) 
# print(arr1[1])
# print(arr1[-1])
#------------------------------------
# ___Slicing_1D___
# print(arr1[0:5])
# print(arr1[0:5:2])
# print(arr1[:3])
# print(arr1[2:])
# print(arr1[::2])
# print(arr1[::-1])
#------------------------------------
# ___Multidimensional indexing___
arr2 = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5]
])
# print(arr2[2,2]) 2-row, 2-column

## Extracting Rows
# print(arr2[2])

## Extracting Columns
# print(arr2[:,1])
#--------------------------------------
# ___Slicing_2D___
# print(arr2[:2,:2])
# print(arr2[1:,1:])
# print(arr2[:2,1:])
# print(arr2[2:,:1])
#---------------------------------------
# ___Boolean_Indexing___
# print(arr1 > 10)
# print(arr1[arr1 > 20])
# print(arr1[arr1%3 == 0])
#---------------------------------------
# ___Fancy_Indexing___
# print(arr1[[0,2,4]])
# print(arr1[[1,1,2]])
# print(arr2[[0,2]])