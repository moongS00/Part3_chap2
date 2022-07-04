'''
# 1. 튜플을 요구사항대로 슬라이스 하기
numbers = (8.7, 9.0, 9.1, 9.2, 8.6, 9.3, 7.9, 8.1, 8.3)
# 인덱스 0부터 3까지
print(f'numbers : {numbers[:4]}')

# 인덱스 2부터 4까지
print(f'numbers : {numbers[2:5]}')

# 인덱스 3부터 끝까지
print(f'numbers : {numbers[3::]}')

# 인덱스 2부터 뒤에서 -2까지
print(f'numbers : {numbers[2:-1]}')

# 인덱스 0부터 끝까지 3단계
print(f'numbers : {numbers[::3]}')
'''

# 2. 시험점수를 입력한 후 튜플으ㅔ 저장하고 과목별 학점을 출력해보자
# 혼자풀기 실패

ks = int(input('국어 점수 입력 : '))
es = int(input('영어 점수 입력 : '))
ms = int(input('수학 점수 입력 : '))
ss = int(input('과학 점수 입력 : '))
hs = int(input('국사 점수 입력 : '))

scores = ({'kor':ks}, {'eng':es}, {'mat':ms}, {'sci':ss}, {'his':hs})
print(f'scores : {scores}')



for item in scores:
    for key in item.keys():

        if item[key] < 60:
            item[key] = 'F'

        elif item[key] < 70:
            item[key] = 'D'

        elif item[key] < 80:
            item[key] = 'C'

        elif item[key] < 90:
            item[key] = 'B'

        else:
            item[key] = 'A'


print(f'scores : {scores}')
