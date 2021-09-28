import numpy as np

### zeros() ###
# 모든 요소를 0으로 초기화
print(np.zeros(5))
# 1차원 배열
print(np.zeros((2, 2)))
# 2차원 배열
print(np.zeros((3, 3, 3)))
# 3차원 배열

### ones() ###
# 모든 요소를 1로 초기화
print(np.ones(5))
# 1차원 배열
print(np.ones((2, 3)))
# 2차원 배열
print(np.ones((3, 4, 5)))
# 3차원 배열

### full() ###
# 모든 요소를 지정한 값으로 초기화
print(np.full(5, 2))
# 1차원 배열
print(np.full((3, 3), 5))
# 2차원 배열
print(np.full((3, 3, 3), 1.25))
# 3차원 배열

### eye() ###
# 주대각선의 원소가 모두 1이고 나머지 원소는 모두 0인 정사각 행렬
print(np.eye(3))
# n X n 크기
print(np.eye(5, 6))
# n X m 크기


### tri() ###
# 삼각행렬 생성
print(np.tri(3))
# n X n 크기
print(np.tri(5, 3))
# n X m 크기
print(np.tri(3, 5, 2))
# n X m 크기에 배열이 채워지는 위치를 2만큼 추가
print(np.tri(3, 4, -1))
# n X m 크기에 배열이 채워지는 위치를 -1만큼 추가

### empty() ###
# 초기화되지 않은 배열 생성
# 초기화되지 않아서 기존 메모리 위치에 존재하는 값이 있으므로 주의해야함
print(np.empty(5))
# 1차원 배열
print(np.empty([3, 3]))
# 2차원 배열
print(np.empty([3, 3, 3], dtype=int))
# 3차원 배열


### __like() ###
# 지정된 배열과 shape이 같은 행렬 생성
a1 = np.array([1, 2, 3, 4, 5])
print(np.zeros_like(a1))

a2 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(np.ones_like(a2))

a3 = np.zeros((3, 3, 3))
print(np.full_like(a3, 3))
# a3 shape처럼 3으로 지정해서 생성
