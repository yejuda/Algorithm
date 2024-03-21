def solution(arr):
    answer = []

    answer.append(arr[0])  # 첫번째 요소 바로 추가
    
    for i in range(1, len(arr)):   
        
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    
    return answer