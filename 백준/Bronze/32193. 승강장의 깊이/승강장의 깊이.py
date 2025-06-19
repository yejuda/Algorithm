import sys
input = sys.stdin.readline

n = int(input())
x = 0
k = 0

for _ in range(n):
    
    a, b = map(int, input().split())
    x += a
    k += b
    print(x-k)