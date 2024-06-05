# nums의 개수 1/2

def solution(nums):
    
    get_p = len(nums) // 2  # 가져갈 수 있는 폰켓몬 개수
    unique = list(set(nums))  # nums의 고유값을 저장    # 참고) set은 리스트의 고유값을 집합으로 반환한다. 

    # 가져갈 수 있는 폰켓몬 개수(get_p)와 nums의 고유값 개수(unique) 둘 중에 작은 값이 정답이다.
    return min(get_p, len(unique))