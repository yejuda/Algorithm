n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:  # i에서 k로 가는 길이 있고 동시에 k에서 j로 가는 길이 있다면, i에서 j로 가는 길이 존재한다
                    graph[i][j] = 1
    
for row in graph:
    print(*row)