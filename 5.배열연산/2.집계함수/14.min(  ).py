import numpy as np

### numpy.min(a, axis=, out=, keepdims=, initial=., where=) ###
# 최소값

# 1차원 배열
a1 = np.random.randint(1, 10, (5))
print(a1)

print(np.min(a1))
print(np.min(a1 > 2))
print(np.min(a1[3] >= 3))

# 2차원 배열
a2 = np.random.randint(1, 10, (3, 3))
print(a2)

print(np.min(a2))
print(np.min(a2, axis=0))
print(np.min(a2, axis=1))
