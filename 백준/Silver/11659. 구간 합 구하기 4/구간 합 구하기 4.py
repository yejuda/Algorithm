# 슬라이싱을 통해서 합을 구하는 건 시간 초과 발생 -> 누적합 사용

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 구간합
prefix_sum = [0] * (n+1)
# 구간합 배열 채우기
for k in range(n):
    prefix_sum[k+1] = prefix_sum[k] + nums[k]

for _ in range(m):  # 합을 구해야 하는 횟수 m
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i-1])

    