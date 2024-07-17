def solution(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    # 0부터 n까지 총 n개의 배열 생김
    ans = [[0] for _ in range(n+1)]  
    
    ans[1] = 1  # 1가지
    ans[2] = 2  # 2가지
    
    for i in range(3, n+1):
        ans[i] = ans[i-1] + ans[i-2]
        
    return ans[n] % 1234567