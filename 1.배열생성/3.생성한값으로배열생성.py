import numpy as np
from numpy.core.function_base import logspace

### arange() ###
# 정수 범위로 배열 생성
# arrange(start, stop, step, ...)
print(np.arange(5))
# [0 1 2 3 4]
print(np.arange(2, 8))
# [2 3 4 5 6 7]
print(np.arange(0, 11, 2))
# [ 0  2  4  6  8 10]


### linspace() ###
# 범위 내에서 균등간격의 배열 생성
# linspace(start, stop, num= , endpoint=boolean, retstep=boolean, ...)
print(np.linspace(0, 1, 5))
# [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(2, 3, num=5, endpoint=False))
# endpoint=False이면 stop 값은 포함 안함(Defalt는 True)
print(np.linspace(0, 1, num=5, retstep=True, endpoint=False))
# retstep=True이면 간격을 출력(Defalt는 False)


### logspace() ###
# 범위 내에서 균등간격으로 로그 스케일로 배열 생성
# logspace(start, stop, num=, endpoint=boolean, base=, ...)
print(logspace(0.1, 1, num=4))
# [1.25892541  2.51188643  5.01187234 10.]
print(logspace(0.1, 2, 5, base=2))
# base=2면 밑을 2로 하는 로그(Defalt는 10)
