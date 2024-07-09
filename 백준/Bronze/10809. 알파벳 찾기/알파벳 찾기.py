n = input()
s = 'abcdefghijklmnopqrstuvwxyz'

for i in s:
    if i in n:  # n에 i가 있으면
        print(n.index(i), end= ' ')
    else:
        print(-1, end=' ')
        