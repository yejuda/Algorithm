import heapq, sys
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(li, -x) # -를 붙여서 최대힙으로 사용할 수 있게끔
    else:
        if not li:
            print(0)
        else:
            print(-heapq.heappop(li)) # 최대값 리스트에서 뺀 후 출력


# for _ in range(n):
#     x = int(input())

#     if x == 0 and li:
#         print(max(li))  # 가장 큰 값을 출력
#         li.remove(max(li)) # 그 값 제거

#     # 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우
#     elif x == 0 and not li:
#         print(0)
#     # x가 자연수일 경우
#     else:
#         li.append(x)