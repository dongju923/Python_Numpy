import numpy as np

### np.dot(a, b, axes=2) ###
# 텐서 곱 계산

a2 = np.array([[2, 3, 6], [3, 1, 7], [9, 6, 7]])
print(a2)
b2 = np.ones_like(a2)
print(b2)

print(np.tensordot(a2, b2))
print(np.tensordot(a2, b2, axes=2))
print(np.tensordot(a2, b2, axes=0))
print(np.tensordot(a2, b2, axes=1))
