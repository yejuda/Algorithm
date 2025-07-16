# 빼기 기호 뒤에 나오는 모든 숫자들을 모두 더해서 가장 크게 빼기!

import re

n = input()

parts = re.findall(r'\d+|[+-]', n)
flag = False  # '-'를 만났는지 확인 플래그 변수
prev = 0  # - 만나기 전 변수
former = 0    # - 만난 후 변수

for i in parts:
    if i == '-':
        flag = True  # - 변수를 만났다

    if not flag and i.isdigit(): # -를 만나기 전이라면 숫자들만 다 더해. 어차피 다 덧셈일 것
        prev += int(i)

    if i.isdigit() and flag:  # 만난 이후 숫자들은 다 더해  # 숫자이고 flag가 true(-변수 만난 이후)이라면,
        former += int(i)

print(prev-former)