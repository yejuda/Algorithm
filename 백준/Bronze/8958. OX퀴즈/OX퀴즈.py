n = int(input())

for _ in range(n):
    cnt = 0  # cnt를 안에서 초기화해야 한 케이스가 끝났을 때 초기화 된다.
    O_cnt = 0  # O의 개수

    o_x = input()  # ox입력
    for i in o_x:
        if i == 'O':
            O_cnt += 1    # O 카운트 추가
            cnt += O_cnt  # O 카운트 만큼 더하기

        else:  # X라면
            O_cnt = 0     # O카운트 리셋
            cnt += 0
    
    print(cnt)

