# i번째부터 j번째까지 자른 후, 정렬하기
# 그리고 k번째의 숫자 출력하기
# 리스트에 담기

def solution(array, commands):
    answer = []
    
    for command in commands:
        # i, j, k 지정해주기
        i,j,k = command
        # i번째부터 j번째까지 자르고 정렬 후 k번째 값 answer 리스트에 담기
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer



'''
def solution(array, commands):
    answer = []
    
    for z in commands:
        # i, j, k 지정해주기
        i = z[0]  #2
        j = z[1]  #5
        k = z[2]  #3
        
        # i번째부터 j번째까지 자르기
        slicing = array[i-1:j]   # [5,2,6,3]
    
        # 정렬
        slicing.sort()
        
        # k번째 숫자 구한 후, 빈리스트에 append
        answer.append(slicing[k-1])
    
    
    return answer
'''


