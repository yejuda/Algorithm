import sys
input = sys.stdin.readline

def add(x):
    if x not in s:
        s.add(x)

def remove(x):
    if x in s:
        s.remove(x)

def check(x):
    if x in s:
        return 1
    else:
        return 0
    
def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    global s  # 전역변수 선언
    s = set(range(1, 21))

def empty():
    global s  # 전역변수 선언
    s = set()



if __name__ == '__main__':
    n = int(input())
    s = set()  # 전역 변수
    for _ in range(n):
        cal = input().split()
        if cal[0] == 'add':
            add(int(cal[1]))
        elif cal[0] == 'remove':
            remove(int(cal[1]))
        elif cal[0] == 'check':
            print(check(int(cal[1])))   # check함수는 print를 해주어 출력해주기
        elif cal[0] == 'toggle':
            toggle(int(cal[1]))
        elif cal[0] == 'all':
            all()
        else:
            empty()