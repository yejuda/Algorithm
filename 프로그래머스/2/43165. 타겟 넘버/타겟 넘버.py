cnt = 0

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt


def dfs(numbers, target, curr, idx):
    global cnt
    
    # idx의 역할 : 우리는 numbers의 크기만큼 반복을 해야하기 때문에 그것을 count해주기 위한 역할이다.
    if idx == len(numbers):  # 인덱스를 하나씩 증가시킬 것. 그리고 이 인덱스가 numner의 크기와 같다면
        if curr == target:  # 그리고 현재 값이랑 target이 같다면
            cnt += 1        # cnt(target값 나온 경우의 수) 증가
        return
            
    # 재귀함수
    dfs(numbers, target, curr + numbers[idx], idx+1)
    dfs(numbers, target, curr - numbers[idx], idx+1)
    
