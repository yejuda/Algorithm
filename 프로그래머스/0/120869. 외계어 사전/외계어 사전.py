def solution(spell, dic):
    # for i in dic:
    #     for j in spell: 
    #         if i in j:   # dic의 단어들 안에 spell이 있다면 
    #             return 1
    #         else:
    #             return 2
    spell_x = ''.join(sorted(spell))
    
    for i in dic:
        if spell_x == ''.join(sorted(i)):
            return 1
    return 2   # 모든 루프를 다 돌았는데, 같은 것이 없으면 2
    