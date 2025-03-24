n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(1, n):

    loc = i - 1  # 4
    newItem = a[i]  # 5 

    while (0 <= loc) and (newItem < a[loc]):
        a[loc + 1] = a[loc]
        cnt += 1  # 원소가 새 위치에 기록될 떼마다 카운트
            
        if cnt == k:
            print(a[loc+1])
            exit()
        loc -= 1
        
    # 최종 삽입
    if (loc + 1 != i):  # 이동이 있었을 때만
        a[loc + 1] = newItem
        cnt += 1
            
        if cnt == k:
            print(a[loc+1])
            exit()       


print(-1)