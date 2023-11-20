def solution(num):
    cnt = 0  # 횟수를 기록할 변수
    
    if num == 1:
        return 0
    
    while num != 1:     # num이 1이 아닐 때까지 반복
        
        if num%2 == 0:   # 짝수일경우
            num /= 2
            cnt += 1
        else:            # 홀수일경우
            num = (num * 3) + 1
            cnt += 1
            
        if cnt == 500:  # 작업을 500번 반복할 때까지 1이 되지 않는다면 -1 리턴
            return -1
        
    return cnt   
