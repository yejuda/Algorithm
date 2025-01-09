n = int(input())

EndNum = 666
cnt = 0  # 종말 번호를 업데이트 시켜줄 카운트 값

while True:
    if '666' in str(EndNum):
        cnt += 1
        if cnt == n:
            break
    EndNum += 1  # (666이 EndNum에 포함되어 있지 않으면) 종말번호를 계속해서 1씩 추가
    
print(EndNum)