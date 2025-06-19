n, m = map(int, input().split())
cnt = 0

for _ in range(n):
    opinion = input()
    # 문자열의 길이와 비교했을 때 'O'가 많으면 찬성 -> 문제 출제
    if len(opinion)//2 < opinion.count('O'):
        cnt += 1
print(cnt)