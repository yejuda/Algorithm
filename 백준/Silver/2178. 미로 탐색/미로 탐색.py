# 미로 찾기
from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

# 이동할 방향(상,하,좌,우)
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 

# bfs함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 큐에 넣어주기

    # queue가 빌때까지
    while queue:
        x, y = queue.popleft()  # 큐에서 빼주기

        # 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위를 벗어나거나 벽에 도달하는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 이동할 수 없는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 이동할 수 있을 경우 + 1
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 현재 위치에 1을 더한 것을 새로운 위치에 넣어주기
                queue.append((nx, ny))  # 새로운 위치를 다시 큐에 넣어서 탐색
            
    return graph[n-1][m-1]


print(bfs(0, 0))