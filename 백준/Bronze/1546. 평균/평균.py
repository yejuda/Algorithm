

n = int(input())  # 시험 본 과목의 개수
score_lis = list(map(int, input().split()))  # 세준이의 현재 성적
emp = []  # 새로운 성적을 담을 리스트

max_score = max(score_lis)

for i in score_lis:
    i = i/max_score*100
    emp.append(i)

a_b_c_sum = sum(emp)

# print(a_b_c_sum/n)
average = a_b_c_sum / n

# 소수점 이하 두 자리까지 출력
print(f"{average:.2f}")