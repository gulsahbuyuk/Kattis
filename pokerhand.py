"""
Author : Gülşah Büyük
Date : 29.07.2020
"""

from collections import Counter

hand = input().split()
char = []


for i in hand:
    char.append(i[0])

print(Counter(char).most_common(1)[0][1])
