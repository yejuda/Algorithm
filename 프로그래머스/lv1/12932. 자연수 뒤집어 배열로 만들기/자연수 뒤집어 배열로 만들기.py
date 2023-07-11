def solution(n):
    List = []
    
    for i in str(n):         # 숫자를 문자열로 변환한 후("12345")
        List.append(int(i))  # 각 문자를 정수로 변환하여 리스트에 저장.
        
    return List[::-1]

