from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]  # 정보 입력받기(2차원)

# 이동 방향(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 하나의 단지를 탐색
def bfs(x, y):
    count = 1 # 현재 단지 내의 집의 수(시작점 포함)
    queue = deque([(x, y)])  # 큐 생성 및 큐에 현재 위치 넣어주기
    graph[x][y] = 0  # 방문한 집은 0으로 표시해 다시 방문하지 않도록 해주기

    # 큐가 빌 때까지
    while queue: 
        x, y = queue.popleft()

        # 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                count += 1

    return count  # 단지하나를 다 돌았을 때, 단지 내의 집의 수가 return 된다.


# 단지내 집의 수를 단지별로 저장    
complex_cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 1일 때 단지 탐색
            complex_cnt.append(bfs(i, j))


complex_cnt.sort()
print(len(complex_cnt))
for c in complex_cnt:
    print(c)