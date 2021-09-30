import numpy as np

### insert() ###
# axis를 지정하지 않으면 1차원 배열로 변환
# 추가할 방향을 axis로 지정
# 원본 배열 변경없이 새로운 배열 반환
# insert(arr, obj, values, axis=None)


# 1차원 배열
arr1 = np.arange(1, 6)
print(arr1)
arr1 = np.insert(arr1, 3, 10)
# arr1 배열의 3번째 인덱스에 10을 추가
print(arr1)
# [1  2  3 10  4  5]
arr1 = np.insert(arr1, 5, 8)
print(arr1)
# [ 1  2  3 10  4  8  5]

# 2차원 배열
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)
arr2 = np.insert(arr2, 1, 10, axis=0)
print(arr2)
# 가로축을 기준(axis=0)으로 1번째 인덱스에 10을 추가
arr2 = np.insert(arr2, 1, 20, axis=1)
print(arr2)
# 세로축을 기준(axis=1)으로 1번째 인덱스에 20을 추가
arr2 = np.insert(arr2, 3, 50)
print(arr2)
# [ 1 20  2 50  3 10 20 10 10  4 20  5  6  7 20  8  9]
# 2차원배열에서 axis를 정하지 않으면 1차원배열로 변환되어 추가
