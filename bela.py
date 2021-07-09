"""
Author : Gülşah Büyük
Date : 3.07.2020
"""

num,domination = input().split()
num = int(num)*4

values = {"A" : 11 , "K" : 4 , "Q" : 3 , "J" : 2 , "T" : 10 , "9" : 0 , "8" : 0 , "7" : 0}
point = 0

for i in range(num):
    card = input()
    if card[0] == "J" and card[1] == domination:
        point += 20
    elif card[0] == "9" and card[1] == domination:
        point += 14
    else:
        point += values[card[0]]

print(point)