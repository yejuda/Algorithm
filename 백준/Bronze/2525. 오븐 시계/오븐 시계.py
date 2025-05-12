h, m = map(int, input().split())
add = int(input())

minute = h * 60
sum_minute = minute + m + add

hour = (sum_minute // 60) % 24  # 24시일 경우 0이 출력될 수 있도록! 나머지 연산
minute_a = sum_minute % 60

print(hour, minute_a)