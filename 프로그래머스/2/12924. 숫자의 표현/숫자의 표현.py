from collections import deque

def solution(n):
    # 계산할 값 담을 큐(리스트) 초기화
    q = deque([])
    # 개수를 담을 변수 초기화
    cnt = 0
    # n까지 값을 순회하면서 더하기
    for i in range(1, n+1):
        q.append(i)
        
        q_sum = sum(q)
        
        # n보다 크면 (n보다 클때까지)왼쪽 수를 차례로 popleft
        while q_sum > n:
            q_sum -= q.popleft()
            
        
        # 큐 안의 값을 더한 것이 n과 같으면 개수 + 1
        if q_sum == n:
            cnt += 1
    
    return cnt