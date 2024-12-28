import sys

input = sys.stdin.readline

n = int(input()) 

stack_cnt = 0
stack = []

# 값 입력 받기
stack_num = [int(input()) for _ in range(n)]

for current_h in reversed(stack_num):  #  보는 방향 순(오른쪽부터)으로 진행
    # 스택에 값을 추가해야 하는 경우
    if not stack or current_h > stack[-1]:
        stack_cnt += 1
        stack.append(current_h)

print(stack_cnt)