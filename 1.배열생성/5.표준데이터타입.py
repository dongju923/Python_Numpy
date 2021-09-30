import numpy as np
'''데이터 타입
bool_: True, False값을 가짐
int_: 기본 정수 타입
intc: C언어 에서 사용되는 int와 동일
intp: 인덱싱에 사용되는 정수(int32, int64)
int8,int16,int32,int64: 정수
uint8,uint16,uint32,uint64: 부호없는 정수
float16,float32,float64: 부동소수점
float_: float64를 줄여서 표현
complex64, complex128: 복소수
complex: complex128을 줄여서 표현
'''
print(np.zeros(10, dtype=int))
# 0으로된 10개 배열을 int 형태로 출력
print(np.ones(10, dtype=bool))
# 1로된 10개 배열을 boolean 형태로 출력
print(np.ones((3, 3), dtype=bool))
# 1로된 3X3 배열을 boolean 형태로 출력
print(np.full((3, 3), 2, dtype=float))
# 2로된 3X3 배열을 float 형태로 출력

