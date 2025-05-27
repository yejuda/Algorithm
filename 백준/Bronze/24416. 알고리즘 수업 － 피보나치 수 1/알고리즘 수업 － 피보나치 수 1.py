n = int(input())

cnt = 0  #  fibo(1) 또는 fibo(2) 호출 횟수
cntdp = 0  # dp 연산 횟수

def fibo(n):
    global cnt

    if n == 1 or n == 2:
        cnt += 1  # fibo(1) 또는 fibo(2)가 실제로 호출된 횟수 (진짜 계산이 일어난 지점만 세야 함)
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# (0) 1 1 2 3 5 # 1, 2일때는 1을 리턴
def dpFibo(n):
    global cntdp
    
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cntdp += 1  # 점화식 계산 1회

    return dp[n]

fibo(n)
dpFibo(n)

print(cnt, cntdp)