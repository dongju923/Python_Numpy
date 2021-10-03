import numpy as np

### np.cross(a, b, axisa=- 1, axisb=- 1, axisc=- 1, axis=None) ###
# 벡터 곱 계산

# 1차원 배열
a1 = np.array([1, 2, 3])
print(a1)
b1 = np.array([4, 5, 6])
print(b1)

print(np.cross(a1, b1))
# [-3  6 -3]
# 2*6 - 3*5
# 3*4 - 1*6
# 1*5 - 2*4

# 2차원 배열
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2)
b2 = np.array([[4, 5, 6], [1, 2, 3]])
print(b2)

print(np.cross(a2, b2))
