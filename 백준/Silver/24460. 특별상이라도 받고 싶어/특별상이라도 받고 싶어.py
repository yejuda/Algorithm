n = int(input())
arr = [list(map(int, input().split()))  for _ in range(n)]

# 재귀로 구간을 분할한다.
def recursive(start_row, start_col, size):
    global arr

    if size == 1:
        return arr[start_row][start_col]  # 해당 칸의 값을 반환하기(그 값을 호출했던 상위 재귀 함수로 전달된다.)
    
    # 4개의 부분 배열의 시작점을 계산
    half_size = size // 2  
    left_top = recursive(start_row, start_col, half_size)   # 좌상단
    right_top = recursive(start_row, start_col+half_size, half_size)  # 우상단(원래 배열의 시작 열인 start_col에서 half_size만큼 이동해야, 우상단 부분 배열의 시작열이 된다.)
    left_bottom = recursive(start_row+half_size, start_col, half_size)  # 좌하단
    right_bottom = recursive(start_row+half_size, start_col+half_size, half_size)  # 우하단

    # 각 영역에서의 '두 번째로 작은 값'(4개)을 모으로 정렬한 다음, 그중에서 2번째로 작은 값을 찾아 반환
    tmp = sorted([left_bottom,left_top,right_bottom,right_top])[1]

    return tmp

print(recursive(0, 0, n))
