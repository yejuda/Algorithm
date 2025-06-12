import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    # dp테이블 정의
    dp = [0] * 12

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[n])
