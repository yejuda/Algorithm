a = list(map(int, input().split()))
sort_a = sorted(a)

if a == sort_a:
    print("Good")
else:
    print("Bad")