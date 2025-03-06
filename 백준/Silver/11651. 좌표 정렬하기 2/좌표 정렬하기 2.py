# n을 입력 받는다.
# n만큼 for문을 돌려서 좌표를 입력 받는다.
# 입력받은 좌표(튜플)를 리스트에 넣는다.
# y 기준으로 오름차순 정렬, 만약에 y가 같으면 x기준으로 오름차순으로 정렬

import sys


input = sys.stdin.readline

def main(n):
    empt_list = []

    for _ in range(n):
        x, y = map(int, input().split())
        empt_list.append((x, y))  # 튜플 형식으로 리스트에 넣기

    # key는 함수를 입력 받는다. 즉, lambda는 함수
    answer = sorted(empt_list, key = lambda corr: (corr[1], corr[0]))   # 인덱스 1번으로 정렬! -> "1번의 숫자가 같으면" 0번으로 정렬(오름차순)

    return answer


if __name__ == '__main__':
    n = int(input())
    answer = main(n)

    for i in answer:
        print(" ".join(map(str, i)))   # 각 요소를 문자열로 변경한 후, 공백으로 연결한다.
    