import sys

n = int(input())  # 명령의 수
stack = []

# push
def push(a):
    stack.append(a)
# pop
def pop():
    if stack:
        return stack.pop()
    else:
        return -1
# size
def size():
    return len(stack)
# empty
def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0
# top
def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]


for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "top":
        print(top())