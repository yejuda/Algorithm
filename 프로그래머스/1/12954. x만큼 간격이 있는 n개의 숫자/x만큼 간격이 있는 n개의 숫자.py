def solution(x, n):
    answer = []
    
    answer.append(x)  # 첫 숫자 넣기
    
    for i in range(0, n-1):
        n = x + answer[i]
        answer.append(n)
    return answer