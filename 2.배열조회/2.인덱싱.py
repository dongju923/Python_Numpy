import numpy as np


# 1차원 배열
arr1 = np.arange(4, 9)
print(arr1[0])  # 4
print(arr1[1])  # 5
print(arr1[2])  # 6
print(arr1[3])  # 7
print(arr1[4])  # 8
print(arr1[-1])  # 8
print(arr1[-2])  # 7
print(arr1[-3])  # 6
print(arr1[-4])  # 5
print(arr1[-5])  # 4

# 2차원 배열
arr2 = np.array([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
print(arr2[0, 0])  # 1
print(arr2[0, 1])  # 2
print(arr2[1, 0])  # 4
print(arr2[1, 2])  # 6
print(arr2[2, 0])  # 7
print(arr2[2, 2])  # 9
print(arr2[0][-1])  # 3
print(arr2[-2][-3])  # 4
print(arr2[-1, 2])  # 9

# 3차원 배열
arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
print(arr3[0, 0, 0])  # 1
print(arr3[2, 2, 1])  # 26
print(arr3[1, 1, 2])  # 15
print(arr3[-2, -3, -1])  # 12
print(arr3[-1, 2, -3])  # 25
