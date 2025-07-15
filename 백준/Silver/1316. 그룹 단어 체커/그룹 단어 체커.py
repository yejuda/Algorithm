# 같은 문자가 나온다면 그것은 하나로 취급
# 이전 문자가 다르고 set에 들어가있지 않으면 새로운 문자 ->set에 추가

n = int(input())
cnt = 0    # 그룹단어 카운트

for _ in range(n):
    stored = set()  # 나온 단어 저장 변수
    is_grouped = True  # 그룹단어 확인변수
    prev = ''  # 이전 단어 확인 변수

    word = input()

    for w in word:
        # 그룹단어가 아닌 조건
        if w != prev and w in stored:
            is_grouped = False
            break
        # 이전 문자와 현재 문자가 같으면 pass
        if w == prev:
            pass
        # 각 문자를 stored에 추가하고 prev를 업데이트
        stored.add(w)
        prev = w

    if is_grouped == True:
        cnt += 1
print(cnt)
