n = int(input())  # 배달해야 하는 설탕 n킬로그램
cnt = 0  # 봉지 개수

while n >= 0:
    # n이 5의 배수인지 확인 -> 5의 배수라면 몫(봉지 수) 출력
    if n % 5 == 0:   
        cnt += (n//5)
        print(cnt)
        break
    else:            # 5의 배수가 아니라면
        n -= 3       # 3을 빼주기
        cnt += 1     # 봉지 수는 늘린다
else:
    print(-1)