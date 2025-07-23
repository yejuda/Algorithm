
# 피보나치 수를 어떤 수 m으로 나눈 나머지는 주기를 가진다. -> 피사노 주기

n = int(input())


def fibo(n):
    mod = 10**6  # 피보나치 수를 나눌 값
    p = 15*10**5 # 피사노 주기

    n %= p # 우리가 구해야 할 값

    dp = [0] * (n+2)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % mod

    return dp[n]


print(fibo(n))