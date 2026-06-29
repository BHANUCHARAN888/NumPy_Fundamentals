import numpy as np
# Practice challenge 4
# 1. Create: 
arr = np.array([1,2,3,4,5,6]) #Reshape it into 2×3.
# print(arr.reshape(2,3))

# 2. Reshape the same array into 3×2.
# print(arr.reshape(3,2))

# 3. Use reshape(-1,2).
# print(arr.reshape(-1,2))

# 4. Flatten:
arr = np.array([[1,2],[3,4]])
# arr[0] = 200
# print(arr.flatten())
# print(arr)

# 5. Use ravel() on the same matrix.
# arr[0] = 100
# print(arr.ravel())
# print(arr)

# 6. Transpose
arr = np.array([
    [1,2,3],
    [4,5,6]
])
# print(arr.T)
# print(arr.transpose())

# 7. Add 100 to:
arr = np.array([
    [10,20],
    [30,40]
])
# print(arr + 100)

# 8. Broadcast:
matrix = np.array([
    [1,2,3],
    [4,5,6]
])
vector = np.array([10,20,30])
# print(matrix + vector)

# 9. Broadcast:
matrix = np.array([
    [1],
    [2],
    [3]
])
vector = np.array([100,200,300])
# print(matrix + vector)

# 10. Verify the difference between flatten() and ravel() by modifying the returned array and observing whether the original changes.
arr = np.array([
    [1,2,3],
    [4,5,6]
])
flat = arr.flatten()
flat[0] = 88
# print("Flatten: ",flat)
# print("Original:",arr)
# Originsl unchanged
# ----------------------
ravel = arr.ravel()
ravel[0] = 88
# print("Ravel: ",ravel)
# print("Original:",arr)
# Original changed