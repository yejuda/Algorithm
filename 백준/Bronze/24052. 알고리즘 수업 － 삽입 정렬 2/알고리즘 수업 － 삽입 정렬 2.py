n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(1, n):

    loc = i - 1  
    newItem = a[i]  

    while (loc >= 0) and (newItem < a[loc]):
        a[loc + 1] = a[loc]
        cnt += 1  # 원소가 새 위치에 기록될 때마다 카운트
            
        if cnt == k:
            print(*a)
            exit()
        loc -= 1
        
    # 최종 삽입
    if (loc + 1 != i):  # 이동이 있었을 때만
        a[loc + 1] = newItem
        cnt += 1
            
        if cnt == k:
            print(*a)
            exit()     


print(-1)