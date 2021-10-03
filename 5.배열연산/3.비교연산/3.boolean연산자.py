import numpy as np

### &, np.bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) ###
### |, np.bitwise_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) ###
### ^, np.bitwise_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) ###
### ~, np.bitwise_not(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) ###

a2 = np.arange(1, 10).reshape(3, 3)
print(a2)

print((a2 > 5) & (a2 < 8))
print(a2[(a2 > 5) & (a2 < 8)])
# [6 7]
print((a2 > 5) | (a2 < 8))
print(a2[(a2 > 5) | (a2 < 8)])
# [1 2 3 4 5 6 7 8 9]
print((a2 > 5) ^ (a2 < 8))
print(a2[(a2 > 5) ^ (a2 < 8)])
# [1 2 3 4 5 8 9]
print(~(a2 > 5))
print(a2[~(a2 > 5)])
# [1 2 3 4 5]
