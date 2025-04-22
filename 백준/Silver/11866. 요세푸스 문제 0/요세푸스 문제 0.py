n, k = map(int, input().split())

array = [i for i in range(1, n+1)]
idx = 0
result = []

while array:
    # 요소를 제거함으로써 이미 한 칸 간 것이므로, k-1만큼 이동
    # 인덱스는 계속 누적
    # # 리스트 크기를 벗어나지 않도록 '%연산자'로 항상 조정
    idx = (idx + k - 1) % len(array) 
    result.append(array.pop(idx))

format = '<' + ', '.join(map(str, result)) + '>'
print(format)