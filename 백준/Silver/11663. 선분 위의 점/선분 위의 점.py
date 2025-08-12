import sys
input = sys.stdin.readline


n, m = map(int, input().split())
corr = sorted(map(int, input().split()))

# B 이하 - A 미만  --> 이 범위에 점의 좌표 값이 몇개 있는가?
# 두 인덱스의 차이가 [A, B] 범위에 속하는 점 개수이다.

# 점들 중 a이상인 첫번째 점의 위치
def lower_b(arr, target):
    # 0부터 arr의 길이까지
    low = 0
    high = len(arr)
    while low < high:
        mid = (high + low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


# 점들 중 b 초과인 첫번째 점의 위치(그래야 인덱스 상으로 범위 안에 속함)
def upper_b(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (high + low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


for _ in range(m):
    a, b = map(int, input().split())
    left_idx = lower_b(corr, a)
    right_idx = upper_b(corr, b)
    print(right_idx - left_idx)


# for _ in range(m):
#     cnt = 0
#     a, b = map(int, input().split())

#     for i in corr:
#         if a <= i <= b:
#             cnt += 1

#     print(cnt)