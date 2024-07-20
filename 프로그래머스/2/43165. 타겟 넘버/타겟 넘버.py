# dfs

cnt = 0

def solution(numbers, target):
    
    dfs(numbers, target, 0, 0)
    
    return cnt

def dfs(numbers, target, curr, idx):  # curr: 현재까지 연산한 값
    global cnt
    
    if len(numbers) == idx:
        if target == curr:
            cnt += 1 
        return
            
    dfs(numbers, target, curr+numbers[idx], idx+1)  # curr(현재값)과 idx를 업데이트 -> 재귀를 통해 반복
    dfs(numbers, target, curr-numbers[idx], idx+1)  # 이건 뺏을 경우
            
    

    