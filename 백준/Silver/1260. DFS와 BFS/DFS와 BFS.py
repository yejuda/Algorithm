from collections import deque

# 정점이 작은 것을 먼저 방문해야 하기 때문에 list가 아닌 set을 사용
# 1. set은 중복을 허용하지 않는다. 2. 자동 정렬된다(순서가 없음)

# 정점개수, 간선개수, 탐색시작 정점 번호 입력 받기
n, m, s = map(int, input().split())

# 방문 확인 변수
visited1 = [False]*(n+1)   # dfs
visited2 = [False]*(n+1)   # bfs

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 간선 연결 정보 받기
# 그래프에 노드와 간선 정보 넣기
for _ in range(m):   # 간선 수만큼 반복
    # 노드와 간선 정보 입력받기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향

# 각 리스트를 정렬하여 작은 정점을 먼저 방문하도록 설정
for edges in graph:
    edges.sort()


# BFS #### deque, while
def bfs(s):
    # 방문한 곳을 순서대로 넣을 큐
    q = deque([s])  # 첫번째 노드 넣음

    # 방문 처리
    visited2[s] = True
    
    while q:  # 큐가 비어있을 때까지
        # 왼쪽에 있는 값 pop
        s_pop = q.popleft()
        print(s_pop, end = ' ')

        for i in graph[s_pop]:  # pop한 노드와 연결되어 있는 노드 가져오기
            if not visited2[i]:
                q.append(i) # 큐에 추가
                visited2[i] = True # 방문처리


# DFS
def dfs(s):
    # 방문처리
    visited1[s] = True
    # 방문 후 정점 출력
    print(s, end= ' ')
    
    # 현재 노드에 연결되어 있는 노드 탐색하면서 방문처리
    for i in graph[s]:  # s번 노드에 연결된 모든 노드를 반복
        if not visited1[i]: # 방문하지 않았다면
            # 재귀를 통해 방문처리
            dfs(i)


dfs(s)
print()
bfs(s)