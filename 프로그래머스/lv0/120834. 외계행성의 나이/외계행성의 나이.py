from string import ascii_lowercase

def solution(age):
    answer = ''
    alph_list = list(ascii_lowercase)
    for i in str(age):
        answer += alph_list[int(i)]
    return answer