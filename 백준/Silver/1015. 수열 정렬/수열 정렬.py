n = int(input())
a = list(map(int, input().split()))

# (값, 원래 인덱스) 구하기
indexed_a = []
for i in range(n):
    indexed_a.append((a[i], i))

indexed_a.sort()


# 결과 배열
p = [0] * n  

# 정렬된 짝들을 순회하며 순위부여
for rank, (val, original_idx) in enumerate(indexed_a):
    p[original_idx] = rank

print(*p)