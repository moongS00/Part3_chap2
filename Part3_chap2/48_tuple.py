# 학생 수를 나타낸 튜플을 이용해서 요구사항에 맞는 데이터 출력
# 전체 학생 수, 평균 학생 수, 학생 수가 가장 많은 학급, 학생 수가 가장 적은 학급, 학급별 학생 편차

stCnt =({'cls01':18},
        {'cls02':21},
        {'cls03':20},
        {'cls04':19},
        {'cls05':22},
        {'cls06':20},
        {'cls07':23},
        {'cls08':17})

total = 0
max_cls = 0
max_cnt = 0
min_cls = 0
min_cnt = 0

for cls in stCnt:
    for key in cls.keys():
        total += cls[key]

        if key == 'cls01' or min_cnt > cls[key]:
            min_cls = key
            min_cnt = cls[key]


        if max_cnt < cls[key]:
            max_cls = key
            max_cnt = cls[key]

avg = round(total / len(stCnt), 1)

print(f'전체 학생 수 : {total}명')
print(f'평균 학생 수 : {avg}명')
print(f'학생 수가 가장 적은 학급 : {min_cls}({min_cnt}명)')
print(f'학생 수가 가장 많은 학급 : {max_cls}({max_cnt}명)')

for cls in stCnt:
    for key in cls.keys():
        cls[key] -= avg


print(f'학급별 학생 편차 : {stCnt}')

'''
# 선생님 풀이

for idx, dic in enumerate(stCnt):
    for k, v in dic.items():
        total += v


    if min_cnt == 0 or min_cnt > v:
        min_cls = k
        min_cnt = v

    if max_cnt > v:
        max_cls = k
        max_cnt = v

'''
