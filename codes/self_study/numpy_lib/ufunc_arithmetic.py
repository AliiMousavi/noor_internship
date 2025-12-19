import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
print(newarr)

arr3 = np.array([10, 20, 30, 40, 50, 60])
arr4 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr3, arr4)
print(newarr)

arr5 = np.array([10, 20, 30, 40, 50, 60])
arr6 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr5, arr6)
print(newarr)

arr7 = np.array([10, 20, 30, 40, 50, 60])
arr8 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr7, arr8)
print(newarr)

