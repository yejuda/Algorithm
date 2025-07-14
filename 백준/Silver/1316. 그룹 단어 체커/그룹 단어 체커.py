# 그룹단어 특징: 떨어져서 나오지 않는다.
n = int(input())

word_list = [input() for _ in range(n)]

# 그룹단어 카운트
total_group_words = 0

for word in word_list:
    seen_latters = set()
    is_group_word = True  # 이 단어가 그룹단어인지 판별할 플래그

    prev_char = ''  # 이전 글자를 저장할 변수

    for char in word:
        # 이전 글자와 같으면 연속된 글자이므로 넘어가기
        if prev_char == char:
            pass
        # 이전 글자와 다르면, 새로운 글자 등장
        else:
            # 이미 나왔던 글자가 다시 나왔으므로 그룹단어 아님
            if char in seen_latters:
                is_group_word = False
                break  # 해당 단어 검사 중단
            # 이전글자와 다른데 나왔던 글자 아님
            else:
                seen_latters.add(char)  # 처음 나오는 글자이므로 seen_latters에 추가
        prev_char = char  # 현재 글자를 이전 글자로 업데이트

    if is_group_word:
        total_group_words +=1 

print(total_group_words)