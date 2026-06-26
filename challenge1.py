import numpy as np
# 1. Create a NumPy array containing numbers from 10 to 20.
print(np.arange(10,21))

# 2. Create a 3×4 array of zeros.
print(np.zeros((3,4)))

# 3. Create a 2×5 array of ones.
print(np.ones((2,5)))

# 4. Create a 4×4 array filled with 9.
print(np.full((4,4),9))

# 5. Print the shape, size, ndim, and dtype of the array:
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ndim)
print(arr.size)
print(arr.shape)
print(arr.dtype)

# 6. Create a 5×5 identity matrix.
print(np.eye(5))

# 7. Create numbers from 0 to 50 with a step of 5.
print(np.arange(0,51,5))

# 8. Create 8 equally spaced numbers between 0 and 1.
print(np.linspace(0,1,8))

# 9. Create a 2×3 array and verify that rows × columns = size.
rows, cols = arr.shape

print(rows * cols == arr.size)

# 10. Create an array [1, 2, 3, 4] and multiply every element by 10.
arr = np.array([1,2,3,4])
# print(arr * 10)

# ------------------------------------------------------------------------------
########### MINI CHALLENGE ###########
# 1. Create a 5×5 identity matrix.
print(np.eye(5))

# 2. Create an array containing numbers 1 to 100.
print(np.arange(1,101))

# 3. Create an array of even numbers from 2 to 100.
print(np.arange(2,101,2))

# 4. Create a 3×3 matrix filled with 25.
print(np.full((3,3),25))

# 5. Create 10 equally spaced values between 5 and 50.
print(np.linspace(5,50,10)) 
