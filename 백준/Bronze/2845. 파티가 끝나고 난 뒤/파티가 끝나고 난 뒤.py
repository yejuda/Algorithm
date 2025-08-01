n, m = map(int, input().split())
s = map(int, input().split())
u = []

for i in s:
    u.append(i - (n*m))

print(*u)