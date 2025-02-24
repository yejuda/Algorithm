# 5번 반복
# 입력 받은 값 모두 리스트에 넣기
# 이중 for 문으로 탐색

people = []

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))
    
# 모든 사람의 등수를 1로 설정
rank = [1] * n
    
for i in range(n):
    for j in range(i+1, n):
        # 피플의 x 비교, y도 비교
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            rank[j] += 1   # 더 덩치가 작은 사람이 등수가 늘어나야 함(등수는 오름차순이니까)
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
            
print(*rank)