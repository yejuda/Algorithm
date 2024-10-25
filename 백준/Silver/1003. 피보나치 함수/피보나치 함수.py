# 동적 계획법
t = int(input())

# 최대 입력 값에 맞추어 DP 배열을 미리 생성한다. 
dp = [(0,0) for _ in range(41)]  #(fibo(0)호출 횟수, fibo(1)호출 횟수)\
dp[0] = (1, 0)   # fibo(0) 호출 시 
dp[1] = (0, 1)   # fibo(1) 호출 시

# DP를 이용하여 각 n에 대해 호출 횟수를 미리 계산한다.
for i in range(2, 41):
    dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])
    
for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])