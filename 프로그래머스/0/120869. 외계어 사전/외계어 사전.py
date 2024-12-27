def solution(spell, dic):

    spell_x = ''.join(sorted(spell))
    
    for i in dic:
        if spell_x == ''.join(sorted(i)):
            return 1
    return 2   # 모든 루프를 다 돌았는데, 같은 것이 없으면 2
    