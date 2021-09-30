import numpy as np


### T ###
# 행과 열이 전치가 됨
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)
arr2 = arr2.T
print(arr2)


arr3 = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [
                4, 5, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [7, 8, 9]]])

print(arr3)
print(arr3.T)


### swapaxes ###
# axis가 전치가됨
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)
print(arr2.swapaxes(1, 0))

arr3 = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [
                4, 5, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [7, 8, 9]]])
print(arr3)
print(arr3.swapaxes(0, 1))
print(arr3.swapaxes(1, 2))
print(arr3.swapaxes(0, 2))
