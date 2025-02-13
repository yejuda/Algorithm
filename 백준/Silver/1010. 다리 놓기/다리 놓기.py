import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    combs_num = math.comb(m, n)   # combinations는 모든 조합을 생성. math.comb는 바로 조합의 수를 구할 수 있음 
    print(combs_num)