import numpy as np

'''삼각함수
np.sin(x1): 요소 별 사인
np.cos(x1): 요소 별 코사인
np.tan(x1): 요소 별 탄젠트
np.arcsin(x1): 요소 별 아크사인
np.arccos(x1): 요소 별 아크코사인
np.arctan(x1): 요소 별 아크탄젠트
np.arctan2(x1,x2): 요소 별 아크탄젠트(x1,x2)
np.sinh(x1): 요소 별 하이퍼볼릭 사인
np.cosh(x1): 요소 별 하이퍼볼릭 코사인
np.tanh(x1): 요소 별 하이퍼볼릭 탄젠트
np.arcsinh(x1): 요소 별 하이퍼볼릭 아크사인
np.arccosh(x1): 요소 별 하이퍼볼릭 아크코사인
np.arctanh(x1): 요소 별 하이퍼볼릭 아크탄젠트
np.deg2rad(x1): 요소 별 각도에서 라디안 변환
np.rad2deg(x1): 요소 별 라디안에서 각도 변환
np.hypot(x1,x2): 요소 별 유클리드 거리계산
'''

a1 = np.linspace(0, np.pi, 3)
print(a1)
print(np.sin(a1))
print(np.cos(a1))
print(np.tan(a1))

x = [-1, 0, 1]
print(np.arcsinh(x))
print(np.arccos(x))
print(np.arctan(x))
