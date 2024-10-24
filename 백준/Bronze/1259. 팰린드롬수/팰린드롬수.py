while True:
    word = input()   # 문자열로 입력받기
    if word == '0':
        break
    reverse_word = "".join(reversed(word))
    
    if word == reverse_word:
        print('yes')
    else:
        print('no')
    