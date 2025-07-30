w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 벽이 있어서 주기를 가지고 움직인다. -> 주기는 2w(2h)이다. (왔다갔다하기 때문에!) -> 즉 , (current_p + t) % 2*w

# x축 최종 위치 계산
x = 2*w
# 총 거리를 주기로 나눈 나머지
remain_x = (p + t) % (2 * w)

# 개미가 0 -> w 방향으로 이동중이거나 w에 도달한 상황
if remain_x <= w:
    final_p = remain_x  
# 개기가 w -> 0 방향으로 되돌아오고 있는 상황
elif remain_x > w:
    final_p = (2*w) - remain_x


y = 2*h
# 총 거리를 주기로 나눈 나머지
remain_y = (q + t) % (2 * h)

# 개미가 0 -> h 방향으로 이동중이거나 h에 도달한 상황
if remain_y <= h:
    final_q = remain_y  
# 개기가 h -> 0 방향으로 되돌아오고 있는 상황
elif remain_y > h:
    final_q = (2*h) - remain_y


print(final_p, final_q)