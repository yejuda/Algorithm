### 인덱스로만 비교!!! ###

# 배열의 크기 입력
n = int(input())
# 배열 a입력
a = list(map(int, input().split()))
# 배열 b입력
b = list(map(int, input().split()))

# 배열a와 배열b가 처음부터 같은 경우
if a == b:
    print(1)
    exit()

# a 배열의 마지막 원소부터 두번째 원소까지 반복문 -> 끝에서부터 정렬을 해나가기 위함
for i in range(n-1, 0, -1):  # 참고) 인덱스는 4까지 존재
    # 배열 첫번째부터 현재 원소까지의 최댓값 인덱스 구하기
    max_idx = a.index(max(a[:i+1]))
    # 만약, 최댓값 인덱스가 현재 인덱스와 다르다면
    if max_idx != i:
        # swapping
        a[max_idx], a[i] = a[i], a[max_idx]
    # swapping한 배열 a가 배열 b와 같은지 확인 / 같으면 1을 출력하고
    if a == b:
        print(1)
        # 코드 종료
        exit()
        # (다르다면 계속 진행)

# 코드가 종료 안 되었으면, 배열 a와 배열 b가 다르다는 것이므로 0을 출력
print(0)
