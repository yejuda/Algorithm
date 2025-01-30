import sys
from typing import List  # Tuple

# 코테에서 재귀를 사용할 때는, 제한 설정해주기
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find_parent(n: int) -> List[int]:
    # 방문 처리 리스트
    visited = [False] * (n+1) 
    # 트리 정보 저장(인접리스트)
    tree = [[] for _ in range(n+1)]
    # 부모노드 저장할 정답 리스트
    result = [0] * (n+1)
    
    for _ in range(1, n):  # n-1개 입력 받기
        n1, n2 = map(int, input().split())
        # 양방향 인접리스트(트리에 정보 저장)
        tree[n1].append(n2)
        tree[n2].append(n1)
    
    
    def DFS(current: int) -> None:
        # 현재 노드 방문 처리
        visited[current] = True
        
        # current 노드에 연결된 노드들 순회
        for node in tree[current]:
            if not visited[node]:  # 아직 방문하지 않았다면,    
                # 다음 노드 방문하기 전에, 현재 노드를 부모 노드로 저장
                result[node] = current
                # 다음 노드로 이동(재귀를 통해 방문처리)
                DFS(node)
                
    DFS(1)  # 루트노드인 1번 노드부터 시작
    
    return result[2:]  # 2번 노드부터 끝까지 return


def main():
    n = int(input())
    answer = find_parent(n)    
    for parent in answer:
        print(parent)
    
    
if __name__ == '__main__':
    main()