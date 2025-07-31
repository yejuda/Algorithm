n = int(input())
m = int(input())
s = input()

pattern = 'IOI'+ ('OI' * (n-1))

cnt = 0

# 문자열 슬라이싱!!
for i in range(len(s) - len(pattern) + 1):
    if s[i:i+len(pattern)] == pattern:
        cnt += 1

print(cnt)