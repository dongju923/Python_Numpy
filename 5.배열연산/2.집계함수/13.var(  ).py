import numpy as np

### numpy.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>) ###
# 분산 계산

a2 = np.array([[1, 2], [3, 4]])
print(a2)

print(np.var(a2))
print(np.var(a2, axis=0))
print(np.var(a2, axis=1))
print(np.var(a2, where=[[True], [False]]))
