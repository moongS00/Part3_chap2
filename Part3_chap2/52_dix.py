# 5명의 회원을 가입받고 전체 회원 정보를 출력하는 프로그램


n = 1
mem = {}
while n < 6:
    m = input('메일 입력 : ')
    p = input('비번 입력 : ')

    if m in mem:
        print('이미 사용중인 메일 계정 입니다.')
        continue
    else:
        mem[m] = p

    n += 1


for key in mem.keys():
    print(f'{key} : {mem[key]}')


# 특정 회원을 삭제하는 프로그램

while True:
    did = input('삭제할 계정 입력 : ')
    if did in mem.keys():
        dpw = input('비번 입력 : ')
        if dpw == mem[did]:
            del mem[did]
            print(f'{did}님 삭제 완료!')
            break

        else:
            print('비번 확인 요망!')
            continue
    else:
        print('계정 확인 요망!')
        continue





for key in mem.keys():
    print(f'{key} : {mem[key]}')
