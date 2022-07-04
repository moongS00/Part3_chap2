'''
# 1. 삼각형부터 십각형가지의 내각의 합과 내각을 딕셔너리에 저장하는 프로그램을
# n각형 내각의 합 = 180 * (n-2)

dic = {}

for n in range(3, 11):
    hap = 180 * (n-2)
    ang = int(hap / n)
    dic[n] = [hap, ang]


print(dic)
'''

# 2. 2부터 10까지 각각의 정수에 대한 약수를 저장하는 딕셔너리
dic = {}

for n in range(2, 11):
    temList = []
    for i in range(1, n+1):
        if n % i == 0:
            temList.append(i)

    dic[n] = temList

print(dic)