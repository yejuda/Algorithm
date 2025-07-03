isbn = input()
idx = isbn.index('*')

# 0부터 9까지 가능한 숫자를 '*'자리에 넣어보기
for i in range(10):
    tmp = list(isbn)
    tmp[idx] = str(i)  # '*'이 있던 자리에 숫자 'i'를 문자열로 넣기
    nums = list(map(int, tmp))  # 문자 리스트를 정수 리스트로 변경

    s = 0 # 검증을 위한 합계 초기화

    for j in range(12):
        # 홀수는 그냥 더하기(가중치 1) -> 인덱스 기준 짝수임
        if j % 2 == 0:
            s += nums[j]
        else:
            s += nums[j] * 3
        
    check = (10 - (s % 10)) % 10

    if check == nums[12]:
        print(i)
        break