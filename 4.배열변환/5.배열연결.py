import numpy as np

### concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind(‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’)") ###
# 튜플이나 배열의 리스트를 인수로 사용해 배열 연결

# 1차원 배열
arr1_a = np.array([1, 3, 5])
arr1_b = np.array([2, 4, 6])
print(np.concatenate([arr1_a, arr1_b]))
# [1 3 5 2 4 6]
arr1_c = np.array([7, 8, 9])
print(np.concatenate([arr1_a, arr1_b, arr1_c]))
# [1 3 5 2 4 6 7 8 9]


# 2차원 배열
arr2_a = np.array([[1, 2], [3, 4]])
arr2_b = np.array([[5, 6], [7, 8]])
print(np.concatenate([arr2_a, arr2_b], axis=0))
print(np.concatenate([arr2_a, arr2_b], axis=1))
print(np.concatenate([arr2_a.T, arr2_b.T], axis=0))


### vstack(tup) ###
# 수직스택(vertical stack), 2차원으로 연결
print(np.vstack([arr2_a, arr2_b]))

### hstack(tup) ###
# 수평스택(horizontal stack), 2차원으로 연결
print(np.hstack([arr2_a, arr2_b]))

### dstack(tup) ###
# 깊이스택(depth stack), 3차원으로 연결
print(np.dstack([arr2_a, arr2_b]))

### stack(arrays, axis=0, out=None) ###
# 새로운 차원으로 연결
print(np.stack([arr2_a, arr2_b]))
