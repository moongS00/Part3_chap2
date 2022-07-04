# 1부터 사용자가 입력한 숫자까지의 약수와 소수를 리스트에 각각 저장하고 출력하는 프로그램

input_num = int(input('1보다 큰 정수 입력 : '))
listA = []
listB = []

for i in range(1, input_num+1):
    if input_num % i == 0:
        listA.append(i)


for i in range(2, input_num+1):
    flag = True
    for n in range(2, i):
        if i % n == 0:
            flag = False
            break

    if flag:
        listB.append(i)


print(f'{input_num}의 약수 : {listA}')
print(f'{input_num}까지의 소수 : {listB}')




