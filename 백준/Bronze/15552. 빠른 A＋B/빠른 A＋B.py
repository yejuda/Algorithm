import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    sys.stdout.write(str(a + b) + '\n')
