n = int(input())
cnt = 0

for _ in range(n):
    s = input() # 문자 입력 받기
    stack = []  # 매 줄마다 스택이 초기화
    
    for i in s:
        if not stack:  # 스택이 비어있다면 append
            stack.append(i)
        
        # 그게 아니라, 스택의 최상단 문자와 현재 읽고 있는 문자가 같다면
        elif stack[-1] == i:  
            stack.pop()
        
        else:
            stack.append(i)
        
    if not stack:
        cnt += 1
        
print(cnt)
