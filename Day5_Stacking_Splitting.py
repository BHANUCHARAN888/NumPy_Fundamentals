import numpy as np
# ___Horizontal Stack___
# 1D
a = np.array([1,2,3])
b = np.array([4,5,6])
result = np.hstack((a,b))
# print(result)

# 2D
a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
result = np.hstack((a,b))
# print(result)
#------------------------------------

#___Vertical Stack___
# 1D
a = np.array([1,2,3])
b = np.array([4,5,6])
# print(np.vstack((a,b)))

# 2D
a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
# print(np.vstack((a,b)))
#-------------------------------------

# ___Column Stack___
a = np.array([1,2,3])
b = np.array([4,5,6])
# print(np.column_stack((a,b)))
#-------------------------------------

# ___Concatenate___
# 1D
# print(np.concatenate((a,b)))

# 2D
a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
# print(np.concatenate((a,b), axis=0))
# print(np.concatenate((a,b), axis=1))
#----------------------------------------

# ___Split___
# 1D
arr = np.array([1,2,3,4,5,6])
# print(np.split(arr, 3))

arr = np.array([1,2,3,4,5,6,7])
# print(np.array_split(arr,3))

# 2D
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
# print(np.vsplit(arr,2))
arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
# print(np.hsplit(arr,2))
#-----------------------------------------