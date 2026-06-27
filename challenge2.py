import numpy as np
# Practice challenge 2

arr = np.array([1,2,3,4,5])
arr1 = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
# 1. Print the first element.
print(arr[0])
print(arr1[0,0])

# 2. Print the last element.
print(arr[-1])
print(arr1[2,2])

# 3. Print the second row.
print(arr1[1])

# 4. Print the third column.
print(arr1[:,2:])

# 5. Reverse the array:
print(arr[::-1])

# 6. Extract the first two rows.
print(arr1[0:2])

# 7. Extract the last two columns.
print(arr1[:,1:])

# 8. Extract the bottom-right 2×2 block.
print(arr1[1:,1:])

# 9. Create: arr = np.array([5,10,15,20,25,30])
# Print only values greater than 15.
arr2 = np.array([5,10,15,20,25,30])
print(arr2[arr2 > 15])

# 10. Use fancy indexing to print the elements at indices [0, 2, 5] from:
arr3 = np.array([100,200,300,400,500,600])
print(arr3[[0,2,5]])

#-----------------------------------------------------------
####### MINI CHALLENGE #######
matrix = np.array([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# 1. Extract the third row.
print(matrix[2])

# 2. Extract the last column.
print(matrix[:,4:])

# 3. Extract the center 3×3 block.
print(matrix[1:4,1:4])

# 4. Extract the four corner values using indexing.
print(matrix[0,0],matrix[0,4],matrix[4,0],matrix[4,4])

# 5. Print all values greater than 15 using boolean indexing.
print(matrix[matrix > 15])

# 6. Using fancy indexing, extract rows 1 and 3 (2nd and 4th rows).
print(matrix[1],matrix[3])
#--------------------------------------------------------------

# arr[2] returns row
# arr[:,2] returns 1D
# arr[:,2:] returns 2D