import numpy as np

### numpy.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>) ###
# 표준편차 계산

a2 = np.array([[1, 2], [3, 4]])
print(a2)

print(np.std(a2))
print(np.std(a2, axis=0))
print(np.std(a2, axis=1))
print(np.std(a2, where=[[True], [False]]))
