n = int(input())                    # 참가자의 수
a = list(map(int, input().split())) # 티셔츠 사이즈별 신청자의 수
t, p = map(int, input().split())    # 티셔츠와 펜의 묶음 수

result = 0

for i in a:
    result += (i + t - 1) // t

print(result)
print(n//p, n%p)  # 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지