import numpy as np

### np.isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False) ###
# 상대 차이 ( rtol * abs ( b ))와 절대 차이 atol 이 함께 더해 a 와 b 의 절대 차이를 비교

a1 = np.array([1, 2, 3, 4, 5])
print(a1)
# [1 2 3 4 5]
b1 = np.array([1, 2, 3, 3, 4])
print(b1)
# [1 2 3 3 4]

print(np.isclose(a1, b1))
# [True  True  True False False]


### np.isinf(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) ###
# 배열이 inf면 True, 아니면 False

### np.isfinite(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) ###
# 배열이 inf, nan이면 False, 아니면 True

### np.isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) ###
# 배열이 nan이면 True, 아니면 False

a1 = np.array([np.nan, 2, np.inf, 4, np.NINF])
print(a1)
# [ nan   2.  inf   4. -inf]

print(np.isinf(a1))
# [False  True False  True False]
print(np.isfinite(a1))
# [False  True False  True False]
print(np.isnan(a1))
# [ True False False False False]
