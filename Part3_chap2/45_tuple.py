# 다음 두개의 튜플에 대해서 합집합과 교집합을 출력해보자

t1 = (1, 3, 2, 6, 12, 5, 7, 8)
t2 = (0, 5, 2, 9, 8, 6, 17, 3)

t1 = list(t1)
t2 = list(t2)
t3 = t1 + t2

cn = []
for num in t3:
    if t3.count(num) >= 2:
        cn.append(num)
        t3.remove(num)
cn.sort()
t3.sort()
cn = tuple(cn)
t3 = tuple(t3)
print(f'합집합(중복x) : {t3}')
print(f'교집합 : {cn}')

'''
선생님 풀이

t1 = (1, 3, 2, 6, 12, 5, 7, 8)
t2 = (0, 5, 2, 9, 8, 6, 17, 3)

temHAP = list(t1)
temGYO = []

for num in t2:
    if num not in temHAP:
        temHAP.append(num)
    else:
        temGYO.append(num)

temHAP.sort()
temGYO.sort()
temHAP = tuple(temHAP)
temGYO = tuple(temGYO)
print(f'합집합(중복x) : {temHAP}')
print(f'교집합 : {temGYO}')


'''
