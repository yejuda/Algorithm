import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = {}

for _ in range(n):
    address, password = input().split()
    data[address] = password

for _ in range(m):
    search = input().strip()
    print(data[search])