from os import supports_bytes_environ
num = input()
sp_num = num.split('-') 

# 분리된 요소들이 정확히 '010', 'XXXX', 'XXXX' 형태를 가지는지 검사
if len(sp_num) == 3 and sp_num[0] == '010' and len(sp_num[1]) == 4 and len(sp_num[2]) == 4:
  # 각 부분이 숫자로 이루어져있는지 검사
  if sp_num[1].isdigit() and sp_num[2].isdigit():
    print("valid")
  else:
    print("invalid")

# 하나라도 조건에 맞지 않으면 "invalid"를 출력
else:
  print("invalid")

# ==========================================================================================


# # 하이픈 기준으로 숫자가 4글자여야 한다.
# # 숫자는 0부터 9까지 있다.

# # 하이픈 기준으로 숫자를 나누고, 3,4글자인지 확인.

# num = input()
# sp_num = num.split('-')  # ['010', '1232', '1231']

# # 하이픈 기준으로 나눈 것을 for문 돌리면서 길이가 3,4인지 확인,.
# # 3,4가 아니라면 invalid출력

# for i in sp_num:
#   if len(i) != 3 and len(i) != 4:
#     print('invalid')
#     break
# else:
#   # for 루프가 모두 끝나고 중간에 break가 발생하지 않은 경우 'valid' 출력
#   print('valid')
