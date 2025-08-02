n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
answer = 0

while start <= end:
    total_length = 0

    mid = (start + end) // 2   # 절단 높이 H

    # mid 높이로 잘랐을 때 얻는 나무 길이 계산
    for t in tree:
        if t > mid:
            total_length += (t-mid)
            # 이미 m을 넘었다면 더 이상 계산할 필요 없음
            if total_length >= m:
                break

    # 필요한 m미터 이상의 나무를 얻은 경우
    if total_length >= m:
        answer = mid  # 정답 후보 저장

        # 더 높은 높이로 잘라도 되는지 확인
        start = mid + 1
    
    # m미터보다 나무가 부족한 경우
    else:
        end = mid - 1


print(answer)