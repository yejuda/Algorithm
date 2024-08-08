l = int(input())
char = input()

r = 31
m = 1234567891
cnt = 0

for i in range(l):
    n = ord(char[i]) - 96
    cnt += n*(r**i)

print(cnt % m)