import numpy as np

### np.prod(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>) ###
# 곱 계산

a1 = np.array([1, 2])
print(np.prod(a1))
# 2
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2)

print(np.prod(a2))
# 720
print(np.prod(a2, axis=1))
# [  6 120]
print(np.prod(a2, axis=0))
# [ 4 10 18]

a1 = np.array([2, 3, 5])
print(np.prod(a2, where=[True, False, True]))
# 10

a2 = np.array([[2, 3, 4], [3, 4, 5]])
print(a2)

print(np.prod(a2, where=([[True, False, True], [False, True, True]])))
# 160
print(np.prod(a2, axis=1, where=([[True, False, True], [False, True, True]])))
# [ 8 20]
print(np.prod(a2, axis=0, where=([[True, False, True], [False, True, True]])))
# [ 2  4 20]
# where=[False] = np.prod([]) = 1과 같음

a1 = np.array([1, 2, 3])
print(np.prod(a1, initial=5))
# 30
# [5, 2, 3], 첫 요소의 시작을 5배로 계산
a1 = np.array([2, 2, 3])
print(np.prod(a1, initial=10))
# 120
# [20, 2, 3], 첫 요소의 시작을 10배로 계산
