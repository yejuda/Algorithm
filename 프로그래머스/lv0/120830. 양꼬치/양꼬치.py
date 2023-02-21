def solution(n, k):

    eat = n * 12000  # 양꼬치 가격
    drink = k * 2000  # 음료수 가격
    
    
    return eat + drink - (n // 10 * 2000)