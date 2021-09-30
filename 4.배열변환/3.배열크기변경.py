import numpy as np

### resize(a, new_shape) ###
# 배열 모양만 변경
arr2 = np.random.randint(0, 10, (2, 5))
print(arr2)
arr2.resize(5, 2)
print(arr2)
# 사이즈 크기는 그대로이기 때문에 shape만 바뀜

# 배열 크기 증가
# 남은 공간은 0으로 채워짐
arr2.resize(4, 4)
print(arr2)

# 배열 크기 감소
# 포함되지 않은 값은 삭제됨
arr2.resize(2, 3)
print(arr2)
