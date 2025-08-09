n = int(input())
m = list(map(int, input().split()))

# 중복 제거 후 오름차순 정렬
set_m = sorted(set(m))

result = {}
for idx, val in enumerate(set_m):
    result[val] = idx

for rank in m:
    print(result[rank], end= ' ')