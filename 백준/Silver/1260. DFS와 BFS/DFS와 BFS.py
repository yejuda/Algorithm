## 단, 방문할 수 있는 정점이 여러 개인 경우에는,
## 정점 번호가 작은 것을 먼저 방문(set을 활용하는 방법도 있음)
## 1. set은 중복을 허용하지 않는다. 2. 자동 정렬된다.(순서가 없음)

n, m, v = map(int, input().split()) 

# 방문 확인 변수(dfs, bfs따로 설정해두어야 함.)
visited1 = [False] * (n+1)  # dfs
visited2 = [False] * (n+1)  # bfs

# 노드 정보(그래프 구조)
# 노드 개수만큼 생성되고 그 안에 노드와 연결 되어 있는 정보가 들어간다
graph = [[] for _ in range(n+1)]

# 노드 정보 입력해주기 
for _ in range(m): # 간선 수만큼
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)   # 양방향 연결이기 때문에!

## 정렬
# 정점 번호가 작은 것을 먼저 방문해야 하기 때문에 '정렬' 해주기
for s in graph:
    s.sort()

# dfs 함수 생성
def dfs(v):

    # 현재 노드 방문 처리
    visited1[v] = True
    # 방문 후 정점 출력
    print(v, end = ' ')

    for neighbor in graph[v]:  # 그래프를 순회하기(현재 노드와 연결되어 있는 노드들을 순회해야 함)
        if not visited1[neighbor]:     # 만약 아직 방문하지 않은 노드라면
            dfs(neighbor)  # 재귀적으로 방문 처리


## BFS(deque)
from collections import deque

# bfs
def bfs(v):

    # 큐에 첫 노드 넣기
    queue = deque([v])
    # 첫노드 방문처리
    visited2[v] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 노드 빼서 탐색
        node = queue.popleft()
        # 방문 후 정점 출력
        print(node, end=' ')

        for neighbor in graph[node]:
            if not visited2[neighbor]:
                # 방문처리
                visited2[neighbor] = True
                # 해당 노드 다시 큐에 넣기(이후 해당 노드와 연결되어 있는 노드들을 탐색하기 위해서)
                queue.append(neighbor)



# 1번 컴퓨터와 연결되어 있는 컴퓨터 수를 알기 위해서는 
# 1번 노드부터 시작했을 때 방문하는 컴퓨터 개수 
dfs(v)
print()
bfs(v)