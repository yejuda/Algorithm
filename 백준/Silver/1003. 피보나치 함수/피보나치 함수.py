


# 1. 최대 입력값에 맞추어 DP 배열을 미리 생성
dp = [(0, 0) for _ in range(41)]    # 40개의 dp배열이 생성됨


# 2. 0과 1인 경우는 미리 지정해주기(정해져 있는 값이기 떄문에)
dp[0] = (1, 0)
dp[1] = (0, 1)


# 3. DP를 이용하여 각 n에 대해 호출 횟수를 미리 계산
# 3번 인덱스의 0,1횟수는 이전과 이이전의 값을 더한 것이 횟수가 된다.
for i in range(2, 41):
    # 미리 횟수 계산
    dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1])


# 4. 숫자를 입력받아 0과 1의 리턴 수 반환
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])