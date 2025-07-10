import sys

input = sys.stdin.readline

total_score = 0 # 총 점수를 저장할 변수 초기화

# 5명의 학생 점수를 입력받아 처리
for _ in range(5):
    score = int(input()) # 점수 입력 받기

    # 점수가 40점 미만이면 40점으로 보정
    if score < 40:
        score = 40
    
    total_score += score # 보정된 점수를 총 점수에 더하기

# 5명의 평균을 계산하여 출력
average_score = total_score // 5 # 정수 나눗셈 (몫만 취함)
print(average_score)