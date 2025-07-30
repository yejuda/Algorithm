S = int(input())

current_sum = 0
num = 1

while True:
    if current_sum + num > S:
        break # 현재 합에 다음 숫자를 더했을 때, S를 초과할 경우 루프 종료
    
    current_sum += num
    num += 1

print(num-1)