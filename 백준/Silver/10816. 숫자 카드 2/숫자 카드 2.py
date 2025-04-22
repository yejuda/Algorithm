# 해시로 풀어볼까

from collections import Counter

def number_card():
    n = int(input())
    c1 = list(map(int, input().split()))
    m = int(input())
    c2 = list(map(int, input().split()))

    result = []

    # c1에 있는 숫자 개수 카운트
    c1_cnt = Counter(c1)

    # c2의 숫자와 비교
    for i in c2:
        # c2에 있는 숫자가 c1에 있으면 개수 출력
        if i in c1_cnt:
            result.append(c1_cnt[i])
        # 아니면 0 출력
        else:
            result.append(0)
        
        # 아래 처럼 코드를 줄일 수 있음
        # result.append(c1_cnt[i] if i in c1_cnt else 0)

    return result

if __name__ == '__main__':
    print(' '.join(map(str, number_card())))
