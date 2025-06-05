# "게임에서 얻을 수 있는 총 점수의 최댓값"
# 다이나믹 프로그래밍

n = int(input())

# 계단 점수 입력
scores = [int(input()) for _ in range(n)]

# 1. dp 테이블를 정의한다.
dp = [0] * (n + 1)


if n == 1:
    print(scores[0])
elif n == 2:
    print(scores[0] + scores[1])
else:
    # 2️. dp 테이블의 초기값 계산한다.
    dp[1] = scores[0]
    dp[2] = scores[0] + scores[1]
    # 3️. 점화식에 따라 각 계단에 대한 dp 테이블을 채워준다.
    for i in range(3, n+1):
        dp[i] = max(scores[i-1] + dp[i-2], dp[i-3] + scores[i-2] + scores[i-1])

    # 4️. dp 테이블의 마지막 값을 출력한다.
    print(dp[-1])
