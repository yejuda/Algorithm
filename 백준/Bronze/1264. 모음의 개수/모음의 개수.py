n = [ 'a', 'e', 'i', 'o', 'u']

while True:
    a = input()

    if a == '#':
        break

    # 문자열을 소문자로 바꾸기
    a = a.lower()
    
    result = 0

    for i in n:
        result += a.count(i)
    print(result)
    