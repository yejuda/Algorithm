n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

# 종이를 1/2로 자르기
def div(start_row, start_col, size):
    global paper, white, blue

    # 같은지 아닌지(white or blue) 확인 변수
    flag = True
    standard = paper[start_row][start_col]

    for i in range(start_row, start_row+size):
        for j in range(start_col, start_col+size):
            if paper[i][j] != standard:
                flag = False
                break
        if not flag:
            break
    
    # 같은 색깔인 경우
    if flag:
        if standard == 0:
            white += 1
        else:
            blue += 1
        return  # 함수 종료
    
    # 다른 숫자가 있을 경우
    new_size = size // 2

    for r in range(2):
        for c in range(2):
            div(start_row + r * new_size,
                start_col + c * new_size,
                new_size)
            
div(0, 0, n)
print(white)
print(blue)