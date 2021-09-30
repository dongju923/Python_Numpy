import numpy as np

### append(arr, values, axis=None) ###
# 배열의 끝에 값 추가

a1 = np.array([1, 2, 3, 4, 5])
print(np.append(a1, 6))
# a1배열의 끝에 6 추가

# axis지정이 없으면 1차원 배열 형태로 변형되어 결합
b1 = np.arange(1, 10).reshape(3, 3)
b2 = np.arange(10, 19).reshape(3, 3)
print(b1)
print(b2)
print(np.append(b1, b2))
# a1배열의 끝에 a2배열 추가(1차원 배열 형태)

# axis를 0으로 지정
print(np.append(b1, b2, axis=0))

# axis를 1로 지정
print(np.append(b1, b2, axis=1))
