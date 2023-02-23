# from string import ascii_lowercase

# def solution(age):
#     answer = ''
#     alph_list = list(ascii_lowercase)
#     for i in str(age):
#         answer += alph_list[int(i)]
#     return answer

def solution(age):
    answer = ''
    alph_list = ['a','b','c','d','e','f','g','h','i','j']
    for i in str(age):
        answer += alph_list[int(i)]
    return answer