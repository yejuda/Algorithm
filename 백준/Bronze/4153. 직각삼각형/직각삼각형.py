while True:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    # 세변 중 어느 변이든 빗변이 될 수 있기 때문에 a,b,c 각각이 빗변인 경우 구하기
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("right")
    else:
        print("wrong")