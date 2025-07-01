n = int(input())
cnt = 0

while n >= 0:
    # 5로 나눠지면 끝!
    if n % 5 == 0:
        cnt += n // 5  # 15일 경우에 5로 3번 나눌 수 있으니까!
        print(cnt)
        break
    # 5로 나눠지지 않으면 3을 빼가기
    n -= 3
    cnt += 1

else:
    print(-1)
