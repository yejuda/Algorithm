class GoodWordChecker:
    def __init__(self):
        self.stack = []

    def process(self, s):
        self.stack = []  # 매 줄마다 스택 초기화
        
        for i in s:
            if not self.stack:
                self.stack.append(i)
            elif self.stack[-1] == i:
                self.stack.pop()
            else:
                self.stack.append(i)
        return not self.stack  # 스택이 비어 있으면 좋은 문자(True = not False)
    
    
if __name__ == '__main__':
    n = int(input())
    cnt = 0    
    # 클래스 인스턴스 생성
    checker = GoodWordChecker()

    for _ in range(n):
        s = input()
        if checker.process(s):  # 스택이 비어있으면 (True 이면)
            cnt += 1

    print(cnt)