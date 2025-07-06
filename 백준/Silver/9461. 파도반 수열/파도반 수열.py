t = int(input())

for _ in range(t):
    n = int(input())

    dp = [0] * max(6, n+1)  # n이 6보다 작으면 6칸짜리 리스트 만들도록

    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2

    if n <= 5:
        print(dp[n])
        continue

    for i in range(6, n+1):

        dp[i] = dp[i-1] + dp[i-5]

    print(dp[n])