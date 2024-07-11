def selection_sort_kth_swap(n, k, arr):
    swap_count = 0
    for last in range(n - 1, 0, -1):
        max_idx = 0
        for i in range(1, last + 1):
            if arr[i] > arr[max_idx]:
                max_idx = i
        
        if max_idx != last:
            arr[max_idx], arr[last] = arr[last], arr[max_idx]
            swap_count += 1
            if swap_count == k:
                return sorted([arr[max_idx], arr[last]])
    
    return -1

# 입력 받기
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 결과 출력
result = selection_sort_kth_swap(n, k, arr)
if result == -1:
    print(result)
else:
    print(result[0], result[1])
