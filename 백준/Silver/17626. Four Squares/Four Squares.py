import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

# dp = [float('inf')] * (n + 1) # 모든 dp 값을 무한대로 초기화
# dp[0] = 0 # 0을 나타내는 데 필요한 제곱수 개수는 0개이므로 예외 처리

for i in range(1, n+1):
    dp[i] = i  # dp가 현재 0으로 초기화되어 있기 때문에, 최소값은 무조건 0이 출력될 것이다.
    for j in range(1, i + 1):  # j가 i를 넘지 않도록
        if j*j > i:  # 만약에 넘으면 break
            break
        dp[i] = min(dp[i], dp[i-j*j] + 1)

print(dp[n])