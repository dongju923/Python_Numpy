import numpy as np

### np.inner(a, b) ###
# 벡터의 내부 곱 계산

# 1차원 배열
a1 = np.array([1, 2, 3])
print(a1)
b1 = np.array([0, 1, 0])
print(b1)

print(np.inner(a1, b1))


# 2차원 배열
a2 = np.random.randint(1, 5, (3, 3))
print(a2)
b2 = np.ones_like(a2)
print(b2)

print(np.inner(a2, b2))
