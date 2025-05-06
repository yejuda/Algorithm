from collections import Counter

n = int(input())  # 홀수
m = [int(input()) for _ in range(n)]

# 산술평균
print(round(sum(m) / n))

# 중앙값
sort_m = sorted(m)
print(sort_m[len(sort_m) // 2])

# 최빈값
# most_common(): (값, 빈도수) 튜플을 많이 등장한 순서로 정렬해 반환한다.
mode = Counter(m)
max_freq = max(mode.values())  # values의 최댓값 구해두기
modes = []  # 최빈값을 저장할 변수

for key, val in mode.items():
    if max_freq == val:
        modes.append(key)

if len(modes) == 1:
    print(modes[0])
else:
    print(sorted(modes)[1])  # 최빈값이 두개면 <정렬 후> 두번째꺼 출력


# 범위
print(max(m) - min(m))

