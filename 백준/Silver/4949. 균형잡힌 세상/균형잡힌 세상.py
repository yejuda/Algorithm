# 스택을 활용
# 온점이 들어오면 종료
# 스택에 '('또는 '['을 넣는다.
# 만약, ')' 또는 ']'가 들어오면, 스택에 있는 것을 뺀다.

while True:   
    st = input()
    if st == '.':
        break

    # 스택 초기화 (다음 테스트를 위해 스택을 비워야 함)
    stack = []

    # 스택 시작
    for i in st:
        if i == '(' or i == '[': 
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':  # 스택이 비어있지 않거나 ')'일 때는 pop()
                stack.pop()
            else:                 # 스택이 비어있거나 짝이 맞지 않으면
                stack.append(i)   # 스택에 append해서 불균형 상태를 명확히 하기(스택이 비어있지 않음으로써 "no"가 출력될 수 있게끔)
                break

        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break


    # 스택이 비어있는지 확인
    if not stack:
        print("yes")
    else:
        print("no")