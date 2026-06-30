import numpy as np
# Practice challenge 5

a = np.array([1,2,3])
b = np.array([4,5,6])
# 1. Stack horizontally:
# print(np.hstack((a,b)))

# 2. Stack vertical
# print(np.vstack((a,b)))

# 3. Column_stack()
# print(np.column_stack((a,b)))

# 4. Concatenate two arrays.
# print(np.concatenate((a,b)))

# 5. Split
arr = np.array([10,20,30,40,50,60]) # into 3 equal parts.
# print(np.split(arr,3))

# 6. join
a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
# print(np.hstack((a,b)))
# print(np.vstack((a,b)))
# print(np.concatenate((a,b),axis=0))
# print(np.concatenate((a,b),axis=1))

# 7. Split:
arr = np.array([1,2,3,4,5,6,7]) # using array_split(arr,3).
# print(np.array_split(arr,3))

# 8. Split the following matrix vertically:
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
# print(np.vsplit(arr,2))

# 9. Split the following matrix horizontally:
arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
# print(np.hsplit(arr,2))

# 10. Create two 1D arrays representing:
math = np.array([80,85,90])
science = np.array([75,88,92])
# print(np.column_stack((math,science)))
#-----------------------------------------------------

#### MINI CHALLENGE ####

names = np.array(["Alice","Bob","Charlie","David"])
marks = np.array([85,72,91,68])
attendance = np.array([95,88,100,90])

# 1. Combine marks and attendance into a 2-column matrix.
# print(np.column_stack((marks, attendance)))

# 2. Stack all three arrays (names, marks, attendance) into a single table-like structure.
# print(np.column_stack((names, marks, attendance)))

# 3. Split the marks array into 2 equal parts.
# print(np.split(marks,2))

# 4. Split the attendance array into 3 parts using array_split().
# print(np.array_split(attendance,3))

# 5. Print the first half and second half of the marks separately.
# first_half, second_half = np.split(marks, 2)
# print(first_half)
# print(second_half)
