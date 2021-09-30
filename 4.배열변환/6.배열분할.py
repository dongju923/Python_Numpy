import numpy as np

### split(ary, indices_or_sections, axis=0) ###
# 배열 분할
arr1 = np.arange(0, 10)
print(arr1)
print(np.split(arr1, [5]))
# [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9])]
a1, b1, c1, d1, e1 = np.split(arr1, [2, 4, 6, 8])
print(a1, b1, c1, d1, e1)
# [0 1] [2 3] [4 5] [6 7] [8 9]


### vsplit(ary, indices_or_sections) ###
# 수직 분할, 1차원으로 분할
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)
a2, b2 = np.vsplit(arr2, [2])
print(a2)
print(b2)

### hsplit(ary, indices_or_sections) ###
# 수평 분할, 2차원으로 분할
arr2 = np.arange(1, 10).reshape(3, 3)
print(arr2)
a2, b2 = np.hsplit(arr2, [2])
print(a2)
print(b2)

### dsplit(ary, indices_or_sections) ###
# 깊이 분할, 3차원으로 분할
arr3 = np.arange(1, 28).reshape(3, 3, 3)
print(arr3)
a3, b3 = np.dsplit(arr3, [2])
print(a3)
print(b3)
