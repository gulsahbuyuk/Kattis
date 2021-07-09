"""
Author : Gülşah Büyük
Date : 15.10.2020
"""

number = int(input())
won = 0

for i in range(number) :
    battle = str(input())
    if 'CD' not in battle:
        won += 1
    else :
        pass
print(won)
