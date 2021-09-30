import numpy as np
'''랜덤패키지 내 함수 종류
send(): 난수 발생을 위한 시드(seed)지정
permutation(): 순서를 임의로 바꾸거나 임의의 순열 반환
shuffle(): 리스트나 배열의 순서를 뒤섞음
random(): 랜덤한 수의 배열 생성
rand(): 균등분포에서 표본 추출
randint(): 주어진 최소.최대 범위의 난수 추출
randn(): 표준편차가 1, 평균값이 0인 정규분포의 표본 추출
binomial(): 이항분포에서 표본 추출
normal(): 정규분포(가우시안)에서 표본 추출
beta(): 베타분포에서 표본 추출
chisquare(): 카이제곱분포에서 표본 추출
gamma(): 감마분포에서 표본 추출
uniform(): 균등(0, 1)분포에서 표본 추출
'''

### random.random() ###
print(np.random.random(()))
print(np.random.random(3))
print(np.random.random((3, 3)))

### random.randint() ###
# random.randint(low, high=None, size=None, dtype=int)
print(np.random.randint(5, size=10))
# 0~4까지 크기가 10인 랜덤 배열 생성
print(np.random.randint(0, 5, size=10))
# 0~4까지 크기가 10인 랜덤 배열 생성
print(np.random.randint(0, 10, size=(2, 2)))
# 0~9까지 크기가 2X2인 랜덤 배열 생성
print(np.random.randint(0, 10, (3, 3)))
# 0~9까지 크기가 3X3인 랜덤 배열 생성

### random.normal() ###
# random.normal(loc=0.0, scale=1.0, size=None)
# loc: 평균의 위치를 놓을 곳, scale: 표준편차
print(np.random.normal(0, 1, size=(3)))
print(np.random.normal(3, 2.5, (2, 4)))

### random.rand() ###
# random.rand(d0, d1, ..., dn)
print(np.random.rand(3, 3))
print(np.random.rand(2, 2, 2))


### random.randn() ###
# random.randn(d0, d1, ..., dn)
print(np.random.randn(3, 3))
print(np.random.randn(1, 2, 3))

### random.shuffle() ###
# random.shuffle(x)
arr = np.arange(9)
np.random.shuffle(arr)
print(arr)


### random.permutation() ###
# random.permutation(x)
print(np.random.permutation(10))
print(np.random.permutation([1, 4, 9, 12, 15]))
