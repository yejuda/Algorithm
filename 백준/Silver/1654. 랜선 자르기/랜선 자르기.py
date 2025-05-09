# 주어진 각 랜선을 같은 길이로 잘라야 한다.
# 합이 목표 개수 n이상인지 확인 -> 이분 탐색 조건

# 이미 가지고 있는 랜선개수, 필요한 랜선 개수
k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

# 초기 범위 설정
start = 1
end = max(lines)
result = 0  # 만들 수 있는 최대 길이 저장

# start가 더 크면 더이상 가능한 길이가 없음을 뜻한다.
while start <= end:
    # 중간 길이 설정
    mid = (start + end) // 2

    cnt_line = 0

    for line in lines:
        cnt_line += (line // mid)

    # 더 긴 길이로 자를 수 있는 경우
    if cnt_line >= n:
        result = mid  # 가능한 길이 중 최대를 저장(계속 갱신)
        start = mid + 1  # 더 길게 해도 되나? 확인
    # (cnt_line < n) -> 너무 많이 자른 경우
    else: 
        end = mid - 1

print(result)