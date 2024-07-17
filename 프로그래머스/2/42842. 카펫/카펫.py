def solution(brown, yellow):
    answer = []
    
    # yellow 크기만큼 반복
    for i in range(1, yellow+1):
        if yellow % i == 0:  # 0으로 나누어 떨어졌을 때 **
            yellow_x = yellow // i # yellow를 i로 나눈 몫이 yellow의 가로 길이
            yellow_y = i           # i가 yellow의 세로 길이가 된다.
            
            # 방정식이 brown의 개수일때
            if (yellow_x*2) + (yellow_y*2) + 4 == brown:
                answer.append(yellow_x+2)  # yellow_x에 2를 더한 것이 가로 길이
                answer.append(yellow_y+2)  # yellow_y에 2를 더한 것이 세로 길이
                break
        
    return answer