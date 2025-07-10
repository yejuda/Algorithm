import sys

input = sys.stdin.readline

score_min = sum(list(map(int, input().split())))

score_man = sum(list(map(int, input().split())))

print(max(score_min, score_man))