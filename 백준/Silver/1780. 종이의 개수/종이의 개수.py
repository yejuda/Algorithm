n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# -1, 0, 1 종이의 개수를 셀 변수
minus = 0
zero = 0
one = 0 

# 종이를 계속 1/3으로 잘라내는 재귀함수
def divide_paper(start_row, start_col, size):
    global paper, minus, zero, one

    # 같은지 아닌지 flag변수
    flag = True
    # 현재 종이 조각이 모두 같은 숫자로 이루어져있는지 검사
    standard = paper[start_row][start_col]  # 기준값

    for i in range(start_row, start_row+size):
        for j in range(start_col, start_col+size):
            # 동일하지 않다면
            if paper[i][j] != standard:
                flag = False
                break
        # 내부 for문에서 이미 같은 숫자가 아니라고 판정난 경우
        if not flag:
            break
    
    # 모두 같은 숫자로 이루어져 있는 경우
    if flag: 
        if standard == -1:
            minus += 1
        elif standard == 0:
            zero += 1
        else:
            one += 1
        return  # 함수 종료

    # 숫자가 다를 경우 9개의 작은 조각으로 나누기, 재귀호출
    new_size = size // 3

    for r in range(3):
        for c in range(3):
            divide_paper(start_row + r * new_size,
                         start_col + c * new_size,
                         new_size)

divide_paper(0, 0, n)
print(minus)
print(zero)
print(one)