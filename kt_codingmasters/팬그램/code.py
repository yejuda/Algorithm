import string

# 입력 받기
st = input()

# (소문자 형태)알파벳 정보 변수에 넣기
alphabet = string.ascii_lowercase
# set형으로 변경
alphaset = set(alphabet)

# 알파벳 전체(alphaset)가 입력 문자열 집합(set(st.lower()))에 포함되는지 확인
if alphaset <= set(st.lower()):  # 부분집합연산자(alphaset이 set(st.lower())에 포함되어 있는지?)# 소문자형으로 변환 -> 입력받은 문자열을 중복이 없게 하기 위해 set으로 감싸준 후, 
  print('YES')
else:
  print('NO')
