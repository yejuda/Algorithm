import sys
input= sys.stdin.readline

# n,m 입력 받기
n, m = map(int, input().split())
# 체스 정보 입력받기 
chess = [input().strip() for _ in range(n)]   # strip()을 해주지 않으면 공백이 포함됨(아래 인덱스 계산에서 문제 생김)

# 최소 덧칠할 횟수 정의
min_chess = 64

# 체스판의 패턴 정의
white_first = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

# 보드판 자르기(8*8) 
# 가능한 시작 위치를 제한해주기
# 시작점이 마지막 행에서 최소 8칸 떨어져있어야 한다. (인덱스로는 7)
for i in range(n-7):
    for j in range(m-7):
        # 덧칠할 횟수 초기화
        cnt = 0

        # 8*8 보드 확인 (처음부터 8개까지)
        # - (i, j)는 현재 탐색 중인 8*8 보드의 시작점
        # - (row, col)은 시작점으로부터 상대적인 위치
        # - 따라서, 전체 체스판에서 이 칸의 실제 위치는 (i+row, j+col)로 표현된다.
        for row in range(8):
            for col in range(8): 
                if chess[i+row][j+col] != white_first[row][col]:   # 현재 탐색 중인 칸이 White 시작 패턴과 다른지 확인하는 부분
                    cnt += 1

        # 덧칠 횟수가 더 작은 것을 선택
        # - 모든 8*8보드를 확인한 후 마지막에 한번만 실행 되어야 한다. 
        # - 모든 가능한 8*8 보드를 확인하면서 각 보드마다 계산된 cnt와 64-cnt 중 최소값을 갱신해야 한다.
        min_chess = min(cnt, min_chess, 64-cnt)   #  64-cnt: Black으로 시작하는 패턴에 맞추기 위해 다시 칠해야 하는 칸의 개수를 나타낸다.

print(min_chess)