# "게임에서 얻을 수 있는 총 점수의 최댓값"
# 다이나믹 프로그래밍
# 가능한 경로 중 최대 점수 얻는 방법을 dp로 차근차근 쌓아감

n = int(input())

# 점수 입력 받기
score = [int(input()) for _ in range(n)]

# dp초기화
dp = [0] * (n)

if n <= 2:  # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(score))  

# 3개 이상인 경우
else:
    # 1번째, 2번째 계단 초기화
    dp[0] = score[0]
    dp[1] = score[0] + score[1]

    for i in range(2, n):  # 3번째 계단부터 dp점화식을 이용해서 풀기
        dp[i] = max(dp[i-3] + score[i-1] + score[i],  # i-3까지의 계단 점수 최댓값과 i-1, i 계단의 합
                    dp[i-2] + score[i])  # i-2까지의 계단 점수 최댓값과 i 계단의 합
    print(dp[-1])