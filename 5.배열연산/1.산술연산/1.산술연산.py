import numpy as np

'''산술연산자
np.add()    #덧셈
np.subtract()   #뺄셈
np.negative()   #단항 음수
np.multiply()   #곱셈
np.divide() #나눗셈
np.floor_divide()   #나눗셈 내림(몫 연산)
np.power()  #지수 연산
np.mod()    #나머지 연산
'''

# 1차원 배열
a1 = np.arange(1, 10)
print(a1)

print(a1+1)
print(np.add(a1, 10))

print(a1-1)
print(np.subtract(a1, 10))

print(-a1)
print(np.negative(a1))

print(a1*2)
print(np.multiply(a1, 2))

print(a1/2)
print(np.divide(a1, 2))

print(a1//2)
print(np.floor_divide(a1, 2))

print(a1 ** 2)
print(np.power(a1, 2))

print(a1 % 2)
print(np.mod(a1, 2))

b1 = np.random.randint(1, 10, (9))
print(b1)
print(a1+b1)
print(a1-b1)
print((-a1)+b1)
print(a1*b1)
print(a1/b1)
print(a1 // b1)
print(a1 ** b1)
print(a1 % b1)

# 2차원 배열
a2 = np.arange(1, 10).reshape(3, 3)
b2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
print(b2)

print(a2+b2)
print(a2-b2)
print((-a2)+b2)
print(a2*b2)
print(a2/b2)
print(a2 // b2)
print(a2 ** b2)
print(a2 % b2)
