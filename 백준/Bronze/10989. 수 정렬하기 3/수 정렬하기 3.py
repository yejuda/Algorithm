# 계수 정렬 활용

import sys
# input = sys.stdin.read

n = int(input())   # 값의 개수 

# 메모리 사용을 최소화하기 위해 10000개의 0으로 이루어진 리스트 초기화
cnt = [0] * (10000 + 1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언

for _ in range(n):
    a = int(sys.stdin.readline())
    cnt[a] += 1  # for문을 돌며 각 데이터에 해당하는 인덱스 값을 +1 한다. 

for i in range(len(cnt)):
    for _ in range(cnt[i]):  # cnt의 인덱스 하나를 돈다.
        print(i)   # i를 cnt의 값만큼 출력하고 빠져나와 그 다음 i+1번째 인덱스로 이동한다.