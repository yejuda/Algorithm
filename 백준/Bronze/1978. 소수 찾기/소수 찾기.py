n = int(input())    # 수의 개수
a = list(map(int, input().split()))
cnt = 0

for i in a:

    if i == 1:  # 1은 소수가 아니다.
        continue 

    for j in range(2, i):  # 소수는 1보다 큰 자연수 중에서 1과 자기자신을 제외한 자연수로 나누어떨어지지 않는 자연수이다.
        if i % j == 0:
            break
    else:
        cnt += 1
        
print(cnt)