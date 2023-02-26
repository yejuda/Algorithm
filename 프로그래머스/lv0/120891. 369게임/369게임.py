def solution(order):
    answer = 0
    number = ['3', '6', '9']
    for i in str(order):
        
        if i in number:
            answer += 1
            
    return answer