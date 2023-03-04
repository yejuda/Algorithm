# 단순 역순 출력해서 다른 문자와 같은지 확인하는 문제가 아님.
# 순서를 뒤죽박죽 아무렇게나 섞어서 다른 문자가 나와도 만들 수 있다고 판단해야 하는 문제임.

def solution(before, after):
    answer = 0
    
    # 정렬을 했을 때, 두 문자가 같으면 1 아니면 0
    a = sorted(before)
    b = sorted(after)
    
    if a == b:
        answer = 1
    else:
        answer = 0
    
    return answer

