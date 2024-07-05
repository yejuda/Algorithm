def solution(s):
    # 빈리스트 생성
    stack = []
    
    # 스택
    # 문자를 하나씩 넣어가면서 탐색
    
    for i in s:
        if i == '(':
            stack.append(i)
            
        elif i == ')':
            if stack and stack[-1] == '(':  # stack이 비어있지 않고, stack의 마지막 문자가 여는 괄호이면
                stack.pop() # stack에 있는 여는 괄호를 pop(제거)
                
            else:  # 짝이 맞지 않거나 닫는 괄호가 더 많은 경우
                return False
    
    # stack이 다 비었으면 True
    return len(stack) == 0  # return not stack
                
            