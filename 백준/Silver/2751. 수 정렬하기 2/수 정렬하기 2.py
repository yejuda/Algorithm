import sys

n = int(input())
x = []

for i in range(n):
    a = int(sys.stdin.readline())
    x.append(a)

x.sort()

for j in x:
    print(j)