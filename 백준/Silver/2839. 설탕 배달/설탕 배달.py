n = int(input())
cnt = 0

# 핵심: 5로 나누어지면 끝!
# cnt 에 n을 5로 나눈 것을 넣어서 개수 누적하기
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    
    n -= 3
    cnt += 1

else:
    print(-1)