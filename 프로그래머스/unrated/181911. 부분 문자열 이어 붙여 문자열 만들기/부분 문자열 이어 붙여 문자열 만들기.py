def solution(my_strings, parts):
    answer = ''
    n = 0
    
    for string in my_strings:
        answer += string[parts[n][0]:parts[n][1]+1]
        n += 1
    
    return answer