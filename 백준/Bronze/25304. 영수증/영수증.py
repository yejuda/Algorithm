x = int(input())
n = int(input())

result = 0
for _ in range(n):
    a, b = map(int, input().split())
    result += a*b

if result == x:
    print('Yes')
else:
    print("No")