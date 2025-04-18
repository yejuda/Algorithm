def solution(participant, completion):
    # participant에서 completion를 빼면 남는거 출력
    
    # participant를 hash로 변환해서 참가자 count 세기
    hash_p = {}
    for part in participant:
        if part in hash_p:
            hash_p[part] += 1
        else:
            hash_p[part] = 1
            
    # hash_p에 completion 참가자가 있으면 빼주기
    # 동명이인이 있는 경우, 1씩 빼주기
    for comp in completion:
        if hash_p[comp] == 1:
            del hash_p[comp]
        else:
            hash_p[comp] -= 1
            
    return list(hash_p.keys())[0]
    
        