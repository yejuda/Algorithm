import sys
sys.setrecursionlimit(10**6)

n = int(input())                  # 전체 사람의 수(=노드 수)
a, b = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())                  # 부모 자식들 간의 관계의 개수(=간선)

visited = [False] * (n+1)  # 방문한 노드 확인
graph = [[] for _ in range(n+1)]  # 각 노드별 연결된 촌수 넣을 변수

# 촌수 정보 넣기
for _ in range(1, m+1):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

# dfs 함수
def dfs(number, depth):  # dfs(현재 노드, cnt, 현재 깊이)

    if number == b:
        return depth

    # 현재 노드 방문처리
    visited[number] = True

    # 현재 노드에 연결된 노드들 순회
    for node in graph[number]:
        if not visited[node]:  # 아직 방문하지 않은 노드라면
            # 재귀로 더 깊이 탐색
            result = dfs(node, depth+1)
            
            # 재귀 호출 결과가 -1이 아니라면, (b를 찾았다면)
            if result != -1:
                return result

    # b에 도달하지 않은 경우 -1출력        
    return -1
            

print(dfs(a, 0))  # a에서 출발해서 b까지 도달을 하는가?