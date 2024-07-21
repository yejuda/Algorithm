# dfs - 재귀
# bfs - while deque
# BFS - 최단거리, 두 노드 사이의 거리를 구하는 문제.
# DFS - 경로 존재유무,가능한 모든 경로를 탐색하며 조건을 만족하는 경로를 찾는 문제(백트래킹)

# 1번 노드로부터 가장 멀리 떨어진 노드가 몇개인지? = 최단경로로 이동헸을 때 간선의 개수가 가장 많은 노드

from collections import deque

def solution(n, edge):
    # answer = 0
    
    # 노드와 간선 정보를 담을 빈 리스트 생성
    graph = [[] for _ in range(n+1)]  # 7개
    # visit 변수 생성
    visit = [0]*(n+1)

    # 변수 담기(각 노드마다 간선 정보 담기)
    for i in edge:  # 0~6(7개)  간선수만큼 반복
        graph[i[0]].append(i[1])  
        graph[i[1]].append(i[0])
    
    # 큐 생성
    q = deque([1])  # 시작노드 넣어주기
    
    # 시작노드(1번 노드) 방문처리(= 1)
    visit[1] = 1
        
    while q:  # q가 비어있지 않을 때까지
        # q의 왼쪽값 popleft()
        n = q.popleft()
        
        # 연결 정보 순회
        for j in graph[n]:  # pop한 노드와 연결되어 있는 노드 가져오기
            # 방문하지 않았다면 
            if not visit[j]:
                q.append(j)  # 큐에 추가
                visit[j] = visit[n] + 1  # 인접 노드 j의 거리 업데이트
                
    distance = max(visit)
        
        
    return visit.count(distance)




