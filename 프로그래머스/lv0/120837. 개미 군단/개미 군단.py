# def solution(hp):
    
#     first = hp // 5 
#     second = (hp - (5*first)) // 3
#     third = (hp - (5*first) - (3*second)) // 1
    
#     return first + second + third

def solution(hp):
    
    answer = 0
    answer = hp//5
    hp %= 5
    answer += hp//3
    hp %= 3
    answer += hp//1

    return answer