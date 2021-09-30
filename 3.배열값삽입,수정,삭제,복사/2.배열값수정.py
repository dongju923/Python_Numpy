import numpy as np

# 1차원 배열
arr1 = np.arange(1, 6)
print(arr1)
# [1 2 3 4 5]

arr1[0] = 4
arr1[1] = 5
arr1[2] = 6
arr1[3] = 7
arr1[4] = 8
print(arr1)
# [4 5 6 7 8]

arr1[:1] = 1
arr1[2:4] = 3
print(arr1)
# [1 5 3 3 8]

i = np.array([1, 3, 4])
arr1[i] = 0
print(arr1)
# [1 0 3 0 0]
arr1[i] += 4
print(arr1)
# [1 4 3 4 4]

# 2차원 배열
arr2 = np.arange(1, 7).reshape(3, 2)
print(arr2)

arr2[0, 0] = 8
arr2[1, 1] = 9
arr2[2, 0] = 4
print(arr2)

arr2[0] = 1
arr2[1] = 2
arr2[2] = 3
print(arr2)

arr2[1:, 1] = 9
arr2[-2:, 0] = 0
print(arr2)
