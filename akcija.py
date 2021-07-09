"""
Author : Gülşah Büyük
Date : 15.10.2020
"""

booksNum = int(input())
prices = []
for i in range(booksNum):
    cost = int(input())
    prices.append(cost)

prices.sort()
pos = 1
price = 0

while len(prices) > 0:
    if pos % 3 == 0:
        prices.pop()
    else:
        price += prices.pop()
    pos += 1
print(price)