"""
Author : Gülşah Büyük
Date : 14.10.2020
"""

text = input()
cypher = "PER"
day = 0
for i in range(len(text)):
    if text[i] != cypher[i % 3]:
        day += 1
print(day)