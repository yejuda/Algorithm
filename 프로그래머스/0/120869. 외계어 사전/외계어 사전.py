def solution(spell, dic):
    
    for i in dic:
        if sorted(spell) == sorted(i):
            return 1
    return 2   # 모든 루프를 다 돌았는데, 같은 것이 없으면 2


    
    