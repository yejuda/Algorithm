import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 포켓몬 개수, 내가 맞춰야 하는 문제의 개수
pocket = {}

# 포켓몬 도감에 번호별로 넣어주기
for i in range(1, n+1):
    name = input().strip()
    pocket[name] = i

# 번호 -> 포켓몬 이름 (반전 딕셔너리)
pocket_reverse = {v: k for k, v in pocket.items()}

for _ in range(m):
    problem = input().strip()  # 숫자 또는 문자가 들어옴
    # 숫자인 경우
    if problem.isdigit():
        problem = int(problem)
        print(pocket_reverse[problem])

    # 문자인 경우
    else:
        print(pocket[problem])