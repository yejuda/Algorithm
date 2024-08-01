# 투포인터 사용하면서 합을 계산하기
# : 시작과 끝 포인터를 설정한 후, 합이 타겟값보다 작다면 시작 포인터 증가(더 큰값을 만들기 위함)
#   합이 타겟값보다 크다면 끝 포인터 감소(더 작은 값을 만들기 위함)

n, m = map(int,input().split())  # n: 카드의 개수 / m: 딜러가 외치는 숫자
nums = list(map(int, input().split()))
nums.sort()     # 오름차순 정렬
closest_sum  = 0  # 현재까지 가장 가까운 합


for i in range(n-2):
    start = i+1
    end = n-1

    while start < end:
        current_sum = nums[i] + nums[start] + nums[end]
        
        # 현재 합이 m을 넘지 않으면서 지금까지 발견된 가장 가까운 합보다 큰지를 확인
        if current_sum <= m and current_sum > closest_sum:
            closest_sum = current_sum

        if current_sum < m:
            start += 1
        elif current_sum > m:
            end -= 1
        else:
            print(current_sum)
            exit()  # 타겟값과 같은 경우 프로그램 종료

print(closest_sum)