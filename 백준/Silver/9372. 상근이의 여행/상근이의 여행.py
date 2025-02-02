import sys
input = sys.stdin.readline

def main(t):
    for _ in range(t):
        n, m = map(int, input().split())
        for _ in range(m):
            a, b = map(int, input().split())
                   
        print(n-1)


if __name__ == '__main__':
    t = int(input())
    main(t)