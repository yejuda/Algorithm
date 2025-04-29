
def prime(n, m):

    # 0과 1은 소수가 아니므로 False 나머지는 True로 초기화
    pr = [False, False] + [True] * (m-1)
    for i in range(2, int(m**0.5)+1):
        if pr[i]:  # 소수면
            # 소수의 배수들을 모두 False로 만들기 (# i의 배수들은 모두 False로)
            for j in range(i*2, m+1, i): 
                pr[j] = False

    # 소수만 리스트로 반환
    return [i for i in range(n, m+1) if pr[i]]

if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in prime(n, m):
        print(i)
