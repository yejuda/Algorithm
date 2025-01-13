import sys
input = sys.stdin.readline

def zero(k):
    arr = []
    
    for _ in range(k):
        n = int(input())
        
        if n == 0:
            arr.pop()
        else:
            arr.append(n)
        
    return print(sum(arr))

if __name__ == '__main__':
    k = int(input())
    zero(k)