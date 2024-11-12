n, m = map(int, input().split())
string = input()
chatering = ''

for st in string:
  for j in range(m):
    chatering += st

print(chatering)
