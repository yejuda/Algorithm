import math

# 우선 팩토리얼 계산
def factorial(n):
    return math.factorial(n)
    
# 그 숫자를 왼쪽부터 순회
    # 0 이면 개수 + 1
    # 아니면 break
def rounds(num, cnt):
    num_str = str(num)
    for re in reversed(num_str):
        if re == '0':
            cnt += 1
        else:
            break
    return cnt
    
if __name__ == '__main__':
    n = int(input())
    
    num = factorial(n)
    print(rounds(num, 0))