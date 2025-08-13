import heapq, sys  # heapq가 가장 작은 값을 반환하고 제거를 해준다.
input = sys.stdin.readline

n = int(input())
li = []

# "최소힙"
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(li, (abs(x), x))  # (절대값, 원래값) 형태로 저장  # heapq는 첫번째 요소 기준으로 정렬된다.
    else:
        if not li:   # 리스트가 비어있으면
            print(0) # 0출력
        else:
            print(heapq.heappop(li)[1])