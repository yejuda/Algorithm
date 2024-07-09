# 줄을 바꿔가면서 입력 받기
a = [int(input()) for _ in range(9)]


print(max(a))
print(a.index(max(a))+1)