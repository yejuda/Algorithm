li = [int(input()) for _ in range(2)]
if li[0] > 0 and li[1] > 0:
    print(1)
elif li[0] < 0 and li[1] > 0:
    print(2)
elif li[0] < 0 and li[1] < 0:
    print(3)
else:
    print(4)