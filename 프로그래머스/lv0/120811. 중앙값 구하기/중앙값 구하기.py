def solution(array):
    answer = 0
    array.sort()
    return array[len(array) // 2]