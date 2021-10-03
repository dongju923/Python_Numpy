import numpy as np

### np.cumsum(a, axis=None, dtype=None, out=None) ###
# 누적 합 계산
a2 = np.arange(1, 7).reshape(2, 3)
print(a2)

print(a2.cumsum())
print(np.cumsum(a2))
print(a2.cumsum(axis=0))
print(np.cumsum(a2, axis=0))
print(a2.cumsum(axis=1))
print(np.cumsum(a2, axis=1))
