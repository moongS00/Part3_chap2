# 다음 퓨틀의 과일 개수에 대해서 오름차순 및 내림차순으로 정렬해보자
# 혼자풀기 실패, 많이 어려움

fruits = ({'수박':8}, {'포도':13},{'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
fruits = list(fruits)

cIdx = 0  # 현재 비교 하는 값의 인덱스 (ex, 수박)
nIdx = 1  # 현재 비교 하는 녀석의 다음 값 (위가 수박이면, nIdx는 포도, 참외, 사과, 자두, 자몽의 인덱스 값) (변함)
eIdx = len(fruits) - 1  # 마지막 인덱스

flag = True
while flag:
    curDic = fruits[cIdx]
    nextDic = fruits[nIdx]

    curDicCnt = list(curDic.values())[0]  # 현재 딕셔너리의 과일의 개수
    nextDicCnt = list(nextDic.values())[0]  # 다음 딕셔너리의 과일의 개수

    if nextDicCnt < curDicCnt:  # curDicCnt=포도, nextDicCnt=참외인 경우
        fruits.insert(cIdx, fruits.pop(nIdx)) # 순서에 맞게 자리바꿈
        nIdx = cIdx + 1
        continue

    nIdx += 1
    if nIdx > eIdx:
        cIdx += 1
        nIdx = cIdx + 1

        if cIdx == 5:
            flag = False

fruits = tuple(fruits)
print(f'오름차순 : {fruits}')




fruits = ({'수박':8}, {'포도':13},{'참외':12}, {'사과':17}, {'자두':19}, {'자몽':15})
fruits = list(fruits)

cIdx = 0  # 현재 비교 하는 값의 인덱스 (ex, 수박)
nIdx = 1  # 현재 비교 하는 녀석의 다음 값 (위가 수박이면, nIdx는 포도, 참외, 사과, 자두, 자몽의 인덱스 값) (변함)
eIdx = len(fruits) - 1  # 마지막 인덱스


flag = True
while flag:
    curDic = fruits[cIdx]
    nextDic = fruits[nIdx]

    curDicCnt = list(curDic.values())[0]  # 현재 딕셔너리의 과일의 개수
    nextDicCnt = list(nextDic.values())[0]  # 다음 딕셔너리의 과일의 개수

    if nextDicCnt > curDicCnt:  # curDicCnt=포도, nextDicCnt=참외인 경우
        fruits.insert(cIdx, fruits.pop(nIdx)) # 순서에 맞게 자리바꿈
        nIdx = cIdx + 1
        continue

    nIdx += 1
    if nIdx > eIdx:
        cIdx += 1
        nIdx = cIdx + 1

        if cIdx == 5:
            flag = False

fruits = tuple(fruits)
print(f'내림차순 : {fruits}')