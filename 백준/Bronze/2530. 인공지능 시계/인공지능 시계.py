
a,b,c = map(int, input().split())
end = int(input())

# 현재 시간을 모두 초로 변환
current_total_seconds = a * 3600 + b * 60 + c

# 요리 시간을 더한 최종 시간 (초)
final_total_seconds = current_total_seconds + end

# 시 계산: 총 초를 3600으로 나눈 몫을 24로 나눈 나머지
final_hour = (final_total_seconds // 3600) % 24
# 분 계산: 총 초를 60으로 나눈 몫에서 시간으로 사용된 부분을 제외하고 60으로 나눈 나머지
final_minute = (final_total_seconds % 3600) // 60
# 초 계산: 총 초를 60으로 나눈 나머지
final_second = final_total_seconds % 60

print(final_hour, final_minute, final_second)