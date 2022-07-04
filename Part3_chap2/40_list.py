# 1부터 100사이에 난수 10개를 생성한 후, 짝수와 홀수를 구분해서 리스트에 저장 후 출력

import random

r_num = random.sample(range(1, 101), 10)
listA = []
listB = []

for i in r_num:
    if i % 2 == 0:
        listA.append(i)
    else:
        listB.append(i)

print(f'짝수 : {listA}, 개수 : {len(listA)}개')
print(f'홀수 : {listB}, 개수 : {len(listB)}개')