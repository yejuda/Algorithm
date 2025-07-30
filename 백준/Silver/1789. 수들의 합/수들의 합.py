s = int(input())
total = 0
num = 1

# 더한게 s보다 작거나 같을 때까지
while total <= s:
    total += num
    num += 1

if total > s:
    print(num - 2)
else:
    print(num - 1)