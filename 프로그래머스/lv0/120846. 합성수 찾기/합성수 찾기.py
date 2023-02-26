def solution(n):
    answer = []
    cnt = 0
    # 약수를 판별해보자
    for i in range(2, n+1):
        for j in range(1, n+1):
            if i % j == 0:
                answer.append(i)  # 4일때 answer = [4,4,4]
        if answer.count(i) >= 3:  # answer.count(4) 이면 answer에서 4인값의 개수를 찾아줘. 
            cnt += 1              # 그 개수가 3개 이상인 경우 cnt의 개수를 1씩 늘려줘.
            
    return cnt