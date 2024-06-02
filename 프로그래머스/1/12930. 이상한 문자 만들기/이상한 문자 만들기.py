

def solution(s):
    answer = []
    for word in s.split(' '):  # 단어 단위로 분리
        transformed_word = []
        for idx, char in enumerate(word):
            if idx % 2 == 0:  # 홀수 인덱스
                transformed_word.append(char.upper())
            else:  # 짝수 인덱스
                transformed_word.append(char.lower())
        answer.append(''.join(transformed_word))  # 변환된 단어를 리스트에 추가
    
    return ' '.join(answer)  # 단어를 공백으로 연결하여 문자열 반환