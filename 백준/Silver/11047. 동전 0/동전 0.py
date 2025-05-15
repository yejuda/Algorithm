# 그리디 알고리즘
# 우선 목표 값보다 큰 가격은 제외시킨다.
# 그리고 남은 수 중 가장 큰 가격으로 목표값의 몫을 구하고 cnt에 넣는다.
    # 나머지도 구해서 목표 값을 업데이트한다. 

n, k = map(int, input().split())  
money = []
cnt = 0  # 필요한 동전의 개수

for _ in range(n):
    a = int(input())
    # 목표 값보다 작은 값만 넣는다.
    if a <= k:
        money.append(a)

for i in reversed(money):
    if k == 0:
        break
    # 개수 누적해나감
    cnt += k // i
    # 목표값 업데이트
    k %= i

print(cnt)