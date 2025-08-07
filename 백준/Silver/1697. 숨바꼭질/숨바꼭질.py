from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001

def bfs(n, h):  # 시작 위치
    queue = deque([(n, 0)])  # 시작 위치와 시간 넣고 시작
    visited[n] = True  # 방문처리

    while queue:
        curr_loc, h = queue.popleft()
        
        if curr_loc == k:
            return h
        
        # 이동 위치 계산
        next_loc1 = curr_loc - 1
        next_loc2 = curr_loc + 1
        next_loc3 = curr_loc * 2

        if 0 <= next_loc1 <= 100000 and not visited[next_loc1]:
            visited[next_loc1] = True
            queue.append((next_loc1, h + 1))

        if 0 <= next_loc2 <= 100000 and not visited[next_loc2]:
            visited[next_loc2] = True
            queue.append((next_loc2, h + 1))

        if 0 <= next_loc3 <= 100000 and not visited[next_loc3]:
            visited[next_loc3] = True
            queue.append((next_loc3, h + 1))           

print(bfs(n, 0))