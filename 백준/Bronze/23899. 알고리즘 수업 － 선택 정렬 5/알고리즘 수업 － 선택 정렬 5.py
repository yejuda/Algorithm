### 인덱스로만 비교!!! ###

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp = 0  # 교환을 위한 변수

if a == b:
    print(1)
    exit()

# 배열 a의 마지막 원소부터 시작(N부터 인덱스 1까지)
for last in range(n-1, 0, -1):  
    # 배열 시작부터 현재 원소(last)부까지 최댓값 인덱스 찾기
    max_idx = a.index(max(a[:last+1]))

    # 현재 원소(last)인덱스가 최댓값 인덱스와 같지 않다면, 교환한다.
    if last != max_idx:
        a[last], a[max_idx] = a[max_idx], a[last]
        
        # 한번 교환할 때마다 배열 b와 같은지 비교 
        # 같으면 1을 출력하고 종료.
        if a == b:
            print(1)
            exit()
        # 다르면, 계속 진행

# 끝까지 진행했는데 같은게 없었으면 0을 출력
print(0)