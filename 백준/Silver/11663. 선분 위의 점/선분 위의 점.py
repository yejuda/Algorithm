import sys
input = sys.stdin.readline


n, m = map(int, input().split())
corr = sorted(map(int, input().split()))


# 선분 중 가장 작은 점의 인덱스 구하기(target 이상인 값의 시작점을 찾는다.)
def lower(arr, target):
    # 일단 arr의 절반 위치 인덱스 구해
    start = 0
    end = len(arr)

    # start가 end보다 작을 때까지 반복(이분탐색~)
    while start < end:
        mid = (start + end) // 2
        
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start


# 선분 중 가장 큰 점의 인덱스 구하기(target보다 큰 값들 중 가장 첫 번쨰 값을 찾는다.)
def upper(arr, target):
    # 일단 arr의 절반 위치 인덱스 구해
    start = 0
    end = len(arr)

    # start가 end보다 작을 때까지 반복(이분탐색~)
    while start < end:    
        mid = (start + end) // 2

        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start


for _ in range(m):
    a, b = map(int, input().split())
    left_idx = lower(corr, a)
    right_idx = upper(corr, b)
    print(right_idx - left_idx)
