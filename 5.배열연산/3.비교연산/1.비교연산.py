import numpy as np


# 1차원 배열
a1 = np.arange(1, 10)
print(a1)
# [1 2 3 4 5 6 7 8 9]

print(a1 == 5)
print(np.equal(a1, 5))
# [False False False False  True False False False False]

print(a1 != 5)
print(np.not_equal(a1, 5))
# [ True  True  True  True False  True  True  True  True]

print(a1 < 5)
print(np.less(a1, 5))
# [ True  True  True  True False False False False False]

print(a1 <= 5)
print(np.less_equal(a1, 5))
# [ True  True  True  True  True False False False False]

print(a1 > 5)
print(np.greater(a1, 5))
# [False False False False False  True  True  True  True]

print(a1 >= 5)
print(np.greater_equal(a1, 5))
# [False False False False  True  True  True  True  True]

# 2차원 배열
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)

print(a2 > 5)
print(np.sum(a2 > 5))
print(np.sum(a2 >= 5, axis=0))
print(np.sum(a2 >= 5, axis=1))
print(np.any(a2 > 5, axis=0))
print(np.all(a2 > 5, axis=1))
