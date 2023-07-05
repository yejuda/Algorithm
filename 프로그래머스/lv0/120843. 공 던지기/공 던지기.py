def solution(numbers, k):
    
    # 2칸씩 이동하므로 2를 곱해주고
    # 0번 인덱스부터 '공을 던지는 사람'을 찾아야 하므로 k-1
    # numbers 길이를 넘어갈 수 없으므로 % 사용
    
    answer = numbers[2*(k-1) % len(numbers)]
    
    return answer