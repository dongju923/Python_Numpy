import numpy as np

### numpy.any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>) ###
# 배열 내 값이 한개라도 True이면 True


# 1차원 배열
a1 = np.array([True, False, False])
print(a1)
# [ True False False]
print(np.any(a1))
# True

b1 = np.array([False, False, False])
print(b1)
# [False False False]
print(np.any(b1))
# False


# 2차원 배열
a2 = np.random.randint(0, 2, (3, 3), dtype=bool)
print(a2)

print(np.any(a2))
print(np.any(a2, axis=0))
print(np.any(a2, axis=1))
