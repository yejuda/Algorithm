import sys

input = sys.stdin.readline

K, N, M = map(int, input().split())

total_cost = K * N

money_needed = total_cost - M

print(max(0, money_needed))