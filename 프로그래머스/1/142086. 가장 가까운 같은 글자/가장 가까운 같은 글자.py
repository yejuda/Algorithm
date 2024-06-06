# 딕셔너리 활용?
# '현재 인덱스 - 해당 문자열이 있는 인덱스' -> 몇 칸 앞에 있는지 알 수 있음

def solution(s):
    answer = []
    s_idx = {}  # 순회하면서 문자를 담을 변수
    
    for index, letter in enumerate(s):
        # s_idx에 동일한 문자(letter)가 없으면
        if letter not in s_idx:
            answer.append(-1)
        else:
            answer.append(index - s_idx[letter])
        
        # 현재 문자의 마지막 인덱스를 현재 인덱스로 업데이트
        s_idx[letter] = index
        
        
    return answer