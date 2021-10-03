import numpy as np

### np.cumprod(a, axis=None, dtype=None, out=None) ###
# 누적 곱 계산

# 1차원 배열
a1 = np.array([1, 2, 3, 4, 5])
print(a1)

print(np.cumprod(a1))
# [  1   2   6  24 120]
# 1
# 2 * 1
# 3 * 2 * 1
# 4 * 3 * 2 * 1
# 5 * 4 * 3 * 2 * 1


# 2차원 배열
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2)

print(np.cumprod(a2, dtype=float))
# [  1.   2.   6.  24. 120. 720.]
print(np.cumprod(a2, axis=1))
print(np.cumprod(a2, axis=0))

# 3차원 배열
a3 = np.random.randint(1, 10, (3, 3))
print(a3)

print(np.cumprod(a3, axis=1))
print(np.cumprod(a3, axis=0))
