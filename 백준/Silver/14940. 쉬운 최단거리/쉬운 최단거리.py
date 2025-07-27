#쉬운 최단거리

from collections import deque

n, m = map(int, input().split())  # 세로(행), 가로(열)

grid = [list(map(int, input().split())) for _ in range(n)]

# 거리를 담을 배열(기본 -1로 초기화)
dist = [[-1 for _ in range(m)] for _ in range(n)]


# 2가 있는 위치 찾기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            # dist 0으로 저장
            dist[i][j] = 0
            
        elif grid[i][j] == 2:
            # dist 0으로 저장
            dist[i][j] = 0
            loc_r, loc_c = i, j  # 시작 위치 저장


# 방향 설정(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs함수
def bfs(x, y):

    # 큐 생성
    queue = deque()
    # 현재 값 큐에 넣기
    queue.append((x, y))

    while queue:
        # 현재 값 빼기
        x, y = queue.popleft()
        
        # 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽에 도달하는 경우, 범위에서 벗어나는 경우 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            
            # 아직 방문하지 않았다면
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
    
# 2가 있는 위치부터 탐색 시작
bfs(loc_r, loc_c)

for r in range(n):
    print(*dist[r])