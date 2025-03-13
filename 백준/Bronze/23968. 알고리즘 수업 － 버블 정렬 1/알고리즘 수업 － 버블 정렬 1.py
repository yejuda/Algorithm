import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 현재 교환 횟수
cnt = 0

for i in range(n):  # 패스 수: n-1번
    # 각 패스에서 비교 범위
    for j in range(n-1-i):   # (n이 6이라는 가정하에, 0부터 5까지 / 0부터 4까지)
        if a[j] > a[j+1]:  
            a[j], a[j+1] = a[j+1], a[j]  # 교환
            cnt += 1

            if cnt == k:
                print(a[j], a[j+1])
                exit()

# k번째 교환에 도달하지 못한 경우
print(-1)
    