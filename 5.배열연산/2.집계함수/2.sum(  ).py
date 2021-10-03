import numpy as np

### np.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>) ###
# 합 계산
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)

print(a2.sum())
print(np.sum(a2))
print(a2.sum(axis=0))
print(np.sum(a2, axis=0))
print(a2.sum(axis=1))
print(np.sum(a2, axis=1))
