import numpy as np

### numpy.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>) ###
# 배열 내 값이 한개라도 False면 False


# 1차원 배열
a1 = np.array([True, False, False])
print(a1)
# [ True False False]
print(np.all(a1))
# False

b1 = np.array([True, True, True])
print(b1)
# [ True  True  True]
print(np.all(b1))
# True


# 2차원 배열
a2 = np.random.randint(0, 2, (3, 3), dtype=bool)
print(a2)

print(np.all(a2))
print(np.all(a2, axis=0))
print(np.all(a2, axis=1))
