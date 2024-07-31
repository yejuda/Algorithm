# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
# 245의 분해합은 256(=245+2+4+5)  
# 256 슷자가 주어지고, 이 수를 만드는 분해합(가장 작은 생성자)을 구해야 한다. 

# 분해합 함수
def sum_of_digits(n):  
    return n + sum(map(int, str(n)))

n = int(input())  # M의 분해합(ex.256)
result = 0  # 생성자가 없는 경우 0 출력

for i in range(1, n):
    if sum_of_digits(i) == n:
        result = i
        break

print(result)
