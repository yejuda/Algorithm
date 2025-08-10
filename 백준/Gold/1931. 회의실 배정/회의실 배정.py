n = int(input())

# 값을 모두 받기
value = []
for _ in range(n):
    a, b = map(int, input().split())
    value.append((a, b))

# 모든 회의를 끝나느 시간 기준으로 오름차순 정렬 -> 가장 많은 회의를 진행하려면, 최대한 빨리 끝나는 회의를 먼저 선택해야 하기 떄문
# 끝나는 시간이 같으면 시작 시간을 기준으로 오름차순 정렬
value.sort(key=lambda x : (x[1], x[0]))

# 사용할 수 있는 회의 수
result = 0
# 마지막으로 끝난 회의 시간 저장
last_end_time = 0

for start, end in value:
    # 마지막 회의 끝나는 시간보다 크거나 같으면
    if start >= last_end_time:
        result += 1
        last_end_time = end  # 마지막 끝나는 회의 시간 갱신

print(result)