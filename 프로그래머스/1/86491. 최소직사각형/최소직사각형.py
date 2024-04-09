'''
'가로*세로'로 생각하지 말고, 하나의 모서리라고 생각해보자.
한쪽이 가로가 된다면, 다른 한쪽은 세로가 될 수밖에 없다.
우리는 모든 명함을 수납할 수 있는 최소 직사각형을 만들려고 한다.
sizes 배열을 flatten 후 내림차순으로 sorting 하고, 전체 개수의 1/2씩 2차원 배열로 만들어준다.
2차원 배열마다의 첫번째 수가 큰수 중에 큰수, 작은 수 중에 큰수이기 때문에 최소 직사각형을 만들 수 있다.
'''

def solution(sizes):
    w = []
    h = []
    
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
        
    return max(w) * max(h)


'''
def solution(sizes):
    
    result = []

    # 2차원 배열을 1차원 배열로 flatten
    flatten = [num for onearr in sizes for num in onearr]
    # 내림차순 정렬
    flatten.sort(reverse=True)
    
    # 묶을 숫자 개수(전체의 1/2)
    cnt = len(flatten) // 2
    
    for i in range(0, len(flatten), cnt):  # 0부터 sizes 개수만큼 반복. 전체 개수의 1/2씩
        group = flatten[i:i+cnt]
        result.append(group)
    
    return result[0][0] * result[1][0]
'''