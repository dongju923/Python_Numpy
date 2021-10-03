import numpy as np

### numpy.percentile(a, q, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False) ###
# 백분위 수

# 1차원 배열
a1 = np.array([0, 1, 2, 3])
print(a1)
# [0 1 2 3]

print(np.percentile(a1, 0))
# 0.0
print(np.percentile(a1, 20))
# 0.6000000000000001

print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='linear'))
# [0.  0.6 1.2 1.8 2.4 3. ]
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='higher'))
# [0 1 2 2 3 3]
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='lower'))
# [0 0 1 1 2 3]
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='nearest'))
# [0 1 1 2 2 3]
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='midpoint'))
# [0.  0.5 1.5 1.5 2.5 3. ]


# 2차원 배열
a2 = np.array([[10, 7, 4], [3, 2, 1]])
print(a2)

print(np.percentile(a2, 50))
print(np.percentile(a2, 50, axis=0))
print(np.percentile(a2, 50, axis=1))
print(np.percentile(a2, 50, axis=1, keepdims=True))
print(np.percentile(a2, 50, axis=1, keepdims=False))
