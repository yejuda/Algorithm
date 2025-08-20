n = int(input())

# 100x100 크기의 2차원 배열 생성
# 색종이가 덮는 모든 칸을 1로 표시
# 마지막으로 배열에서 1의 개수를 세기

arr = [[0] * 101 for _ in range(101)]

for _ in range(n):

    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

result = 0
for a in range(100):
    for b in range(100):
        if arr[a][b] == 1:
            result += 1
            
print(result)