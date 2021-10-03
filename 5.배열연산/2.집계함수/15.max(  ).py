import numpy as np

### numpy.max(a, axis=, out=, keepdims=, initial=., where=) ###
# 최소값

# 1차원 배열
a1 = np.random.randint(1, 10, (5))
print(a1)

print(np.max(a1))
print(np.max(a1 > 2))
print(np.max(a1[3] >= 3))

# 2차원 배열
a2 = np.random.randint(1, 10, (3, 3))
print(a2)

print(np.max(a2))
print(np.max(a2, axis=0))
print(np.max(a2, axis=1))
