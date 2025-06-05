n = int(input())                   # 정수 개수
numbers = list(map(int, input().split()))  # 정수 리스트
v = int(input())                   # 찾을 정수

print(numbers.count(v))           # v의 개수 출력
