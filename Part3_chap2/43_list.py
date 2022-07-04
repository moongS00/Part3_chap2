# 4개의 숫자 중 서로 다른 숫자 2개를 선택해서 만들 수 있는 모든 경우의 수를 출력

num = [4, 6, 7, 9]
res = []
n = 0

for i in num:
    for j in num:
        for k in num:
            if i == j or j == k or i == k:
                continue

            res.append([i, j, k])

print(f'res : {res}')
print(f'res length : {len(res)}')