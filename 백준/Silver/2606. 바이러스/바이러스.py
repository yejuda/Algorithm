# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력
# '서로 연결되어 있는' -> 양방향 연결을 의미

## DFS(재귀)
n = int(input())  # 노드 수
m = int(input())  # 간선 수

# 방문 확인 변수
visited = [False] * (n+1)
# 노드 정보(그래프 구조)
# 노드 개수만큼 생성되고 그 안에 노드와 연결 되어 있는 정보가 들어간다
graph = [[] for _ in range(n+1)]

# 1번컴퓨터와 연결되어 있는 컴퓨터 개수 세기
cnt = 0

# 노드 정보 입력해주기 
for _ in range(m): # 간선 수만큼
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)   # 양방향 연결이기 때문에!



# dfs 함수 생성
def dfs(node):
    # 전역 변수 선언
    global cnt

    # 현재 노드 방문 처리
    visited[node] = True

    for neighbor in graph[node]:  # 그래프를 순회하기(현재 노드와 연결되어 있는 노드들을 순회해야 함)
        if not visited[neighbor]:     # 만약 아직 방문하지 않은 노드라면
            dfs(neighbor)  # 재귀적으로 방문 처리
            cnt += 1

    return cnt


## BFS(deque)
from collections import deque

# bfs
def bfs(start):
    # 전역 변수 선언
    global cnt

    # 큐에 첫 노드 넣기
    queue = deque([start])
    # 첫노드 방문처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 노드 빼서 탐색
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                # 방문처리
                visited[neighbor] = True
                # 해당 노드 다시 큐에 넣기(이후 해당 노드와 연결되어 있는 노드들을 탐색하기 위해서)
                queue.append(neighbor)
                cnt += 1
    return cnt


# 1번 컴퓨터와 연결되어 있는 컴퓨터 수를 알기 위해서는 
# 1번 노드부터 시작했을 때 방문하는 컴퓨터 개수 
print(dfs(1))
print(bfs(1))
