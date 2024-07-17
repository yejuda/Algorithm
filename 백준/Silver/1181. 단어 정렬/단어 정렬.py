n = int(input())  # 단어 개수
s_list = set()  # 집합 초기화(중복 허용x, 길이 짧은 것부터 적용하기 위해 집합 사용)

for _ in range(n):
  s = input()   # 단어 입력 받기 
  s_list.add(s) 
  
s_list = list(s_list)
s_list.sort()  # 알파벳순으로 정렬
s_list.sort(key=len)  # 길이 순으로 정렬

for i in s_list:
  print(i)