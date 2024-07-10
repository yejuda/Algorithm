a = int(input())
b = int(input())
c = int(input())

# 값 곱하기
mul = a*b*c

# 개수 담을 리스트 초기화
x = [[] for _ in range(10)]

# 숫자에 해당하는 인덱스에 1추가(카운트 위함)
for i in str(mul):
    index = int(i)
    x[index].append(1)

# 1을 추가한 것을 모두 합한 뒤 출력
for j in x:
    s_x = sum(j)
    print(s_x)