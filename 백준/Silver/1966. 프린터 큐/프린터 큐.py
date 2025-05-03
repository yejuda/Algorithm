from collections import deque

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    important = list(map(int, input().split()))

    cnt = 0

    queue = deque()

    for idx, val in enumerate(important):
        queue.append((idx, val))

    # 뽑은 큐가 우선순위가 가장 높은지 확인
    # 큐를 돌면서 pop한 큐보다 작으면 다시 큐에 append
    while queue:  # 큐가 존재할 때까지
        # 큐를 뽑아.
        i, v = queue.popleft()

        for other in queue:
            if v < other[1]:
                queue.append((i, v))
                break  # 종료하고 다시 새로운 큐를 pop 해야함
                
        # for문을 다 돌았는데도 뽑은 큐가 제일 작은게 아니면(제일 큰거라면)
        else:
            cnt += 1
            if i == m:
                print(cnt)
                break