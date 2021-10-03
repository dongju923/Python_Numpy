import numpy as np

### numpy.argmax(a, axis=None, out=None) ###
# 최대값의 인덱스위치

# 1차원 배열
a1 = np.random.randint(1, 10, (5))
print(a1)

print(np.argmax(a1))

# 2차원 배열
a2 = np.random.randint(1, 10, (3, 3))
print(a2)

print(np.argmax(a2))
print(np.argmax(a2, axis=0))
print(np.argmax(a2, axis=1))
