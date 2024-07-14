def selection_sort(arr, n, k):
    cnt = 0  # 교환 횟수
    for i in range(n-1, 0, -1): 
      max_idx = 0 # 최대값 인덱스

      # 최대값 인덱스 업데이트
      for j in range(1, i+1):
        if arr[max_idx] < arr[j]:   # 현재 범위의 제일 끝쪽(오른쪽)에 있는 값이 현재 최대값보다 작을 경우
          max_idx = j  # 최대값 인덱스 업데이트

      if max_idx != i:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]  # swap
        cnt += 1  # 교환 횟수 증가 

        if cnt == k:
          print(' '.join(map(str,arr)))
          return        

    # K번째 스왑이 일어나지 않았다면 -1 출력
    print(-1)

# 입력 받기
n, k = map(int, input().split())  # n = 배열 a의 크기, k= 교환 횟수
arr = list(map(int,input().split()))

selection_sort(arr, n, k)