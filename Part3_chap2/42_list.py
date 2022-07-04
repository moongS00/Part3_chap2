# 1. 친구 이릅 다섯명을 리스트에 저장하고 오름차순, 내림차순으로 정렬
'''
mf = []

for i in range(5):
    a1 = input('친구 이름 입력 : ')
    mf.append(a1)

print(f'친구들 : {mf}')
mf.sort()
print(f'오름차순 : {mf}')
mf.sort(reverse=True)
print(f'내림차순 : {mf}')
'''

# 2. 다음 리스트에서 중복 아이템(숫자)을 제거하는 프로그램을 만들어보자
num = [2, 22, 7, 8, 9, 2, 7, 3, 5, 2, 7, 1, 3]
print(f'num : {num}')

for i in num:
    if num.count(i) >= 2:
        num.remove(i)

print(f'num : {num}')
