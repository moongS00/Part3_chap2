'''
다음은 공원 입장료를 나타낸 표이다. 1일 총 입장객이 100명이라고 할 때,
1일 전체 입장 요금을 구하는 프로그램을 만들어보자
단, 입장고객의 나이는 난수를 이용한다.

0-7세 : 무료
8-13세 : 200
14-19세 : 300
20-64세: 500
65- : 무료
'''


import random

at = random.sample(range(0, 100), 100)
inf = []
kid = []
you = []
adt = []
eld = []

for age in at:
    if age < 8:
        inf.append(age)
    
    elif age < 14:
        kid.append(age)
    
    elif age < 20:
        you.append(age)
    
    elif age < 65:
        adt.append(age)
    
    else:
        eld.append(age)

n_inf = len(inf)
n_kid = len(kid)
n_you = len(you)
n_adt = len(adt)
n_eld = len(eld)

p_inf = len(inf) * 0
p_kid = len(kid) * 200
p_you = len(you) * 300
p_adt = len(adt) * 500 
p_eld = len(eld) * 0
p_total = p_inf + p_kid + p_you + p_adt + p_eld



print('-' * 30)
print(f'영유아 : {n_inf}명 :{p_inf}원')
print(f'어린이 : {n_kid}명 :{p_kid}원')
print(f'청소년 : {n_you}명 : {p_you}원')
print(f'성인   : {n_adt}명 :{p_adt}원')
print(f'어르신 : {n_eld}명 : {p_eld}원')
print('-' * 30)
print(f'1일 요금 총합계 : {p_total}원')
print('-' * 30)