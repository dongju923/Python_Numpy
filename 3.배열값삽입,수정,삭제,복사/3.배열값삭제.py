import numpy as np

### delete() ###
# 배열의 특정 위치에 값 삭제
# axis를 지정하지 않으면 1차원 배열로 변환
# 삭제할 방향을 axis로 지정
# 원본 배열 변경없이 새로운 배열 반환

# 1차원 배열
arr1 = np.arange(1, 6)
print(arr1)
# [1 2 3 4 5]
arr1 = np.delete(arr1, 1)
print(arr1)
# [1 3 4 5]
arr1 = np.delete(arr1, 3)
print(arr1)
# [1 3 4]

# 2차원 배열
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)
arr2 = np.delete(arr2, 1, axis=0)
print(arr2)
arr2 = np.delete(arr2, 1, axis=1)
print(arr2)
arr2 = np.delete(arr2, 2)
print(arr2)
