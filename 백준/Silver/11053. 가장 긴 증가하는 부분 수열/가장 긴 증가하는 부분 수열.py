n = int(input())
num = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)  # num[i]가 새로운 원소로 추가되므로 dp[j] + 1 

print(max(dp))