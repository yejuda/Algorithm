n = int(input())

# 5로 나누어지면 그게 정답, 아니면 3을 빼기 -> 다시 5로 나눠보기
cnt = 0
while 0 <= n:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    
    n -= 3
    cnt += 1

# n킬로그램 만들 수 없다면 -1
else:
    print(-1)