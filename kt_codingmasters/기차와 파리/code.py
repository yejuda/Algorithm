x, y, z = map(int, input().split())

# 충돌 시간 계산
time = x / (2*y)

# 파리의 이동 거리
distance = int(time*z)  # 소수점 버림

print(distance)
