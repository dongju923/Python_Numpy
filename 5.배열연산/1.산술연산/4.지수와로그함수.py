import numpy as np

### np.exp(), np.exp2() ###
# 지수함수
a1 = np.random.randint(1, 10, (5))
print(a1)
print(np.exp(a1))
print(np.exp2(a1))

### np.log(), np.log2(), np.log10() ###
# 로그함수
a1 = np.random.randint(1, 10, (5))

print(a1)
print(np.log(a1))
print(np.log2(a1))
# 밑이 2인 로그
print(np.log10(a1))
# 밑이 10인 로그
