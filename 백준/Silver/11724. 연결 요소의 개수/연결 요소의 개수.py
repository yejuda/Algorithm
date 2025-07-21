import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

# 연결요소 개수 변수
cnt = 0
# 노드 정보 담을 변수
graph = [[] for _ in range(n+1)]
# 방문 확인 변수
visited = [False] * (n+1)  # 노드 수만큼

# 노드 정보 입력받기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(x):
    # 현재 노드 방문 처리
    visited[x] = True

    # 현재 노드와 연결된 노드들 순회
    for node in graph[x]:
        if not visited[node]:
            dfs(node)


# 전체 노드를 살펴보는 반복문(아직 방문하지 않은 노드를 발견했을 때, cnt를 늘려주기 위함)
for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)

print(cnt)