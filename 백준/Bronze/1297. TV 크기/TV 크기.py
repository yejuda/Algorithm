# 대각선의 길이, 높이, 너비의 비율
d, h, w = map(int, input().split())

# 피타고라스 정리 - 비례상의 대각선 길이 계산
di = (h*h + w*w)**(1/2)

# 실제 크기로 환산하는 배율
ratio = d / di

# 높이, 너비 계산
height = int(h*ratio)
weight = int(w*ratio)

print(height, weight)