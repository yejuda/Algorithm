# 테스트 케이스 수 
t = int(input())

for _ in range(t):
    # 괄호 정보 입력 받기
    a = input()
    # 스택 초기화
    stack = []

    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:                # 스택이 비어있는 경우
                stack.append(i)  # 스택의 불균형을 위해(스택이 비어있지 않아야 NO가 나온다.)
                break
    
    # 스택이 비어있는지 확인
    if not stack:
        print("YES")
    else:
        print("NO")
