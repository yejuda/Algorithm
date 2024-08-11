import sys
from collections import deque

n = int(input())  # 명령의 수
que = deque()

# push
def push(a):
    que.append(a)
# pop
def pop():
    if que:
        return que.popleft()
    else:
        return -1
# size
def size():
    return len(que)
# empty
def empty():
    if len(que) == 0:
        return 1
    else:
        return 0
# front
def front():
    if len(que) == 0:
        return -1
    else:
        return que[0]
# back
def back():
    if len(que) == 0:
        return -1
    else:
        return que[-1]


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
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())