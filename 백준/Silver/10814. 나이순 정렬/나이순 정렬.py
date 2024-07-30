n = int(input())
x = []

for _ in range(n):
    a = list(map(str, input().split()))
    a[0] = int(a[0])
    x.append(a)

x.sort(key=lambda x:x[0])

for i in x:
    print(f"{i[0]} {' '.join(i[1:])}")