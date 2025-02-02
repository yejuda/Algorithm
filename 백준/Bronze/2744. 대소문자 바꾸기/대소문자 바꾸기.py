a = input()

for i in a:
    if i.isupper() == True:
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")