import numpy as np

### np.partition(a, kth, axis=- 1, kind='introselect', order=None)
# 배열에서 k개의 작은 값을 반환

# 1차원 배열
a1 = np.random.randint(1, 10, (10))
print(a1)

print(np.partition(a1, 3))

# 2차원 배열
a2 = np.random.randint(1, 10, (4, 4))
print(a2)

print(np.partition(a2, 3))
print(np.partition(a2, (1, 2), axis=0))
print(np.partition(a2, 3, axis=1))
