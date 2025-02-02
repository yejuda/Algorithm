a = list(map(int, input().split()))
k = [1,1,2,2,2,8]

for i in range(len(a)):
    print(k[i]-a[i], end=" ")