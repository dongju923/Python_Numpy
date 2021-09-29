import numpy as np

# 배열의 각 요소의 선택 여부를 boolean형태로 지정
# True값인 인덱스의 값만 조회

# 1차원 배열
arr1 = np.arange(1, 6)
boolean_index1 = [True, False, False, True, True]
print(arr1)  # [1 2 3 4 5]
print(arr1[boolean_index1])  # [1 4 5]

# 2차원 배열
arr2 = np.arange(1, 10).reshape(3, 3)
boolean_index2 = np.random.randint(0, 2, (3, 3), dtype=bool)
print(arr2)
print(boolean_index2)
print(arr2[boolean_index2])

# 3차원 배열
arr3 = np.arange(1, 28).reshape(3, 3, 3)
boolean_index3 = np.random.randint(0, 2, size=(3, 3, 3), dtype=bool)
print(arr3)
print(boolean_index3)
print(arr3[boolean_index3])
