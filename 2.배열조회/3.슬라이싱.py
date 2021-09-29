import numpy as np

# array[start:stop:step]

# 1차원 배열
arr1 = np.arange(6)
print(arr1[0:])  # [0 1 2 3 4 5]
print(arr1[:6])  # [0 1 2 3 4 5]
print(arr1[2:6])  # [2 3 4 5]
print(arr1[-6:])  # [0 1 2 3 4 5]
print(arr1[-5:-1])  # [1 2 3 4]
print(arr1[-4:6])  # [2 3 4 5]
print(arr1[::2])  # [0 2 4]
print(arr1[1:5:3])  # [1 4]

# 2차원 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2[1])  # [4 5 6]
print(arr2[1, :])  # [4 5 6]
print(arr2[:2, :2])  # [[1 2][4,5]]
print(arr2[1:, ::-1])  # [[6 5 4][9 8 7]]
print(arr2[::-1, ::-1])  # [[9 8 7][6 5 4][3 2 1]]
