n = int(input())

for _ in range(n):
    # 각 테스트 케이스 입력 받기
    a, b = input().split()
    # 정수로 변환
    a = int(a)

    print(''.join([s*a for s in b]))