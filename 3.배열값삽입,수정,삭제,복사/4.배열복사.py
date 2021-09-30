import numpy as np

# 리스트 자료형과 달리 배열의 슬라이스는 복사본이 아님
# 배열을 복사하려면 copy()메서드를 사용해서 명시해야함

x = np.array([1, 2, 3])
print(x)  # [1 2 3]
y = x
print(y)  # [1 2 3]
z = np.copy(x)
print(z)  # [1 2 3]

x[0] = 10
print(x[0], y[0], z[0])  # 10 10 1

'''
x[0] = 10을 한 이후에 x, y는 값이 바뀌었지만
z는 값이 바뀌지 않음 z는 [1,2,3]의 값이 저장되어있음
y = x를 한다고 해도 복사된 것이 아니라 x가 수정되면 y도 수정됨
'''

x = np.arange(1, 10).reshape(3, 3)
y = x
z = np.copy(x)
z = x[:2, :2]
print(z)
print(x)
'''
x의 복사본 z를 수정해도 원본 x는 수정되지 않음'''
