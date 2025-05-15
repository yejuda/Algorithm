# 그리디 알고리즘

n = int(input())
m = list(map(int, input().split()))
prefix_sum  = 0  # 부분합 누적
total = 0  # 전체 누적합

m.sort()

for i in m:
    prefix_sum += i  # 부분 누적합 기록
    total += prefix_sum  # 부분 누적합을 누적하면서 전체 누적합 기록

print(total)