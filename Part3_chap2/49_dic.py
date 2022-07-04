'''
# 1. 과목별 점수를 딕셔너리에 저장하고 출력

sub = ['국어', '영어', '수학', '과학', '국사']
scores = {}

for s in sub:
    score = int(input(s+' 점수 입력 : '))
    scores[s] = score

print(f'과목별 점수 : {scores}')
'''

# 2. 사용자의 아이디, 비밀번호를 이용해 로그인 프로그램을 만들어보자
members = {'abc': '123', 'def': '456', 'ghi': '789', 'jkl': '101112'}

ID = input('ID입력 : ')
PW = input('PW입력 : ')

if members[ID] == PW:
    print('로그인 성공!')
else:
    print('비밀번호 확인!!')
