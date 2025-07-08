n = int(input())

# 3이상일 경우에만 dp를 생성
dp = [0] * max(3, n+1)

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + (dp[i-2] * 2)

print(dp[n] % 10007)