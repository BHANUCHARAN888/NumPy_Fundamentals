import numpy as np
# practice challenge 3

# 1. Create two arrays:
a = np.array([5,10,15])
b = np.array([2,4,6])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# 2. Square every element of:
arr1 = np.array([2,4,6,8])
# print(np.square(arr1))

# 3. Find the square root of:
arr2 = np.array([1,4,9,16,25])
# print(np.sqrt(arr2))

# 4. Compute:
arr3 = np.exp(np.array([1,2,3]))
# print(arr3)

# 5. Compute:
arr4 = np.sin(np.array([0, np.pi/2, np.pi]))
# print(arr4)

# 6. Create:
arr5 = arr = np.array([10,20,30,40,50])
# print(arr5.sum())
# print(arr5.mean())
# print(arr5.max())
# print(arr5.min())
# print(arr5.std())
# print(arr5.var())

# 7. Create:
arr6 = np.array([
    [10,20,30],
    [40,50,60]
])
# print(arr6.sum())
# print(arr6.sum(axis=1))
# print(arr6.sum(axis=0))

# 8. Filter numbers greater than 25 from:
arr7 = np.array([5,15,25,35,45])
# print(arr7[arr7 > 25])

# 9. Compare:
arr8 = np.array([10,20,30,40])
# print(arr8 > 20)
# print(arr8 <= 30)

# 10. Calculate the average of:
arr9 = np.array([78,85,91,66,88])
# print(arr9.mean())
#---------------------------------------------------------------

#### MINI CHALLENGE ####
# 1. 🌡️ Temperature Conversion
celsius = np.array([0, 20, 30, 40, 100])
fahrenheit = (celsius * 9/5) + 32
# print(fahrenheit)

# 2. 📚 Student Marks Analysis
marks = np.array([78, 65, 89, 91, 56, 72, 84, 95, 61, 77])
# print(marks.max())
# print(marks.min())
# print(marks.mean())
# print(marks.std())
# print(marks.var())

# 3. 🎓 Pass Percentage
passed = marks >= 40
failed = marks < 40

num_passed = passed.sum()
num_failed = failed.sum()

pass_percentage = (num_passed / marks.size) * 100
fail_percentage = (num_failed / marks.size) * 100

# print("Passed: ",num_passed)
# print("Failed: ",num_failed)
# print("Pass %: ",pass_percentage)
# print("Fail %: ",fail_percentage)
#-------------------------------------------------------------------