cnt = 0

for _ in range(3):
    st = input()
    cnt += 1
    
    if st.isdigit() and cnt == 1:
        num = int(st) + 3
    elif st.isdigit() and cnt == 2:
        num = int(st) + 2
    elif st.isdigit() and cnt == 3:
        num = int(st) + 1
    else:
        continue

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0 and num % 5 != 0:
    print("Fizz")
elif num % 3 != 0 and num % 5 == 0:
    print("Buzz")
else:
    print(num)