# 저장될 때부터 모든 토마토가 익어있는 상태 -> 0 출력
# 토마토가 모두 익지는 못하는 상황이면 -> -1출력
    # 이 상황은 집단이 끊기는 경우! 즉, 더이상 이동할 수 없는 경우!

from collections import deque
import sys

input = sys.stdin.readline


# 가로, 세로, 높이 입력
m, n, h = map(int, input().split())

# 3차원 토마토 창고 (높이, 세로, 가로)
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 큐 생성
queue = deque([])
# 익은 토마토 개수
unripe_count = 0

# 초기 익은 토마토 찾기 및 익지 않은 토마토 개수 세기
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j))
            elif tomato[k][i][j] == 0:
                unripe_count += 1


# BFS 함수 정의
def bfs():
    # 6가지 이동 방향 (상, 하, 좌, 우, 위, 아래)
    dk = [0, 0, 0, 0, 1, -1]
    di = [-1, 1, 0, 0, 0, 0]
    dj = [0, 0, -1, 1, 0, 0]
    
    while queue:
        k, i, j = queue.popleft()
        
        # 6가지 방향으로 탐색
        for move in range(6):
            nk, ni, nj = k + dk[move], i + di[move], j + dj[move]
            
            # 범위 내에 있고, 아직 익지 않은 토마토인 경우
            if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m and tomato[nk][ni][nj] == 0:
                # 익은 날짜를 업데이트하고 큐에 추가
                tomato[nk][ni][nj] = tomato[k][i][j] + 1
                queue.append((nk, ni, nj))

# BFS 실행
bfs()

# 모든 토마토가 익었는지 확인 및 최댓값 계산
max_days = 0
is_all_ripen = True

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:
                is_all_ripen = False
                break
            max_days = max(max_days, tomato[k][i][j])
        if not is_all_ripen:
            break
    if not is_all_ripen:
        break

if not is_all_ripen:
    print(-1)
else:
    print(max_days - 1)