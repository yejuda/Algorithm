# 종류별로 선택 가능한 경우의 수 = (해당 종류 개수 + 1)
    # +1은 해당 종류에서 안 입는 경우도 포함한 것이다.
# 전체 조합은 모든 종류에 대해 곱을 취하면 된다.
    # (종류1 개수 + 1) * (종류2 개수 + 1)
# 단, 아무것도 안 입는 경우 1가지는 빼주기

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    info = [input().split() for _ in range(n)]

    # 종류만 뽑아오기
    categories = [category for _, category in info]
    # 종류와 종류의 개수 구하기 (ex. Counter({'headgear': 2, 'eyewear': 1}))
    cloth_cnt = Counter(categories)  

    answer = 1
    for count in cloth_cnt.values():
        answer *= (count + 1)
    # 아무것도 입지 않았을 경우 빼기
    answer -= 1

    print(answer)