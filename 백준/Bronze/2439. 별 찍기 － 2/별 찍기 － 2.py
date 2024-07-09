# 공백: 4개, 3개, 2개, 1개, 0개
# 별: 1개, 2개, 3개, 4개, 5개

n = int(input())

for i in range(n): 
    space = ' ' * (n-i-1)
    stars = '*'*(i+1)
    print(space+stars) 