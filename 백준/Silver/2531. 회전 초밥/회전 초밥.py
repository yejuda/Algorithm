# 놓인 접시 수 n, 초밥 가짓수 d, 연속해서 먹는 접시 수 k, 쿠폰 번호 c
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
cnt = 0  # 종류 수 저장 변수

# 리스트를 만들어서 스시를 연장해
add_sushi = sushi * 2

# 한칸씩 이동하면서 4개씩 나눠서(여기에서 set을 사용해서 중복 피하기 -> 종류 수를 구해야하기 때문에) 쿠폰이 있는지 확인해
for i in range(0, n): 
    unique = set(add_sushi[i:i+k])

    if c in unique:
        cnt = max(cnt, len(unique))
    else:
        cnt = max(cnt, len(unique)+1)

print(cnt)