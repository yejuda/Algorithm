# def solution(cipher, code):
#     answer = ''
    
#     for i in range(code-1, len(cipher), code):
#         answer += cipher[i]

#     return answer

def solution(cipher, code):

    return cipher[code-1::code]