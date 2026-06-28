# Arithmetic operations
import numpy as np
arr1 = np.array([10,20,30])
arr2 = np.array([1,2,3])
# ___Addition___
# print(arr1 + arr2)

# ___Subtraction___
# print(arr1 - arr2)

# ___Multiplication___
# print(arr1 * arr2)

# ___Division___
# print(arr1 / arr2)

# ___FloorDivision___
# print(arr1 // arr2)

# ___Modulus___
# print(arr1 % arr2)

# ___Power___
# print(arr2 ** 2)
#-------------------------------------

# ___ComparisonOperators___
arr3 = np.array([10,20,30,40,50])

# print(arr3 > 30)
# print(arr3 < 30)
# print(arr3 >= 30)
# print(arr3 <= 30)
# print(arr3 != 30)
# print(arr3 == 30)
#-------------------------------------

# ___UniversalFunctions___
arr4 = np.array([2,4,6,8])
arr5 = np.array([1,3,5,7])

# print(np.add(arr4,arr5))
# print(np.subtract(arr4,arr5))
# print(np.multiply(arr4,arr5))
# print(np.divide(arr4,arr5))
# print(np.square(arr4))
# print(np.sqrt(arr4))
# print(np.sin(arr5))  uses radians, not degree
# print(np.cos(arr5))  uses radians, not degree
# print(np.exp(arr5))
# print(np.log(arr5))
# print(np.pi)
#-------------------------------------

# ___AggregationFunctions___
arr6 = np.array([10,20,30]) # 1D Array

# print(arr6.sum())
# print(arr6.mean())
# print(arr6.max())
# print(arr6.min())
# print(arr6.std())
# print(arr6.var())

arr7 = np.array([
    [10,20,30],
    [40,50,60]
])

# print(arr7.sum())
# print(arr7.sum(axis=0)) # column wise
# print(arr7.sum(axis=1)) # row wise

# print(arr7.mean())
# print(arr7.mean(axis=0))
# print(arr7.mean(axis=1))
