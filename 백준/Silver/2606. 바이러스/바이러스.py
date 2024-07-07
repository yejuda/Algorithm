

# 컴퓨터 수(노드 수)
n = int(input())
# 간선 수
v = int(input())

# 방문 확인 변수 초기화(DFS)
visited = [False]*(n+1)

## 데이터 입력 받기
# 빈 리스트 초기화
graph = [[] for _ in range(n+1)]

for _ in range(v):  # 간선 수만큼 반복
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향일 경우 사용


# DFS 함수 생성
def dfs(val):
    # 현재 노드 방문처리
    visited[val] = True

    # 현재 노드(val)와 연결되어 있는 다른 노드 재귀적으로 방문
    for i in graph[val]:
        # 만약, 방문하지 않았다면(visited에 해당 노드가 없다면) / False이면,
        if not visited[i]:
            # 재귀함수 사용해서 방문처리
            dfs(i)


dfs(1)

# 실제로 방문한 노드 수(True) 출력
print(visited.count(True)-1)

