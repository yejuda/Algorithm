n = int(input())
cnt = 99

if n <= 99:
    print(n)  # 1부터 99까지의 모든 수는 한수이다.
else:
    for i in range(100, n+1):
        # 숫자를 문자열로 바꾼 후, 각 문자를 다시 정수로 변환
        num_list = [int(digit) for digit in str(i)]
        # 첫-두, 두-셋의 차이를 구해서 차이가 같은지 확인
        if num_list[1]-num_list[0]  == num_list[2]-num_list[1]:
            cnt += 1
        
    print(cnt)