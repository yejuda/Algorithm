def solution(arr, n):
    # answer = 
    
    if len(arr)%2 != 0:    # arr의 길이가 홀수이면
        for i in range(len(arr)):
            if i%2 == 0:  # 짝수 인덱스에 n을 더해라
                arr[i] += n  # arr[i] = arr[i] + n
        return arr
            
    else:        # arr의 길이가 짝수이면
        for i in range(len(arr)):
            if i%2 != 0:   # 홀수 인덱스에 n을 더해라
                arr[i] += n
        return arr
            
    
    return answer