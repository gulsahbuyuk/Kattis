"""
Author : Gülşah Büyük
Date : 3.07.2020
"""

name = input().split("-")

letter = ""
for n in name:
    letter += n[0][:1:]

print(letter)