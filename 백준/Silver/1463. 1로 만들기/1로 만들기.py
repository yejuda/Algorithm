# dp는 1부터 x까지 올라가면서 각 수를 1로 만드는 최소 연산 횟수를 차례로 채워가는 방식이다.

x = int(input())

dp = [0] * (x+1)  # dp[i]는 i를 1로 만드는데 필요한 최소 연산 횟수

for i in range(2, x+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # i // 2연산을 했기 때문에 1을 더해준다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
print(dp[x])