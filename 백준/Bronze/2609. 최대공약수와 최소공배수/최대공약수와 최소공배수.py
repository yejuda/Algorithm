import math

n, m = map(int, input().split())

def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

def lcm(n, m):
    return abs(n*m) // gcd(n, m)


print(gcd(n, m))
print(lcm(n, m))