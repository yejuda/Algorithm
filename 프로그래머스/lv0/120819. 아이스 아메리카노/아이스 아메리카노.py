def solution(money):
    americano = money // 5500
    left = money - (americano * 5500)
    return [americano, left]