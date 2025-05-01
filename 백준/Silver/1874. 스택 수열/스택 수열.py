# 수를 스택에 뽑아 늘어놓음으로써 하나의 수열을 만들 수 있다. 
# 스택에 push하는 순서는 반드시 오름차순(1부터 n까지)을 지킨다.
# 1부터 n까지의 숫자를 넣었다 뺐다 하면서 최종적으로 스택이 비게 되는지 아닌지 확인
n = int(input())
st = []
result = []  # 출력 결과를 담을 곳
cnt = 1 # 1부터 n까지 push할 숫자


for _ in range(n):
    # 수 입력 받기
    m = int(input())


    # m이 나올 때까지 push
    while cnt <= m:
        st.append(cnt)
        result.append('+')
        cnt += 1
    
    # 이제 스택 top이 m과 같아야 pop가능!
    if st[-1] == m:
        st.pop()
        result.append('-')
    # 스택의 top이 m과 같지 않다면 수열이 아니다! 같아야 pop을 할 수 있기 때문!!
    else:
        print("NO")
        break

else:
    for r in result:
        print(r)