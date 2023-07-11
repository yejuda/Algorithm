def solution(myString, pat):
    
    # 우선, my_String과 pat의 알파벳들을 모두 소문자로 변환
    myString = myString.lower()
    pat = pat.lower()
    
    if pat in myString:   # myString안에 pat이 있으면,
        return 1
    else:
        return 0
    
    
