n = int(input())

for j in range(1, n+1):
    result = []
    
    string = input().split(' ')
    for i, s in enumerate(string[::-1]):
        result.append(s)
    print(f"Case #{j}: {' '.join(result)}")
    