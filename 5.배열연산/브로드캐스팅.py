# Numpy의 배열 연산은 벡터화 연산을 사용
# 일반적으로 Numpy의 범용 함수를 통해 구현
# 배열 요소에 대한 반복적인 계산을 한번에 효율적으로 수행
# 일반적으로 Numpy에서 모양이 다른 배열끼리는 연산이 불가능

# 브로드캐스팅(Broadcasting)
# 어떤 조건만 맘ㄴ족한다면 모양이 다른 배열끼리의 연산을 가능하게함
# 모양이 부족한 부분은 확장하여 연산을 수행
import numpy as np

arr1_a = np.array([1, 2, 3])
arr1_b = np.array([4, 5, 6])
print(arr1_a)
# [1 2 3]
print(arr1_b)
# [4 5 6]
print(arr1_a+arr1_b)
# [5 7 9]
# arr1_a와 arr1_b를 더함
print(arr1_a+5)
# [6 7 8]
# 각 배열의 요소에 5를 더함

arr2_a = np.arange(1, 10).reshape(3, 3)
print(arr2_a)
print(arr1_a+arr2_a)
# 1차원 배열의 [1 2 3]을 2차원 배열로 자동변환하여 계산

arr2_b = np.array([1, 2, 3]).reshape(3, 1)
print(arr2_b)
print(arr1_a+arr2_b)
