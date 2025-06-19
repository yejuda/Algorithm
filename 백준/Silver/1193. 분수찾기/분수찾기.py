# 1번 라인 : 1/1
# 2번 라인 : 1/2, 2/1
# 3번 라인 : 3/1, 2/2, 1/3
# 4번 라인 : 1/4, 2/3, 3/2, 4/1
# 5번 라인 : 5/1, 4/2, 3/3, 2/4, 1/5

# (인덱스 기준)
# 홀수 라인 -> 분모가 1씩 작아지고, 분자는 1씩 커진다.
# 짝수 라인 -> 분모가 1씩 커지고, 분자는 1씩 작아진다.

x = int(input())

line = 0  # 몇 번째 줄인지
end = 0   # 현재 줄까지의 누적 개수

# 1. 입력 x가 몇 번째 줄에 있는지 찾기
while x > end:
    line += 1
    end += line  # 누적 개수: 1,3,6,10, ...

# 해당 줄에서 몇 번째인지 계산하기
# line번 째 줄의 시작 번호는 end-line+1
    pos_in_line = x - (end - line)

# 분자/분모 계산
if line % 2 == 0:  # 짝수줄이면 ↗
    top = pos_in_line
    bottom = line - pos_in_line + 1
else:              # 홀수줄이면 ↘
    top = line - pos_in_line + 1
    bottom = pos_in_line

print(f"{top}/{bottom}")