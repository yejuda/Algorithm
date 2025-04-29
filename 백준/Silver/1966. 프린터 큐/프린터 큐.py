from collections import deque

t = int(input())

for _ in range(t):
    # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문제가 현재 큐에서 몇 번째에 놓여있는지?
    n, m = map(int, input().split())
    important = list(map(int, input().split()))
    cnt = 0  # 몇번째 인쇄인지 count

    # 큐 생성
    queue = deque()

    # 큐에 (중요도, 문서번호(인덱스)) 형태로 저장하기
    for idx, val in enumerate(important):
        queue.append((idx, val))


    # 현재 맨 앞 문서의 중요도가 나머지 문서들 중에서 제일 큰지 확인하기
    while queue:
        i, p = queue.popleft()
        # # any(): 하나라도 True인 값이 있으면 True를 반환(전부 False여야 False를 반환)
        # if any(p < other[1] for other in queue):
        #     # 더 중요한 문서가 뒤에 있으면 다시 넣기
        #     queue.append((i, p))

        for other in queue:
            if p < other[1]:
                queue.append((i, p))
                break

        else:
            # 인쇄 횟수 추가
            cnt += 1
            if i == m:
                print(cnt)
                break