import sys
input = sys.stdin.readline

# list에서 시간초과 발생하면 set로
n = int(input())
n_n = set(map(int, input().split()))
m = int(input())
m_n = list(map(int, input().split()))

result = []

for i in m_n:
    if i in n_n:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))