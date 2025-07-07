n = int(input())
num = list(map(int, input().split()))
dp = [1] * n  # 자기 자신 하나만 가지는 경우 1로 초기화

for i in range(1, n):  # 자기 자신의 경우를 뺐기 때문에 n-1길이만큼 순회
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
