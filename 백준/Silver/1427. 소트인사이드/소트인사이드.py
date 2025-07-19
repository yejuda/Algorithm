n = input()

digit = []
for i in n:
    digit.append(int(i))

digit.sort(reverse=True)

str_digit = [str(d) for d in digit]
print(''.join(str_digit))