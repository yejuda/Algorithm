import sys
input = sys.stdin.readline

w, h = map(int, input().split())
line_cnt = int(input())  # 잘라야 하는 점선의 개수

# 시작과 끝점 넣어두기
horizontal_cut = [0, h]  # 가로는 세로 끝점
vertical_cut = [0, w]

for _ in range(line_cnt):
    wh, num = map(int, input().split())
    
    # 위치값(num)을 넣어주기
    if wh == 0:
        horizontal_cut.append(num)
    else:
        vertical_cut.append(num) 

# 정렬
horizontal_cut.sort()
vertical_cut.sort()

# 각 위치값의 차이를 계산하기
max_h = 0
max_w = 0

for i in range(1, len(horizontal_cut)):
    # 현재 위치와 이전 위치 사이의 간격
    diff = horizontal_cut[i] - horizontal_cut[i-1]
    if diff > max_h:
        max_h = diff

for i in range(1, len(vertical_cut)):
    diff = vertical_cut[i] - vertical_cut[i-1]
    if diff > max_w:
        max_w = diff


print(max_h*max_w)