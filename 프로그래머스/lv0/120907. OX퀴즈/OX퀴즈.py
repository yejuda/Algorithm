def solution(quiz):
    answer = []
    for i in quiz:
        
        tmp = i.split()
        
        if tmp[1] == '+':
            r = int(tmp[0]) + int(tmp[2])
        else:
            r = int(tmp[0]) - int(tmp[2])
            
        if r == int(tmp[4]):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer