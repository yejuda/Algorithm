def solution(arr):
    
    if len(arr) > 1:
        arr.remove(min(arr))
    else:
        arr.remove(arr[0])
        arr.append(-1)
        
    return arr