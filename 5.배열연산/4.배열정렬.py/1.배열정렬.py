import numpy as np

### np.sort(a, axis=- 1, kind=None, order=None) ###
# 오름차순 정렬

# 1차원 배열
a1 = np.random.randint(1, 10, size=10)
print(a1)
# [2 6 2 9 9 4 8 4 2 5]
print(np.sort(a1))
# [2 2 2 4 4 5 6 8 9 9]

# 2차원 배열
a2 = np.random.randint(1, 10, (3, 3))
print(a2)
print(np.sort(a2))
print(np.sort(a2, axis=1))
print(np.sort(a2, axis=0))

### np.argsort(a, axis=- 1, kind=None, order=None) ###
# 값에 대한 인덱스 오름차순 정렬

a1 = np.random.randint(1, 10, size=10)
print(a1)
# [5 5 7 5 4 9 6 7 1 6]
print(np.argsort(a1))
# [8 4 0 1 3 6 9 2 7 5]

# 2차원 배열
a2 = np.random.randint(1, 10, (3, 3))
print(a2)
print(np.argsort(a2))
print(np.argsort(a2, axis=1))
print(np.argsort(a2, axis=0))
