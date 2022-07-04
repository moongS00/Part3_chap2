'''
# 1. 자주접속하는 웹사이트 비번을 튜흘에 저장해보자
pass_s = ('pass1234', 'abc123', 'qwerty', 'letmein', 'welcome00')
print(f'pass_s : {pass_s}')
'''

# 2. 대학생 길동이의 1,2,3학년의 성적은 다음과 같다.
#  졸업할 때 4.0 이상의 학점을 받기 위해 길동이가 받아야 하는 4학년 1,2 학기의 최소 학점은?
#  1학년 (3.7, 4.2), 2학년 (2.9, 4.3), 3학년 (4.1, 4.2)

scores = ((3.7, 4.2), (2.9, 4.3), (4.1, 4.2))
sum = 0

for s1 in scores:
    for s2 in s1:
        sum += s2

sum = round(sum , 1)
avg = round(sum / 6, 1)
print(f'3학년 총학점 : {sum}')
print(f'3학년 평균 : {avg}')

tsum = round((4.0 * 8) - sum, 1)
tavg = round(tsum / 2, 1)
scores = list(scores)
scores.append((tavg, tavg))
scores = tuple(scores)
print('-' * 50)
print(f'4학년 목표 총학점 : {tsum}')
print(f'4학년 한학기 최소학점 : {tavg}')
print('-' * 50)
print(f'scores : {scores}')

