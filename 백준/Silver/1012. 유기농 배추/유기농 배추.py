# 그리드 형태의 그래프에서는 간선 수를 따로 계산하거나 저장할 필요가 없다.
# 탐색을 진행하면서 그때그때 이동 가능한 이웃노드(간선)을 찾아가는 방식으로 구현

# 재귀 깊이 제한 늘려주기
import sys
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
    m, n, k = map(int,input().split())  # 가로길이, 세로길이, 배추가 심어져있는 위치의 개수
    cnt = 0  # 배추 덩어리 개수

    # 방문 확인 변수(2차원 배열로)
    visited = [[False] * m for _ in range(n)]

    # 밭(그리드)를 나타내는 2차원 배열 만들기(0으로 초기화)
    graph = [[0]*m for _ in range(n)]

    # 2차원 배열의 입력받은 위치에 배추있음을 표시하기
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1  # graph[세로][가로]


    # 탐색 시작(DFS)
    def dfs(h, w):
        # 현재 칸 방문처리
        visited[h][w] = True

        # 이동 방향 정의
        dh = [-1, 1, 0, 0]  # 상, 하
        dw = [0, 0, -1, 1]  # 좌, 우

        # 네 방향 탐색
        for i in range(4):  # 4가지 방향(상,하,좌,우)
            nh, nw = h + dh[i], w + dw[i]  # 다음 칸의 세로(nh), 가로(nw) 좌표 계산

            # 밭이 범위 내에 있는지, 배추가 심어져 있는지, 아직 방문하지 않았는지
            if 0 <= nh < n and 0 <= nw < m and graph[nh][nw] == 1 and visited[nh][nw] == False:
                dfs(nh, nw)


    # 밭의 모든 칸 셀을 하나씩 순회
    for i in range(n):      # 세로
        for j in range(m):  # 가로
            if graph[i][j] == 1 and visited[i][j] == False:  # 현재칸에 배추가 심어져있고, 아직 방문하지 않았다면 --> 새로운 배추 덩어리의 시작점!

                cnt += 1    # 새로운 배추 덩어리의 시작이기 때문 및 새로운 배추 덩어리 발견!

                # 탐색 시작
                dfs(i, j)
    
    print(cnt)

