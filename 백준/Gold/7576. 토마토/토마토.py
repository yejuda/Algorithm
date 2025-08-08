# 저장될 때부터 모든 토마토가 익어있는 상태 -> 0 출력
# 토마토가 모두 익지는 못하는 상황이면 -> -1출력
    # 이 상황은 집단이 끊기는 경우! 즉, 더이상 이동할 수 없는 경우!

from collections import deque
import sys

input = sys.stdin.readline


m, n = map(int, input().split())  # 가로, 세로
tomato = [list(map(int, input().split())) for _ in range(n)]

# 큐 생성
queue = deque([])

# 초기 익은 토마토 찾기(우선 tomato 전체 순회)
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))  # 큐가 모든 출발점으로 채워진 상태로 bfs가 시작


# bfs 실행
def bfs():

    while queue:
        x, y = queue.popleft()

        # 이동방향 정의
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 이동하면서 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동할 수 있는 경우
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1  # 토마토 값을 '현재 위치의 날짜 +1'로 업데이트하고
                queue.append((nx, ny))  # 큐에 넣기


# bfs 호출
bfs()


# 배열 전체 순회하면서 익지 않은 토마토 있는지 확인
result = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        # 익은 토마토가 있으면(0이 아니라면) 최댓값 업데이트
        result = max(result, tomato[i][j])

# 모든 토마토가 익은 경우
print(result - 1)