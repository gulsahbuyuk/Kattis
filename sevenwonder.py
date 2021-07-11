"""
Author : Gülşah Büyük
Date : 3.08.2020
"""

card = input()
t = 0
c = 0
g = 0
for i in card:
    if i == "T" :
        t += 1
    elif i == "C" :
        c += 1
    elif i == "G" :
        g += 1

set = min(g,min(t,c))
tot = t**2 + c**2 + g**2 + 7*set

print(tot)

