import numpy as np

### np.save(file, arr, allow_pickle=True, fix_imports=True) ###
# Numpy 배열 객체 1개를 파일에 저장(바이너리 파일)
a2 = np.random.randint(1, 10, (5, 5))
print(a2)
np.save("np_save", a2)
# npy라는 확장자를 가진 파일 생성


### np.savez(file, *args, **kwds) ###
# Numpy 배열 객체 여러개를 파일에 저장(바이너리 파일)
b2 = np.random.randint(1, 10, (5, 5))
print(b2)
np.savez("np_savez", a2, b2)
# npz라는 확장자를 가진 파일 생성


### np.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII') ###
# Numpy 배열 저장 파일로부터 객체 로딩(바이너리 파일)
npy = np.load("np_save.npy")
print(npy)
npz = np.load("np_savez.npz")
print(npz.files)
# np_savez.npz안의 파일들을 출력
print(npz['arr_0'])
print(npz['arr_1'])
# 파일을 따로 불러오기 가능


### np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None) ###
# 텍스트 파일에 Numpy 배열 객체 저장(텍스트 파일)
print(a2)
np.savetxt("np_save.csv", a2, delimiter=',')
# np_save.csv파일로 각 요소 구분을 ,로 저장


### np.loadtxt(fname, dtype=<clas 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes', max_rows=None, *, like=None) ###
# 텍스트 파일로부터 배열 로딩(텍스트 파일)
csv = np.loadtxt("np_save.csv", delimiter=',')
print(csv)


np.savetxt("b2.csv", b2, delimiter=',', fmt='%.2e', header='c1,c2,c3,c4,c5')
# b2에 대해서 구분을 ,로 하고 포맷을 소수점 두자리까지, 헤더를 설정
