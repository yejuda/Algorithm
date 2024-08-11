# 시간 초과 문제를 해결하기 위해서 set을 사용. 
# 집합은 평균적으로 O(1) 시간 복잡도로 요소의 존재 여부를 검사할 수 있다.

n = int(input())
n_num = set(map(int, input().split()))

m = int(input())
m_num = list(map(int, input().split()))

for i in m_num:
    if i in n_num:
        print(1)
    else:
        print(0)