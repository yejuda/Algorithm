def solution(price, money, count):
    cnt = 0
    emt = 0
    
    while cnt < count:
        
        cnt += 1
        emt += price * cnt
        
    if emt > money:
        return emt-money
    else:
        return 0

