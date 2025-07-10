import sys
input = sys.stdin.readline

total_price = int(input())

sum_of_nine_items = 0

for _ in range(9):
    item_price = int(input())
    sum_of_nine_items += item_price

missing_item_price = total_price - sum_of_nine_items

print(missing_item_price)