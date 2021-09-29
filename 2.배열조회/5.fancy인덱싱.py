import numpy as np

# 1차원 배열
arr1 = np.arange(1, 6)
index1 = [0, 3]
print(arr1)  # [1 2 3 4 5]
print(arr1[0], arr1[3])  # 1 4
print(arr1[index1])  # [1 4]

index2 = np.array([[0, 1], [3, 4]])
print(arr1[index2])  # [[1 2][4 5]]


# 2차원 배열
arr2 = np.arange(1, 10).reshape(3, 3)
row = np.array([0, 2])
col = np.array([1, 2])
print(arr2)
print(arr2[row, col])  # [2 9]
'''
row[0] = [1 2 3]
col[1] = [2 5 8]
겹치는 값 = 2
row[2] = [7 8 9]
col[2] = [3 6 9]
겹치는 값 = 9
'''
