# 카드가 한 장 남을 때까지 반복.  -> 마지막 남게 되는 카드 출력
# 한번은 버리고
# 그 다음번은 아래로 옮기기

from collections import deque

n = int(input())  
result = deque([i for i in range(1, n+1)])
cnt = 1

# result가 길이가 1이 보다 클때까지
    # 만약 cnt가 홀수이면
        # 왼쪽 카드 버리기
        # cnt += 1
    # 홀수가 아니면(짝수이면) 
        # 카드 popleft해서 다시 result에 append
        # cnt += 1

while len(result) > 1:

    if cnt % 2 != 0:  # 홀수이면
        result.popleft()
        cnt += 1
    else:
        result.append(result.popleft())
        cnt += 1

print(result[0])  