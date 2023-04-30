def solution(num_list):
    answer = 0
    for i, num in enumerate(num_list):  # 인덱스와 값을 순서대로 나열
        if num < 0:
            return i
        
    return -1