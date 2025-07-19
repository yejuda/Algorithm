alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()


# 크로아티아 알파벳은 2~3개, 따라서 해당 크로아티아를 '*'인 한글자로 수정
for i in alpha :
    n = n.replace(i, '*')  
print(len(n))
