def solution(s):
    
    if len(s)%2 == 0:  # 짝수면
        return s[len(s)//2-1:len(s)//2+1]
    
    else:              # 홀수면
        return s[(len(s)//2)] 
