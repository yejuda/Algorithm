def main():
    stick = [64, 32, 16, 8, 4, 2, 1]

    x = int(input())  # 64보다 작거나 같은 값
    cnt = 0

    for i in stick:
        if x >= i:
            x -= i
            cnt += 1
            
        if x == 0:
            break
        
    print(cnt)

if __name__ == "__main__":
    main()