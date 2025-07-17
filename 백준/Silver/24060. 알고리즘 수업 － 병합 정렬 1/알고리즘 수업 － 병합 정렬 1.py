import sys
input = sys.stdin.readline

# 전역 변수 설정
N, K = map(int, input().split())
A = list(map(int, input().split())) 
cnt = 0 # 배열에 저장되는 횟수 카운트
result = -1 # K번째 저장되는 수를 저장할 변수, 기본값은 -1 (K번째 저장이 없을 경우)

# 두 정렬된 부분 배열을 병합하고, K번째 저장을 확인
# p (시작 인덱스)
# q (중간 인덱스)
# r (끝 인덱스)
def merge(arr, p, q, r):
    global cnt, result
    
    i = p     # 왼쪽 부분 배열의 시작 인덱스
    j = q + 1 # 오른쪽 부분 배열의 시작 인덱스
    t = 0     # 임시 배열 tmp의 인덱스
    
    tmp = [0] * (r - p + 1) # 병합 결과를 담을 임시 배열

    # 두 부분 배열을 비교하여 tmp에 정렬된 순서로 저장
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1

    # 왼쪽 부분 배열에 남은 원소들을 tmp에 저장
    while i <= q:
        tmp[t] = arr[i]
        i += 1
        t += 1

    # 오른쪽 부분 배열에 남은 원소들을 tmp에 저장
    while j <= r:
        tmp[t] = arr[j]
        j += 1
        t += 1

    # tmp에 저장된 내용들을 다시 원본 배열 arr로 복사
    i = p
    t = 0
    while i <= r:
        arr[i] = tmp[t] # K번째 저장을 확인하는 핵심 부분
        cnt += 1
        if cnt == K:
            result = arr[i] # K번째로 저장된 값을 result에 저장
            break # K번째 값을 찾았으니 더 이상 진행할 필요 없음
        i += 1
        t += 1

# 재귀적으로 배열을 분할하고 병합
def merge_sort(arr, p, r):
    if p < r and result == -1: # K번째 값을 아직 찾지 못했을 경우에만 계속 진행
        q = (p + r) // 2 # 중간 지점
        merge_sort(arr, p, q)      # 왼쪽 부분 배열 정렬
        merge_sort(arr, q + 1, r)  # 오른쪽 부분 배열 정렬
        merge(arr, p, q, r)        # 정렬된 두 부분 배열 병합

# 병합 정렬 실행
merge_sort(A, 0, N - 1)

print(result)