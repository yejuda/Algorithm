import sys

input = sys.stdin.readline

def result():
    # 난이도 의견 개수
    n = int(input())
    # 난이도 담을 리스트
    level = [int(input()) for _ in range(n)]

    # 난이도 정렬
    level.sort()

    # 제외할 인원 수 (반올림하기)  -> 인덱스로 활용하기
    # round 함수는 오사오입 방식이라 사용X
    pass_h = int((n * 0.15) + 0.5)
    # pass_h 만큼 가장 높은 난이도와 낮은 난이도 제외
    filtered = level[pass_h:n-pass_h] if n > 0 else []

    # 평균 계산 (의견이 없는 경우 예외 처리)
    if filtered:
        avg = int((sum(filtered) / len(filtered)) + 0.5)
    else:
        avg = 0    
    
    return avg

if __name__ == '__main__':
    print(result())