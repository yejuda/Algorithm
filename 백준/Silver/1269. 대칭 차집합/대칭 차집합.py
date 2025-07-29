import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_n = set(map(int, input().split()))
b_n = set(map(int, input().split()))

print((len(a_n - b_n)) + len(b_n - a_n))