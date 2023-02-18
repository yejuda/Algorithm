# def solution(money):
#     americano = money // 5500
#     left = money - (americano * 5500)
#     return [americano, left]

def solution(money):
    return [money // 5500, money % 5500]
