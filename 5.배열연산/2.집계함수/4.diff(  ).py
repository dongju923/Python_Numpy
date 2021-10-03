import numpy as np

### np.diff(a, n=1, axis=-1, prepend=<no value>, append=<no value>) ###
# 차분 계산

# 1차원 배열
a1 = np.array([1, 2, 4, 7, 0])
print(a1)

print(np.diff(a1))
# [ 1  2  3 -7]
# a1[1]-a1[0] = 1
# a1[2]-a1[1] = 2
# a1[3]-a1[2] = 3
# a1[4]-a1[3] = -7
print(np.diff(a1, n=2))
# [  1   1 -10]
# n=1일때 결과에서 다시 차분 계산
print(np.diff(a1, n=3))
# [  0 -11]
# n=2일때 결과에서 다시 차분 계산

# 2차원 배열
a2 = np.array([[1, 3, 6, 10], [0, 5, 6, 8]])
print(a2)

print(np.diff(a2, axis=1))
print(np.diff(a2, axis=0))
print(np.diff(a2, n=2, axis=1))
