from collections import Counter

n, m = map(int, input().split())  
detdobodo = []
result = []

for _ in range(n):
    detdobodo.append(input())

for _ in range(m):
    detdobodo.append(input())

cnt = Counter(detdobodo)

for k, v in cnt.items():
    if v >= 2:
        result.append(k)

print(len(result))
for i in sorted(result):
    print(i)