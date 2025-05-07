# 이분 탐색으로 풀어야 해.

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

start = 1
end = max(lines)
result = 0  # 만들 수 있는 최대 길이 저장


# 계속 잘라가면서 비교
while start <= end:   # start가 더 작거나 같을 때까지 반복(그게 넘어가면 비교할 필요 없음 start가 더 클 수 없음)
    # 중간 길이 구하기
    mid = (start + end) // 2

    cnt_line = 0

    # 길이를 돌아가면서 저장
    for line in lines:
        cnt_line += (line // mid)

    # 더 긴 길이로 자를 수 있는 경우(현재는 길이가 짧기 떄문에 cnt_line이 개수가 더 많아진 것이다.)
    if cnt_line >= n:
        result = mid
        start = mid+1
    # 너무 많이 자른 경우
    else:
        end = mid-1

print(result)