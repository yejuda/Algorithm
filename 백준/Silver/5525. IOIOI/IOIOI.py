n = int(input())
m = int(input())
s = input()

target_n = n

ans = 0
count_o = 0
i = 0

while i < m - 1:
    if s[i] == 'I' and s[i+1] == 'O':
        if i + 2 < m and s[i+2] == 'I':
            count_o += 1
            if count_o == target_n:
                ans += 1
                count_o -= 1
            i += 2
        else:
            count_o = 0
            i += 1
    else:
        count_o = 0
        i += 1

print(ans)