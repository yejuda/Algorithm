# 널빤지 개수 초기화
cover_cnt = 0
# 널빤지 커버 끝 범위 초기화 -> 맨 처음 싱크홀 순회할 때 널빤지 수를 추가하기 위함
cover_end = 0


# 싱크홀 개수, 널빤지 길이
sink_cnt, cover_len = map(int, input().split())
# 싱크홀 위치
sink_location = list(map(int, input().split()))

# 싱크홀 위치 sort -> 널빤지의 최소 개수를 구하기 위함
sort_sink = sorted(sink_location)


for sink in sort_sink:
    
    # 이미 커버된 범위에 있는 싱크홀이면 널빤지를 추가하지 않고 넘어간다.
    if sink <= cover_end:
        continue 
    # 그게 아니면 널빤지 추가, 널빤지 커버 끝 범위 업데이트
    else:
        cover_cnt += 1
        cover_end = sink + cover_len - 1   # 현재 싱크홀 + 널빤지 길이 - 1

# 최종 널빤지 개수 
print(cover_cnt)
