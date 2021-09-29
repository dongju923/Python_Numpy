import numpy as np


def array_info(array):
    print(array)
    print("ndim:", array.ndim)
    # 배열의 차원
    print("shape:", array.shape)
    # 배열의 모양
    print("dtype:", array.dtype)
    # 배열의 타입
    print("size:", array.size)
    # 배열의 크기
    print("itmesize:", array.itemsize)
    # 각 요소의 크기
    print("nbytes:", array.nbytes)
    # 배열의 바이트 크기
    print("strides:", array.strides)
    # 다음 요소로 넘어가기 위해 필요한 바이트 크기


# 1차원 배열
array1 = np.arange(5)
array_info(array1)

# 2차원 배열
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_info(array2)

# 3차원 배열
array3 = np.ones((3, 3, 3))
array_info(array3)
