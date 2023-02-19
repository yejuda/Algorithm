def solution(my_string):
    answer = 0

    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

# def solution(my_string):
#     return sum(int(i) for i in my_string if i.isdigit())