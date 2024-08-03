n = int(input())   # 점의 개수
xy = []  # 값 정보를 담을 빈 리스트

for _ in range(n):
    a = list(map(int, input().split()))
    xy.append(a)

xy.sort(key = lambda x : (x[0], x[1]))  # x[0]을 기준으로 정렬하고, 같을 경우 x[1]을 기준으로 정렬하기

for i in xy:
    print(' '.join(map(str, i)))