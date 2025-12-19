import numpy as np
print(f"version numpy: {np.__version__}")


arr = np.array([1, 2, 3, 4, 5])
print(f"array: {arr}")
print(f"array type: {type(arr)}")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"array: {arr}")


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])