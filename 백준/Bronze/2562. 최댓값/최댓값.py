import sys

# 전체 입력을 받아서 처리
input_data = sys.stdin.read().strip().split()

# 문자열 리스트를 정수 리스트로 변환
a = list(map(int, input_data))

print(max(a))
print(a.index(max(a))+1)