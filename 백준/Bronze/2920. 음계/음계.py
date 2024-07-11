n = list(map(int, input().split()))

if sorted(n) == n:
    print('ascending')
elif sorted(n)[::-1] == n:
    print('descending')
else:
    print('mixed')