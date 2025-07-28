# 가능한 모든 강수량에 대해서 각각 안전 영역의 개수를 세어보기 -> 그중에서 가장 큰 값을 찾기
# 모든 높이에 대해 반복 -> 최대값 찾기

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
region = [list(map(int, input().split())) for _ in range(n)]

# 지역의 최대 높이 찾기
max_height = 0
for r_list in region:
    max_height = max(max_height, max(r_list))  # 이중리스트 -> 내부리스트 안에서 최대값을 찾아야 함

# 초기 최대 안전 영역 개수
max_safe_area = 0


def bfs(start_row, start_col, curr_rain_h, visited):
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True

    # 이동방향 정의(상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 지도 범위 내에 있는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 아직 방문하지 않았고 현재 강수량보다 높으면
                if not visited[nx][ny] and region[nx][ny] > curr_rain_h:
                    visited[nx][ny] = True  # 방문처리
                    queue.append((nx, ny))
                
# 모든 강수량에 대해 반복(0부터 최대 높이까지)
for h in range(max_height + 1):
    # 방문 확인 변수(각 강수량에 대한~~)
    visited = [[False]*n for _ in range(n)]
    # 잠기지 않은 영역(덩어리) 개수
    curr_safe_area = 0

    for i in range(n):
        for j in range(n):
            # 해당 지역이 잠기지 않고 아직 방문하지 않았다면
            if region[i][j] > h and not visited[i][j]:
                # bfs를 시작하자.
                bfs(i, j, h, visited)
                curr_safe_area += 1  # bfs가 한번 끝나면 안전 영역 개수 증가

    # max_safe_area 초기화
    max_safe_area = max(max_safe_area, curr_safe_area)

# 지역 높이가 모두 0일 경우
if max_safe_area == 0 and n> 0:
    max_safe_area = 1

print(max_safe_area)