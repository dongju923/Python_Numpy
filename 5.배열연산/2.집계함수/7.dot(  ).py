import numpy as np

### np.dot(a, b, out=None) ###
# 점 곱 계산

# 1차원 배열
a1 = np.array([1, 2, 3])
print(a1)
b1 = np.array([3, 4, 5])
print(b1)

print(np.dot(a1, b1))
# 26
# 1*3 + 2*4 + 3*5

a2 = np.array([[1, 2], [3, 4]])
print(a2)
b2 = np.array([[5, 6], [7, 8]])
print(b2)

print(np.dot(a2, b2))
# [[19 22]
# [43 50]]
# 1*5 + 2*7 = 19
# 1*6 + 2*8 = 22
# 3*5 + 4*7 = 43
# 3*6 + 4*8 = 50
