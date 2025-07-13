s = input()

result = []

for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        part1 = s[0:i]
        part2 = s[i:j]
        part3 = s[j:len(s)]

        part1 = part1[::-1]
        part2 = part2[::-1]
        part3 = part3[::-1]

        result.append(part1+part2+part3)

print(sorted(result)[0])