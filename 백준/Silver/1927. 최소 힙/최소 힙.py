import heapq
import sys

input = sys.stdin.readline

n = int(input())  #연산의 개수
result = []

for _ in range(n):
    # x입력받기
    x = int(input())
    
    # 만약 x가 자연수라면, 배열에 x라는 값을 넣는 연산
    if x > 0:
        heapq.heappush(result, x)  # result 배열에 x를 넣는다. -> 최소 힙으로 들어감
    
    # x가 0이라면, 가장 작은 값을 출력하고 그 값을 배열에서 제거
    elif x == 0:
        if result: 
            print(heapq.heappop(result))  # 가장 작은 원소를 pop 및 출력
        else:   # result가 비어있는 경우
            print(0)
        
        