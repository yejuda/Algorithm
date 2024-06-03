# 최대한 많은 부서에 예산을 지원해준다는 뜻은, 예산이 적은 수의 부서부터 지원해주면 된다.

def solution(d, budget):
    cnt = 0  # 지원한 부서 개수
    budget_sum = 0  # 지원해줄 부서를 더해가는 변수
    
    # 예산이 적은 순으로 정렬
    d.sort()
    
    for i in d:
        budget_sum += i
        
        if budget_sum > budget:  # 예산보다 크면 종료
            break
            
        cnt += 1
        
    return cnt