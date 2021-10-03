import numpy as np

### numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=False) ###
# 중앙값


# 1차원 배열
a1 = np.random.randint(1, 10, (5))
print(a1)

print(np.median(a1))


# 2차원 배열
a2 = np.array([[10, 7, 4], [3, 2, 1]])
print(a2)

print(np.median(a2))
print(np.median(a2, axis=0))
print(np.median(a2, axis=1))

out = np.zeros_like(np.median(a2, axis=0))
print(np.median(a2, axis=0, out=out))
