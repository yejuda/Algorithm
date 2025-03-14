# 배열 크기, 교환 횟수 입력
n, k = map(int, input().split())
# 배열 a 입력
a = list(map(int, input().split()))
# 현재 교환 횟수 count 변수
cnt = 0

# 배열 개수만큼 반복
for i in range(n):
    # 버블 정렬이기 때문에 처음부터 끝까지 하나씩 줄여나가면서 반복
    for j in range(n-1-i):
        # 만약, 현재 원소가 다음 원소보다 크다면
        if a[j] > a[j+1]:
            # 교환
            a[j], a[j+1] = a[j+1], a[j]
            # 현재 교환횟수 늘리기
            cnt += 1

            # 만약, 현재 교환횟수가 목표 교환횟수와 같다면
            if cnt == k:
                # 현재 배열 출력
                print(*a)
                # 종료
                exit()

# 반복을 다 돌았는데 현재교환횟수 != 목표 교환횟수면, -1출력
print(-1)