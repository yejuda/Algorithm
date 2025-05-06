n = int(input())

stack = []
result = []
cnt = 1

for _ in range(n):
    m = int(input())

    while cnt <= m:
        stack.append(cnt)
        result.append("+")
        cnt += 1

    # 스택의 탑이랑 입력 수가 같으면 계속 pop해야 하기 때문에 break를 하면 X
    if stack[-1] == m:
        stack.pop()
        result.append('-')
    
    else:
        print("NO")
        break

# break문으로 for문을 빠져나오더라도 실행되는 것을 막기 위해 
else:
    for k in result:
        print(k)