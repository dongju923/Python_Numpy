import numpy as np
'''날짜/시간
Y: 연
M: 월
W: 주
D: 일
h: 시
m: 분
s: 초
ms: 밀리초
us: 마이크로초
ns: 나노초
ps: 피코초
fs: 펨토초
as: 아토초
'''
date = np.array('2020-01-01', dtype=np.datetime64)
# 문자열로 날짜를 지정해도 dtype=np.datetime64로 날짜/시간으로 변환
print(date)
print(date + np.arange(12))
# 기존 날짜에 배열만큼 데이터가 저장됨
print(np.datetime64('2020-06-01 12:00'))
# 시간표현
print(np.datetime64('2021-09-28 12:12:35.12', 'ns'))
# 나노초표현
print(np.arange('2021-09', '2021-10', dtype='datetime64[D]'))
# 2021-9월~2021-10월까지의 일[D]로 배열 생성
print(np.arange('2021', '2022', dtype='datetime64[M]'))
# 2021년~2022년 까지의 월[M]로 배열 생성
