import math

def solution(n):
    
    num = int(math.sqrt(n))**2
    
    if num == n:
        return (int(math.sqrt(n)) + 1) ** 2
    else:
        return -1
