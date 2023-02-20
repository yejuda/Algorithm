def solution(dot):
    answer = 0
    # if (int(dot[0]) > 0) and (int(dot[1]) > 0):
    #     answer = 1
    # elif (int(dot[0]) < 0) and (int(dot[1]) > 0):
    #     answer = 2
    # elif (int(dot[0]) < 0) and (int(dot[1]) < 0):
    #     answer = 3
    # else:
    #     answer = 4
    if dot[0] > 0:  # dot의 0번인덱스가 양수인 경우
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    elif dot[0] < 0:  # dot의 0번인덱스가 음수인 경우
        if dot[1] < 0:
            answer = 3
        else:
            answer = 2
    return answer