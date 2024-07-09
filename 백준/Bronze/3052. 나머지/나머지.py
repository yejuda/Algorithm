a_list = []

for i in range(10):
    n = int(input())
    a_list.append(n % 42)

print(len(set(a_list)))