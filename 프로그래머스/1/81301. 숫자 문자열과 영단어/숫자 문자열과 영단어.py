def solution(s):
    
    # 딕셔너리 생성
    dict_n = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven",                 "8":"eight", "9":"nine"}

    for key, value in dict_n.items():
        s = s.replace(value, key)
        
    return int(s)

'''
문자열 s를 하나씩 탐색해가면서 딕셔너리에 있는 value값이 나올 때, 해당 key로 바꿔주는 방법을 생각했었다. 
하지만 코드가 너무 길어지고 시간 복잡도가 증가할 수도 있겠다는 생각이 들었다.

단순히 딕셔너리를 만들어준 후, 문자열(s)에 딕셔너리에 존재하는 value값이 있으면 해당 key로 바꿔줄 수 있었다.
'''