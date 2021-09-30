import numpy as np


### reshape(a, newshape, order='C(F,A)') ###
# 기존 배열의 shape을 재구조화
arr1 = np.arange(1, 10)
print(arr1)
print(arr1.reshape(3, 3))
# 3X3 형태로 배열 재구조

arr1 = np.arange(1, 28)
print(arr1)
arr3 = np.reshape(arr1, (3, 3, 3))
print(arr3)
# 3X3X3 형태로 배열 재구조

'''
arr1 = np.arange(1, 28)
print(arr1)
arr3 = arr1.reshape(3, 3, 2)
print(arr3)
reshape할 구조의 요소수와 기존의 요소수가 다르면 오류가남

ValueError: cannot reshape array of size 27 into shape 
(3,3,2)
'''

### newaxis() ###
# 새로운 축 추가
arr1 = np.arange(1, 6)
print(arr1)
print(arr1[:6, np.newaxis])
# :6 까지 인덱스에 새로운 축을 추가

arr2 = np.arange(1, 7).reshape(2, 3)
print(arr2)
print(arr2[:, :2, np.newaxis])
# :, :2 까지 인덱스에 새로운 축을 추가
