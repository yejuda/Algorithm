# 이항계수 : n개의 원소 중에서 k개를 순서에 상관없이 뽑았을 때 조합의 가짓수

import math

def bino_coef_factorial(n, k):
    return math.factorial(n) // (math.factorial(k)*math.factorial(n-k))

n, k = map(int, input().split())

print(bino_coef_factorial(n, k))